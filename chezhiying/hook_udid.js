Java.perform(function () {
    let UpgradeAppDialog = Java.use("com.che168.autotradercloud.upgradeapp.UpgradeAppDialog");
    UpgradeAppDialog["show"].implementation = function () {
        console.log(`UpgradeAppDialog.show is called`);
        // this["show"]();
    };
    console.log("hook_udid")
    let SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
    SecurityUtil["encode3Des"].implementation = function (context, str) {
        console.log(`SecurityUtil.encode3Des is called: context=${context}, str=${str}`);
        let result = this["encode3Des"](context, str);
        console.log(`SecurityUtil.encode3Des result=${result}`);
        return result;
    };

    console.log("get 3des key")
    let CheckSignUtil = Java.use("com.autohome.ahkit.jni.CheckSignUtil");
    CheckSignUtil["get3desKey"].implementation = function (context) {
        console.log(`CheckSignUtil.get3desKey is called: context=${context}`);
        let result = this["get3desKey"](context);
        console.log(`CheckSignUtil.get3desKey result=${result}`);
        return result;
    };
    console.log("write")
    let PreferenceHelper = Java.use("com.autohome.ahkit.utils.PreferenceHelper");
    PreferenceHelper["write"].overload('android.content.Context', 'java.lang.String', 'java.lang.String', 'int').implementation = function (context, str, str2, i) {
        console.log(`PreferenceHelper.write is called: context=${context}, str=${str}, str2=${str2}, i=${i}`);
        this["write"](context, str, str2, i);
    };
})

// frida -U -F com.che168.autotradercloud -l hook_sign.js -o _sign.txt
// SecurityUtil.encode3Des is called: context=com.che168.autotradercloud.ATCApplication@6d95011, str=0d299257-a11a-3a1a-93fe-3d0a202f6085|15262252626129|391134
// SecurityUtil.encode3Des result=S3KJXNRAzOSximUXFrAa5ZVTZjiglix2pJp2gMbDupMD0zHxKqcKcXHpaBDatsDvBew9CLVkpflo70HQ8U6UfQ==
