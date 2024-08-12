from selenium.webdriver.common.by import By


class LocatorsInitialStepPage:
    # Localizadores por ruta HTML
    locator_validate_modal_permits_notification = (By.ID, "com.android.permissioncontroller:id/permission_message")
    locator_button_allow_permits = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    locator_validate_step_tutorial = (By.XPATH, "//android.widget.TextView[@resource-id='stepDescription']")
    locator_button_skip_tutorial = (By.XPATH, "//android.widget.TextView[@text='Omitir']")
    locator_validate_logo = (By.XPATH, "//android.widget.ImageView[@content-desc='logo']")
