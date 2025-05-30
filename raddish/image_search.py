'''----------------- 
# Author: Parker Clark
# Date: 6/21/2024
# Description: A file containing functions related to image searches
-----------------'''


#---Imports---#
import pyautogui
from pyautogui import ImageNotFoundException
from search_rectangle import SearchRectangle
import time
from typing import Callable as function
from utility import _determineRegion


def locateImage(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, \
                on_success : function = None, on_fail : function = None ) -> tuple[int]:
    '''
    Locate an image on the screen.

    Parameters
    ----------
    image_path : str
        The path to the image to search for.

    confidence : float (Optional)
        The confidence level to search for the image, default is 0.9.

    region : list[int] (Optional)
        A list of four integers that represent a region on the screen.
          The list should be in this format: [x, y, width, height]

    search_rectangle : SearchRectangle (Optional)
        A SearchRectangle object that represents a region on the screen.
    
    on_success : function (Optional)
        An event to trigger when the image is found.
    
    on_fail : function (Optional)
        An event to trigger when the image is not found.

    Returns
    -------
    tuple[int]
        A tuple of two integers that represent the x, y coordinates of the image.
    '''
    # Determine the region to search for the image
    top, left, width, height = _determineRegion(region, search_rectangle)

    # Find the image on the screen
    try:
        image_location = pyautogui.locateOnScreen(image_path, confidence=confidence, region=(top, left, width, height))

        # Trigger the on_success event hook if the image is found
        if image_location != None:

            # Trigger the on_success event hook if it is callable
            if callable(on_success):
                on_success(image_location)

        # Return the image location   
        return image_location
    
    # Trigger the on_fail event hook if the image is not found
    except ImageNotFoundException as e:
        if callable(on_fail):
            on_fail(e)
        raise e
    

def locateAllImages(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, \
                    on_success : function = None, on_fail : function = None) -> list[tuple[int]]:
    '''
    Locate all instances of an image on the screen.

    Parameters
    ----------
    image_path : str
        The path to the image to search for.

    confidence : float (Optional)
        The confidence level to search for the image, default is 0.9.

    region : list[int] (Optional)
        A list of four integers that represent a region on the screen.
          The list should be in this format: [x, y, width, height]

    search_rectangle : SearchRectangle (Optional)
        A SearchRectangle object that represents a region on the screen.
    
    on_success : function (Optional)
        An event to trigger when the image is found.
    
    on_fail : function (Optional)
        An event to trigger when the image is not found.

    Returns
    -------
    list[tuple[int]]
        A list of tuples of two integers that represent the x, y coordinates of the image.
    '''
    # Determine the region to search for the image
    top, left, width, height = _determineRegion(region, search_rectangle)

    # Find the image on the screen
    try:
        image_locations = pyautogui.locateAllOnScreen(image_path, confidence=confidence, region=(top, left, width, height))

        # Trigger the on_success event hook if the image is found
        if image_locations != None and callable(on_success):
            on_success(image_locations)
    
        # Return the image locations
        return image_locations
    
    # Trigger the on_fail event hook if the image is not found
    except ImageNotFoundException as e:
        if callable(on_fail):
            on_fail(e)
        raise e
    

def clickImage(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, timeout = 0):
    '''
    Click on an image on the screen. Will wait for the image to appear if a timeout is provided.

    Parameters
    ----------
    image_path : str
        The path to the image to search for.

    confidence : float (Optional)
        The confidence level to search for the image, default is 0.9.

    region : list[int] (Optional)
        A list of four integers that represent a region on the screen.
          The list should be in this format: [x, y, width, height]

    search_rectangle : SearchRectangle (Optional)
        A SearchRectangle object that represents a region on the screen.

    timeout : int (Optional)
        The amount of time in seconds to wait for the image to appear on the screen.
    '''
    # Determine the region to search for the image
    top, left, width, height = _determineRegion(region, search_rectangle)

    # Find the image on the screen
    try:
        # Find the image on the screen, wait for a timeout if necessary
        image_location = waitForImage(image_path, confidence=confidence, region=(top, left, width, height), search_rectangle=search_rectangle, timeout=timeout)

        # Click on the image
        pyautogui.click(image_location)
    
    # Raise an exception if the image is not found
    except ImageNotFoundException as e:
        raise e


