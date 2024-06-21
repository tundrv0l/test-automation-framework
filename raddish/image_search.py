'''----------------- 
# Author: Parker Clark
# Date: 6/21/2024
# Description: A file containing functions related to image searches
-----------------'''

#---Imports---#
import pyautogui
from pyautogui import ImageNotFoundException
from search_rectangle import SearchRectangle

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
        return image_location
    except ImageNotFoundException as e:
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
        return image_locations
    except ImageNotFoundException as e:
        raise e
    
def clickImage(image_path: str, confidence: float = 0.9, region: list[int] = None, search_rectangle: SearchRectangle = None, timeout = 0):
    '''
    Click on an image on the screen. Also uses a timeout to sleep after the click.

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
        pyautogui.click(image_location, interval=timeout)
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
        for image_location in image_locations:
            pyautogui.click(image_location, interval=timeout)
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

    # Find the image on the screen
    try:
        pyautogui.locateOnScreen(image_path, confidence=confidence, region=(top, left, width, height), timeout=timeout)
    except ImageNotFoundException as e:
        raise e
    
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

    # Find the image on the screen
    try:
        pyautogui.locateAllOnScreen(image_path, confidence=confidence, region=(top, left, width, height), timeout=timeout)
    except ImageNotFoundException as e:
        raise e

# TODO: Implement clicker functions, waitforall images, clickImage, etc


#---Internal Functions---#

def _determineRegion(region : list[int] = None, search_rectangle : SearchRectangle = None) -> list[int]:
    '''
    Determines the region to search for the image.
    '''

    # Check if a region is provided
    if region != None:
        # Validate the given points provided
        _validateRegion(region)
        # Assign individual values from the region list
        top = region[0]
        left = region[1]
        width = region[2]
        height = region[3]
    # Check if a SearchRectangle is provided
    elif search_rectangle != None:
        top = search_rectangle.x
        left = search_rectangle.y
        width = search_rectangle.width
        height = search_rectangle.height
    # If neither are provided, search the entire screen
    else:
        top = 0
        left = 0
        width, height = pyautogui.size()

    return [top, left, width, height]

def _validateRegion(self, region : list[int]):
        '''
        Checks if the region provided is valid on the screen.
        '''

        # Check if the SR is off the screen
        if region[0] < 0 or region[1] < 0:
            raise ImageNotFoundException("The region is off the screen.")
        elif region[2] == 0 or region[3] == 0:
            raise ImageNotFoundException("The region has a negative/zero width or height.")
        elif region[0] + region[2] > pyautogui.size()[0] or region[1] + region[3] > pyautogui.size()[1]:
            raise ImageNotFoundException("The region exceeds the screen.")