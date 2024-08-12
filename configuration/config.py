import os


class Datatest:
    URL = "http://localhost:4723/wd/hub"
    IMPLICIT_WAIT = 10

    # Package y Activity de la aplicacion a testear y la Base URl para endpoint
    PACKAGE_MYAC = "com.alcambio.app"
    ACTIVITY_MYAC = ".MainActivity"

    # Ruta para apk Assist Card
    PATH_APK_MYAC = os.path.abspath("resources/app.apk")

    ##################### CONFIGURACION DE CAPABILITIES ########################################

    ANDROID_CONFIG_EMU = {
        "platformName": "Android",
        "appium:platformVersion": "14",
        "appium:deviceName": "tapas_global",  # "emulator64_x86_64_arm64",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": f"{PACKAGE_MYAC}",
        "appium:appActivity": f"{ACTIVITY_MYAC}",
        "app": f"{PATH_APK_MYAC}",
        "appium:grantPermissions": "true",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 60,
        "appium:connectHardwareKeyboard": True,
        "resetKeyboard": True
    }
