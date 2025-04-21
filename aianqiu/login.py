import requests
import json

import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# 参数
PRIVATE_KEY = "c058579161250b37"
getSecret = "48dce77cf43eb6c3APP"
orgid = "137"

def get_md5(text: str) -> str:
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def aes_encrypt_cbc_pkcs7(plaintext: str, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext.encode('utf-8'), AES.block_size)
    return cipher.encrypt(padded)

def encrypt(text: str) -> str:
    md5_str = get_md5(PRIVATE_KEY + getSecret + orgid)  # 32字符ASCII hex字符串
    key_bytes = md5_str.encode('utf-8')  # 注意这里是ASCII编码！长度32字节

    iv_bytes = b"0000000000000000"  # 16个ASCII字符'0'

    encrypted_bytes = aes_encrypt_cbc_pkcs7(text, key_bytes, iv_bytes)
    return base64.b64encode(encrypted_bytes).decode()


headers = {
    "encrypt": "1",
    "version": "1.1.5",
    "orgid": "137",
    "User-Agent": "chuangqi.o.137.com.iqilu.app137/1.1.5",
    "timestamp": "1745203686",
    "noncestr": "huangye",
    "sign": "5eea416d79ffd33cc1ba408c47273393",
    "x-requested-with": "XMLHttpRequest",
    "imei": "65d8cde6300c49d4",
    "CQ-AGENT": "{\"os\":\"android\",\"brand\":\"google\",\"osversion\":\"10\",\"network\":\"wifi\",\"device_model\":\"Pixel 2 XL\",\"version\":\"1.1.5\",\"core\":\"3.4.10\",\"imei\":\"65d8cde6300c49d4\"}",
    "cq-token": "",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "app-auth.iqilu.com"
}
# cookies = {
#     "redirectToken": "50dd7328857e480697c2d85c73935a7c-140049166",
#     "redirect": ""
# }
pwd="11111111"
result = encrypt(pwd)
print("加密结果Base64:", result)
url = "https://app-auth.iqilu.com/member/login"
params = {
    "e": "1"
}
data = {
    "codeKey": "",
    "password": result,
    "code": "",
    "phone": "18320975327",
    "key": ""
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)