def clickAllImages(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, timeout = 0):
    '''
    Click on all instances of an image on the screen. Also uses a timeout to sleep after the click.

    Parameters
    ----------
    image_path : str
        The path to the image to search for.

    confidence : float (Optional)
        The confidence level to search for the image, default is 0.9.

    region : list[int] (Optional)
        A list of four integers that represent a region on the screen.
          The list should be in this format: [x, y, width, height]

    search_rectangle : SearchRectangle (Optional)
        A SearchRectangle object that represents a region on the screen.

    timeout : int (Optional)
        The amount of time in seconds to wait for the image to appear on the screen.
    '''
    # Determine the region to search for the image
    top, left, width, height = _determineRegion(region, search_rectangle)

    # Find the image on the screen
    try:

        # Find all instances of the image on the screen, wait for a timeout if necessary
        image_locations = waitForAllImages(image_path, confidence=confidence, region=(top, left, width, height), search_rectangle=search_rectangle, timeout=timeout)

        # Click on all instances of the image
        for image_location in image_locations:
            pyautogui.click(image_location, interval=timeout)

    # Raise an exception if the image is not found
    except ImageNotFoundException as e:
        raise e


def waitForImage(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, timeout = 0):
    '''
    Wait for an image to appear on the screen.

    Parameters
    ----------
    image_path : str
        The path to the image to search for.

    confidence : float (Optional)
        The confidence level to search for the image, default is 0.9.

    region : list[int] (Optional)
        A list of four integers that represent a region on the screen.
          The list should be in this format: [x, y, width, height]

    search_rectangle : SearchRectangle (Optional)
        A SearchRectangle object that represents a region on the screen.

    timeout : int (Optional)
        The amount of time in seconds to wait for the image to appear on the screen.
    '''
     # Determine the region to search for the image
    top, left, width, height = _determineRegion(region, search_rectangle)

    # Record the start time
    start_time = time.time()

    # Find the image on the screen
    while True:
        
        try:
            pyautogui.locateOnScreen(image_path, confidence=confidence, region=(top, left, width, height))
            return
        except ImageNotFoundException as e:
            pass

        if time.time() - start_time > timeout:
            raise ImageNotFoundException(f"The image: '{image_path}' was not found within the timeout period.")
        
        # Sleep to space out the searches
        time.sleep(0.1)
    
def waitForAllImages(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, timeout = 0):
    '''
    Wait for all instances of an image to appear on the screen.

    Parameters
    ----------
    image_path : str
        The path to the image to search for.

    confidence : float (Optional)
        The confidence level to search for the image, default is 0.9.

    region : list[int] (Optional)
        A list of four integers that represent a region on the screen.
          The list should be in this format: [x, y, width, height]

    search_rectangle : SearchRectangle (Optional)
        A SearchRectangle object that represents a region on the screen.

    timeout : int (Optional)
        The amount of time in seconds to wait for the image to appear on the screen.
    '''
    # Determine the region to search for the image
    top, left, width, height = _determineRegion(region, search_rectangle)

    # Record the start time
    start_time = time.time()

    # Find the images on the screen
    while True:

        try:
            pyautogui.locateAllOnScreen(image_path, confidence=confidence, region=(top, left, width, height))
            return
        except ImageNotFoundException as e:
            pass
        
        # Raise an exception if the timeout is reached
        if time.time() - start_time > timeout:
            raise ImageNotFoundException(f"The image: '{image_path}' was not found within the timeout period.")
        
        # Sleep to space out the searches
        time.sleep(0.1)


