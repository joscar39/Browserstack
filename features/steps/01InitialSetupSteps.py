from behave import *
from app.application import Application


@given(u'Open the app Al Cambio')
def step_impl(context):
    try:
        context.application = Application(context.driver)
    except Exception as ex:
        assert False, f"Failed the step when initializing the Al Cambio application.\n Motivo del Error: {ex}"

@then(u'Show Modal permits notification')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidateModalPermitsNotification()
    except Exception as ex:
        assert False, f"Failed step to validate Show Modal permits notification\n Motivo del Error: {ex}"

@when(u'Push allow permits notification')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ClickOnButtonAllowPermitsNotification()
    except Exception as ex:
        assert False, f"Failed the step by clicking on the allow permits notification.\n Motivo del Error: {ex}"

@then(u'Check modal of steps tutorial')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidateModalStepsTutorial()
    except Exception as ex:
        assert False, f"Failed the step to validate that Check modal of steps tutorial is displayed.\n Motivo del Error: {ex}"

@when(u'Skin steps tutorial')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ClickOnButtonSkipStepsTutorial()
    except Exception as ex:
        assert False, f"Failed the step by clicking on the Skin steps tutorial.\n Motivo del Error: {ex}"


@then(u'Validate logo app')
def step_impl(context):
    try:
        context.application.InitialStepsPage.ValidateModalLogoAlCambio()
    except Exception as ex:
        assert False, f"Failed the step to Validate logo app is displayed.\n Motivo del Error: {ex}"
