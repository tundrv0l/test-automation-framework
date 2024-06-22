'''----------------- 
# Author: Parker Clark
# Date: 6/22/2024
# Description: A file containing functions related to reading text from the screen.
-----------------'''

#---Imports---#
import pytesseract
from PIL import Image
import pyautogui
from image_search import locateImage
from utility import _determineRegion


def readText(region : list[int] = None, language : str = 'eng') -> str:
    '''
    Read text from the screen using the Tesseract OCR engine.

    Parameters
    ----------
    region : list[int]
        A list of four integers that represent a region on the screen.
          The list should be in this format: [left, top, width, height]
    
    language : str (Default = 'eng')
        The language that the Tesseract engine should use to read the text.

    Returns
    -------
    str
        The text that was read from the screen.
    '''

    # Check if a region is provided
    top, left, width, height = _determineRegion(region=region)

    # Take a screenshot of the region
    screenshot = pyautogui.screenshot(region=(top, left, width, height))

    # Read the text from the screenshot
    text = pytesseract.image_to_string(screenshot, lang=language)

    # Return the text
    return text