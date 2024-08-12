import time
import warnings

import allure
import colorama
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options

from app.application import Application
from configuration.config import Datatest


def before_scenario(context, scenario):
    print("################")
    print("[ CONFIGURACION ] - Initializing the controller configuration")
    print("################")

    caps = Datatest.ANDROID_CONFIG_EMU

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        capabilities_options = UiAutomator2Options().load_capabilities(caps)
        context.driver = webdriver.Remote(command_executor=Datatest.URL, options=capabilities_options)
        context.driver.implicitly_wait(Datatest.IMPLICIT_WAIT)
        context.application = Application(context.driver)
    print("################")
    print("[ SCENARIO ] - " + scenario.name)
    print("################")


def after_scenario(context, scenario):

    if scenario.status == "failed":
        failed_step_name = None
        scenario_name = scenario.name
        for step in scenario.steps:
            if step.status == "failed":
                failed_step_name = step.name
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        screenshot_name = f"{scenario_name}_{failed_step_name}_{current_time}"
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.JPG)
        context.driver.terminate_app(Datatest.PACKAGE_MYAC)
        colorama.init()
        print(f"{colorama.Fore.RED}###############################################{colorama.Fore.RED}")
        print(f"{colorama.Fore.RED}[  DRIVER STATUS  ] - Cleaning and closing controller instance due to scenario error {colorama.Fore.RED}")
        print(f"{colorama.Fore.RED}{scenario_name}{colorama.Fore.RED}")
        print(f"{colorama.Fore.RED}###############################################{colorama.Fore.RESET}")
        print("____________________________________________________________________________")
    elif scenario.status == "passed":
        print(f"{colorama.Fore.GREEN}----------------------")
        print(f"[  SCENARIO STATUS  ] - Success Test (PASS): {scenario.name}")
        print(f"----------------------{colorama.Fore.RESET}")
        context.driver.terminate_app(Datatest.PACKAGE_MYAC)
    context.driver.quit()

