import base64
import os
import shutil
import tkinter.filedialog
import requests
from PIL import Image, ImageTk

# 将getaccesstoken.py中获取的token复制到下方
access_token = ''

headers = {'content-type': 'application/json'}


def open_file(parent=None):
    """打开文件"""
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=[('JPG', '.jpg'), ('JPEG', '.jpeg'), ('PNG', '.png'), ('BMP', '.bmp')], parent=parent)
    return file_path


def modify_img(file_path, x, y):
    """将选择的图片处理成合适显示的大小"""
    up_img = Image.open(file_path)  # PhotoImage打开会报错，使用PIL库的ImageTK
    # 按比例将图片缩放到Frame大小，也可以用self.up_img.size[0]或.size[1]获取宽高数值
    if up_img.width <= x and up_img.height <= y:
        return ImageTk.PhotoImage(up_img)
    else:
        if up_img.width - x > up_img.height - y:
            rate = round(x / up_img.width, 1)
            print('1')
            print(up_img.width * rate)
            print(up_img.height * rate)
            # pillow中调整图片大小的方法，第二个参数是图片质量Image.NEAREST ：低质量Image.BILINEAR：双线性Image.BICUBIC ：三次样条插值Image.ANTIALIAS：高质量
            return ImageTk.PhotoImage(
                up_img.resize((int(up_img.width * rate), int(up_img.height * rate)), Image.ANTIALIAS))
        else:
            rate = round(y / up_img.height, 1)
            print('2')
            print(up_img.width * rate)
            print(up_img.height * rate)
            return ImageTk.PhotoImage(
                up_img.resize((int(up_img.width * rate), int(up_img.height * rate)), Image.ANTIALIAS))


def base64_recognition(file, params):
    """将本地图片编码为base64上传识别"""
    with open(file, 'rb') as f:
        img_base64 = base64.b64encode(f.read())
        b64 = img_base64.decode()
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = "{\"image\":\"" + b64 + "\",\"image_type\":\"BASE64\",\"face_field\":\"" + params + "\",\"max_face_num\":\"30\"} "
    # TODO: access_token只有一个月有效期，最后记得完善一下
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    # TODO: 之后完善一下报错功能
    if response:
        print(response.json())
        return response.json()


def compare_request(file1, file2, params1, params2):
    """人脸对比请求"""
    with open(file1, 'rb') as f1:
        img1_base64 = base64.b64encode(f1.read())
        img1_b64 = img1_base64.decode()
    with open(file2, 'rb') as f2:
        img2_base64 = base64.b64encode(f2.read())
        img2_b64 = img2_base64.decode()

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    print(params1)
    print(params2)
    params = "[{\"image\": \"" + img1_b64 + "\", \"image_type\": \"BASE64\", \"face_type\": \"" + params1 + "\", \"quality_control\": \"LOW\"},{\"image\": \"" + img2_b64 + "\", \"image_type\": \"BASE64\", \"face_type\": \"" + params2 + "\", \"quality_control\": \"LOW\"}]"
    # print(params)
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        return response.json()['result']['score']


def get_group():
    """获取用户组列表"""
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist"

    params = "{\"start\":0,\"length\":100}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        for group_folder in response.json()['result']['group_id_list']:
            if os.path.exists('FaceDatabase\\' + group_folder):
                print('组文件夹存在')
            else:
                os.mkdir('FaceDatabase\\' + group_folder)
        return response.json()['result']['group_id_list']


def get_user(group_id):
    """获取选定组内用户列表"""
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"

    params = "{\"group_id\":\"" + group_id + "\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        for user_folder in response.json()['result']['user_id_list']:
            if os.path.exists('FaceDatabase\\' + group_id + '\\' + user_folder):
                print('用户文件夹存在')
            else:
                os.mkdir('FaceDatabase\\' + group_id + '\\' + user_folder)
        return response.json()['result']['user_id_list']


def get_user_face_list(group_id, user_id):
    """获取用户人脸token"""
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist"

    params = "{\"user_id\":\"" + user_id + "\",\"group_id\":\"" + group_id + "\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        return response.json()['result']['face_list']


def new_group(group_id):
    """新建用户组"""
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/add"

    params = "{\"group_id\":\"" + group_id + "\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        if response.json()['error_code'] == 0:
            os.mkdir('FaceDatabase\\' + group_id)
        else:
            print('创建用户组失败')


def new_user(file, group_id, user_id):
    """新建用户"""
    with open(file, 'rb') as f:
        f1_base64 = base64.b64encode(f.read())
        f1_b64 = f1_base64.decode()
    if os.path.exists('FaceDatabase/' + group_id + '/' + user_id):
        print('用户已存在')
    else:
        os.mkdir('FaceDatabase\\' + group_id + '\\' + user_id)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    params = "{\"image\":\"" + f1_b64 + "\",\"image_type\":\"BASE64\",\"group_id\":\"" + group_id + "\",\"user_id\":\"" + user_id + "\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        Image.open(file).save(
            'FaceDatabase\\' + group_id + '\\' + user_id + '\\' + str(response.json()['result']['face_token']) + '.jpg')


def delete_group(group_id):
    """删除组"""
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/delete"
    params = "{\"group_id\":\"" + group_id + "\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        if response.json()['error_code'] == 0:
            shutil.rmtree('FaceDatabase\\' + group_id)  # 会删除整个目录，无论是否空，os.removedir()不能删除非空目录


def delete_user(group_id, user_id):
    """删除用户"""
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete"
    params = "{\"group_id\":\"" + group_id + "\",\"user_id\":\"" + user_id + "\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        if response.json()['error_code'] == 0:
            shutil.rmtree('FaceDatabase\\' + group_id + '\\' + user_id)


def face_search(file, group_id):
    with open(file, 'rb') as f:
        img_base64 = base64.b64encode(f.read())
        img_b64 = img_base64.decode()
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    params = "{\"image\":\"" + img_b64 + "\",\"image_type\":\"BASE64\",\"group_id_list\":\"" + group_id + "\",\"max_user_num\":\"4\"}"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        return response.json()['result']['user_list']
