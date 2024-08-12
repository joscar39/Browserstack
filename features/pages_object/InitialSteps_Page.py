

from support.BaseActions import BaseActions
from support.GeneralLocators import LocatorsInitialStepPage as lsp

# time sleep
sleep = 0.5

# Definicion de timeout exeception al buscar elementos
timeout = 80

class InitialStepsPage(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    def ValidateModalPermitsNotification(self):
        val = BaseActions.findElementIsVisibleBySelector(self, lsp.locator_validate_modal_permits_notification[0],
                                                         lsp.locator_validate_modal_permits_notification[1], sleep)
        if val:
            BaseActions.screenshot(self, "The modal permits Notification was displayed correctly")
        else:
            assert False, "the modal permits notification is not displayed."

    def ClickOnButtonAllowPermitsNotification(self):
        BaseActions.clickOnElementBySelector(self, lsp.locator_button_allow_permits[0],
                                             lsp.locator_button_allow_permits[1], sleep)

    def ValidateModalStepsTutorial(self):
        val = BaseActions.findElementIsVisibleBySelector(self, lsp.locator_validate_step_tutorial[0],
                                                         lsp.locator_validate_step_tutorial[1], sleep)
        if val:
            BaseActions.screenshot(self, "The modal Steps Tutorial was displayed correctly.")
        else:
            assert False, "The modal steps tutorial is not displayed"

    def ClickOnButtonSkipStepsTutorial(self):
        BaseActions.clickOnElementBySelector(self, lsp.locator_button_skip_tutorial[0],
                                             lsp.locator_button_skip_tutorial[1], sleep)

    def ValidateModalLogoAlCambio(self):
        val = BaseActions.findElementIsVisibleBySelector(self, lsp.locator_validate_logo[0],
                                                         lsp.locator_validate_logo[1], sleep)
        if val:
            BaseActions.screenshot(self, "The logo Al Cambio was displayed correctly.")
        else:
            assert False, "The logo Al Cambio is not displayed"