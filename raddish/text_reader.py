'''----------------- 
# Author: Parker Clark
# Date: 6/22/2024
# Description: A file containing functions related to reading text from the screen.
-----------------'''

#---Imports---#
import pytesseract
import pyautogui
from image_search import locateImage
from utility import _determineRegion
from pyscreeze import Box


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

    #---WIP---#

    # Check if a region is provided
    image = _determineRegion(region=region)

    #region = (top, left, width, height)

    # Take a screenshot of the region
    # TODO: Region only works with hardcoded pixel values, need to fix this
    screenshot = pyautogui.screenshot(region=Box(113, 42, 51, 23))

    # Read the text from the screenshot
    text = pytesseract.image_to_string(screenshot, lang=language)

    # Return the text
    return text