Java.perform(function () {
    console.log('start')
    let SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
    SecurityUtil["encodeMD5"].implementation = function (str) {
        console.log(`SecurityUtil.encodeMD5 is called: str=${str}`);
        let result = this["encodeMD5"](str);
        console.log(`SecurityUtil.encodeMD5 result=${result}`);
        return result;
    };
})

// frida -U -F com.che168.autotradercloud -l hook_sign.js -o _sign.txt

// W@oC!AH_6Ew1f6%8_appidatc.androidappversion3.56.0channelidcsypwd1bbd886460827015e5d605ed44252251signkeytypeudidS3KJXNRAzOSximUXFrAa5ZVTZjiglix2pJp2gMbDupOBdhBk4uNzct1FHBO2 bfHoLf5ogf4VAolde7zJo2NIvA==username18320975328W@oC!AH_6Ew1f6%8