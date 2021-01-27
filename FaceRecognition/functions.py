import base64
import tkinter.filedialog

import requests
from PIL import Image, ImageTk


def open_file():
    """打开文件"""
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=[('JPG', '.jpg'), ('JPEG', '.jpeg'), ('PNG', '.png'), ('BMP', '.bmp')])
    return file_path


def modify_img(file_path, x, y):
    """将选择的图片处理成合适显示的大小"""
    up_img = Image.open(file_path)  # PhotoImage打开会报错，使用PIL库的ImageTK
    # 按比例将图片缩放到Frame大小，也可以用self.up_img.width或.height获取宽高数值
    if (up_img.size[0] / up_img.size[1]) > (x / y):
        rate = x / up_img.size[0]
    else:
        rate = y / up_img.size[1]
    rate = round(rate, 1)
    # pillow中调整图片大小的方法，第二个参数是图片质量Image.NEAREST ：低质量Image.BILINEAR：双线性Image.BICUBIC ：三次样条插值Image.ANTIALIAS：高质量
    out_img = up_img.resize((int(up_img.size[0] * rate), int(up_img.size[1] * rate)), Image.ANTIALIAS)
    return ImageTk.PhotoImage(out_img)


access_token = '24.037e02027b589adb179b494a9c83aff7.2592000.1613726893.282335-23545866'


def base64_recognition(file, params):
    """将本地图片编码为base64上传"""
    with open(file, 'rb') as f:
        img_base64 = base64.b64encode(f.read())
        b64 = img_base64.decode()
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = "{\"image\":\"" + b64 + "\",\"image_type\":\"BASE64\",\"face_field\":\"" + params + "\",\"max_face_num\":\"30\"} "
    # TODO: access_token只有一个月有效期，最后记得完善一下
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    # TODO: 之后完善一下报错功能
    if response:
        return response.json()


def compare_request(file1, file2, params1, params2):
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
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()['result']['score']

def get_group():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist"

    params = "{\"start\":0,\"length\":100}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()['result']['group_id_list']

def get_user(group_id):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"

    params = "{\"group_id\":\""+group_id+"\"}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()['result']['user_id_list']