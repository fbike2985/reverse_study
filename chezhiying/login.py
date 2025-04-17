import base64
import uuid
import requests
import hashlib
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import time
import jpype

jvmPath = jpype.getDefaultJVMPath()
d = 'unidbg-android.jar'  # 对应jar地址
# jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=" + d + "")
jpype.startJVM(jvmPath, "-Dfile.encoding=utf-8", "-Djava.class.path=" + d + "")  # 输出乱码时使用
java = jpype.JClass("com.chezhiying.CheZhiYing")()  # 从com开始找到打包jar的类
signature = java.sign()
print(signature)


def encode_3des(key, iv, plaintext):
    """
    key: 字符串，长度必须是16或24字节(字节数，不是字符数)
    iv: 8字节字节串
    plaintext: 要加密的字符串 (utf-8编码)
    """
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    # 生成密钥，使用24字节key，若长度16则需要转换
    if len(key_bytes) not in (16, 24):
        raise ValueError("Key must be either 16 or 24 bytes long")

    if len(iv_bytes) != 8:
        raise ValueError("IV must be 8 bytes long")

    cipher = DES3.new(key_bytes, DES3.MODE_CBC, iv_bytes)
    padded_text = pad(plaintext.encode('utf-8'), DES3.block_size)  # PKCS5Padding本质是PKCS7，3DES block_size=8
    encrypted_bytes = cipher.encrypt(padded_text)
    # base64 encode返回字符串
    encrypted_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_b64


def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()


def dict_to_custom_string(data, wrapper, keys_order):
    """
    data: 字典
    wrapper: 包裹字符串
    keys_order: 需要拼接的key列表，按顺序拼接对应kv
    """
    middle = ''.join(f"{k}{data[k]}" for k in keys_order if k in data)
    return f"{wrapper}{middle}{wrapper}"


keys = ["_appid", "appversion", "channelid", "pwd", "signkey", "type", "udid", "username"]
uuid = str(uuid.uuid4())
nano_time = time.perf_counter_ns()

key = signature[:24]
iv = "appapich"  # 8字节长度
plaintext = f"{uuid}|{nano_time}|391134"
headers = {
    "Host": "dealercloudapi.che168.com",
    "cache-control": "public, max-age=0",
    "traceid": "atc.android_8ad494fc-b0e1-4538-a2d9-2cf08c6f954f",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "okhttp/3.14.9"
}
url = "https://dealercloudapi.che168.com/tradercloud/sealed/login/login.ashx"
user = "18320975327"
pwd = "1111111"
data = {
    "_appid": "atc.android",
    "_sign": "AFB212EB924E53A3885A570470889876",
    "appversion": "3.56.0",
    "channelid": "csy",
    "pwd": get_md5(pwd),
    "signkey": "",
    "type": "",
    "udid": "S3KJXNRAzOSximUXFrAa5ZVTZjiglix2pJp2gMbDupNDDp5lUjQtR0irrdrp 3IhOMBB190nsLXwcKxZeJxLdgg==",
    "username": user
}

udid = encode_3des(key, iv, plaintext)
data['udid'] = udid

_sign = get_md5(dict_to_custom_string(data, "W@oC!AH_6Ew1f6%8", keys))
data['_sign'] = _sign
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
jpype.shutdownJVM()  # 关闭JVM（注意，必须在所有子线程结束后再关闭，不用子线程调用加密方法会失败）
