
import io

import time

import allure


from PIL import Image
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.config import Datatest
import base64


class BaseActions:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def Tiempo(tie):
        time.sleep(tie)


    #################################### CLICK ON ELELMENT WITH METHOD BY ###################################

    def clickOnElementBySelector(self, by_tipo: str, selector: str, tiempo: float):
        """
        Hacer click sobre un elemento

        :param by_tipo: ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta o path del elemento a cliquear.
        :param tiempo: valor numerico tipo float que determina el tiempo de espera.
        :return: Accion de hacer click sobre un elemento específico
        """

        try:
            ele = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located((by_tipo, selector)))
            ele.click()
            print(f" Click on the element: {selector}")
            allure.attach(f" Click on the element: {selector}", "click on an element",
                          attachment_type=AttachmentType.TEXT)
            BaseActions.Tiempo(tiempo)
        except TimeoutException as ex:
            assert False, f"Error: Time spent waiting while searching " \
                          f"The element {selector} of type {by_tipo}\n The error is: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: Item not found {selector} of type {by_tipo}\n The error is: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: Cannot interact with the element {selector} " \
                          f"of type {by_tipo}\n The error is: {ex}"
        except Exception as ex:
            assert False, f"Unknown error: {ex}"


    ################################## EVALUATE ELEMENT TO RETURN BOOLEAN ##############################

    def findElementIsVisibleBySelector(self, by_tipo: str, selector: str, timeout: float):
        """
        Esta funcion permite Encontrar un texto específico en pantalla y que retorne True si lo consigue

        :param timeout: Tiempo de espera hasta que no se encuentre el elemento
        :param by_tipo: Ingresar el tipo de selector a usar, si es XPATH, CLASS_NAME, ID, etc.
        :param selector: Ruta del elemento a localizar para identificar si está visible.
        :return: Un valor True si se encuentra el elemento en pantalla de ser caso contrario retornará False
        """

        try:
            result = False
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located
                                                                ((by_tipo, selector)))
            if element.is_displayed():
                result = True
                print(f"Se encontro en pantalla el elemento: {selector} de tipo {by_tipo}")
            return result
        except TimeoutException as ex:
            assert False, f"Error: Time spent waiting while searching " \
                          f"The element {selector} of type {by_tipo}\n The error is: {ex}"
        except NoSuchElementException as ex:
            assert False, f"Error: Item not found {selector} of type {by_tipo}\n The error is: {ex}"
        except ElementNotInteractableException as ex:
            assert False, f"Error: Cannot interact with the element {selector} " \
                          f"of type {by_tipo}\n The error is: {ex}"
        except Exception as ex:
            assert False, f"Unknown error: {ex}"


    #################################### ALLURE SCREENCSHOT ##############################################

    def screenshot(self, name=str):
        """
        Funcion que permite tomar una captura de pantalla

        :param
            nombre (str): Nombre con el cual se guardata la captura.
        :return
            Captura de pantalla en el reporte allure
        """

        # allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.JPG)
        # print("Imagen capturada")
        # BaseActions.Tiempo(0.5)

        # Capture the screenshot in PNG format
        screenshot = self.driver.get_screenshot_as_png()

        # Convert the screenshot to a PIL Image object using BytesIO
        image = Image.open(io.BytesIO(screenshot))

        # Convert the image to RGB if it's in RGBA mode
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Compress the image and store it in a BytesIO object
        compressed_image_io = io.BytesIO()
        image.save(compressed_image_io, format='JPEG', quality=85)
        compressed_image_io.seek(0)  # Rewind the BytesIO object to the beginning

        # Read the compressed image data from the BytesIO object
        compressed_image_data = compressed_image_io.read()

        # Attach the screenshot to the Allure report
        allure.attach(compressed_image_data, name, attachment_type=AttachmentType.JPG)
        print("Screenshot Success")
        BaseActions.Tiempo(0.5)

        # allure.attach("Se cumplió el cometido de la funcion", nombre, , attachment_type=AttachmentType.TEXT)
        # print("Imagen capturada")
        # BaseActions.Tiempo(0.5)

