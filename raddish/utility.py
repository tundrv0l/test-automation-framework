'''----------------- 
# Author: Parker Clark
# Date: 6/22/2024
# Description: A file containing auxiliary functions for the library.
-----------------'''

#---Imports---#
import pyautogui
from pyautogui import ImageNotFoundException
from pyrect import Box
from search_rectangle import SearchRectangle

def _validateArea(self, region : list[int]):
        '''
        Checks if the search rectangle is valid on the screen.
        '''

        # Check if the SR is off the screen
        if region[0] < 0 or region[1] < 0:
            raise ImageNotFoundException("The region is off the screen.")
        elif region[2] == 0 or region[3] == 0:
            raise ImageNotFoundException("The region has a negative/zero width or height.")
        elif region[0] + region[2] > pyautogui.size()[0] or region[1] + region[3] > pyautogui.size()[1]:
            raise ImageNotFoundException("The region exceeds the screen.")
        
def _determineRegion(region : list[int] = None, search_rectangle : SearchRectangle = None) -> list[int]:
    '''
    Determines the region to search for the image.
    '''

    # Check if a region is provided
    if region != None:

        # If the region is a Box object, convert it to a list
        if type(region) == Box:
            region = [region.x, region.y, region.width, region.height]

        print(region)

        # Validate the given points provided
        _validateArea(region)
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



