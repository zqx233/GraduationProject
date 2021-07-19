import requests

#client_id 为官网获取的AK， client_secret 为官网获取的SK，填写在下方，把返回的的access token复制到function.py，一个月有效期
client_id = ''
client_secret = ''
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(
    client_id, client_secret)
response = requests.get(host)
if response:
    print(response.json())