Java.perform(function () {
    let EncryptUtil = Java.use("com.iqilu.core.util.EncryptUtil");
    EncryptUtil["aesPassword"].implementation = function (str) {
        console.log(`EncryptUtil.aesPassword is called: str=${str}`);
        let result = this["aesPassword"](str);
        console.log(`EncryptUtil.aesPassword result=${result}`);
        return result;
    };
    console.log("--------------------------------------------------------------------")

    console.log("getSecret:::")
    EncryptUtil["getSecret"].implementation = function () {
        console.log(`EncryptUtil.getSecret is called`);
        let result = this["getSecret"]();
        console.log(`EncryptUtil.getSecret result=${result}`);
        return result;
    };
    console.log("--------------------------------------------------------------------")

    console.log("getOrgId:::")
    let AppUtils = Java.use("com.iqilu.core.util.AppUtils");
    AppUtils["getOrgId"].implementation = function () {
        console.log(`AppUtils.getOrgId is called`);
        let result = this["getOrgId"]();
        console.log(`AppUtils.getOrgId result=${result}`);
        return result;
    };
    console.log("--------------------------------------------------------------------")
    console.log("md5:::")
    EncryptUtil["getMD5"].implementation = function (str) {
        console.log(`EncryptUtil.getMD5 is called: str=${str}`);
        let result = this["getMD5"](str);
        console.log(`EncryptUtil.getMD5 result=${result}`);
        return result;
    };
    console.log("--------------------------------------------------------------------")
    console.log("EncryptUtils:::")
    let EncryptUtils = Java.use("com.blankj.utilcode.util.EncryptUtils");
EncryptUtils["symmetricTemplate"].implementation = function (bArr, bArr2, str, str2, bArr3, z) {
    // 转byte[]数组成字符串（假设UTF-8）
    function bytesToString(byteArray) {
        return Java.array('byte', byteArray).map(b => String.fromCharCode(b & 0xFF)).join('');
    }

    // bArr明文字符串
    let plainText = bArr ? Java.use("java.lang.String").$new(bArr, "UTF-8").toString() : null;
    // bArr2密钥字符串
    let keyText = bArr2 ? Java.use("java.lang.String").$new(bArr2, "UTF-8").toString() : null;
    // bArr3 iv字符串
    let ivText = bArr3 ? Java.use("java.lang.String").$new(bArr3, "UTF-8").toString() : null;

    console.log(`symmetricTemplate called:  
      bArr (plaintext): ${plainText}  
      bArr2 (key): ${keyText}  
      str: ${str}  
      str2: ${str2}  
      bArr3 (iv): ${ivText}  
      z(encrypt?): ${z}`);

    let result = this["symmetricTemplate"](bArr,bArr2,str,str2,bArr3,z);
    console.log(`Result bytes array: ${result}`);
    return result;
};
});


// EncryptUtil.aesPassword is called: str=11111111
// EncryptUtil.aesPassword result=oHplfhe1CAA7Ixk3mreh6Q==
