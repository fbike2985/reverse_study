Java.perform(function () {
    let UpgradeAppDialog = Java.use("com.che168.autotradercloud.upgradeapp.UpgradeAppDialog");
    UpgradeAppDialog["show"].implementation = function () {
        console.log(`UpgradeAppDialog.show is called`);
        // this["show"]();
    };
})

// frida -U -f com.che168.autotradercloud -l byupdate.js