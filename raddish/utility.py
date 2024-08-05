'''----------------- 
# Author: Parker Clark
# Date: 6/22/2024
# Description: A file containing auxiliary functions for the library.
-----------------'''

#---Imports---#
import pyautogui
from pyautogui import ImageNotFoundException
from pyscreeze import Box
from search_rectangle import SearchRectangle

def _validateArea(region : list[int]):
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
        if isinstance(region, Box):
            region = [region.left, region.top, region.width, region.height]

        # Validate the given points provided
        _validateArea(region)

        # Assign individual values from the region list
        return region
    
    # Check if a SearchRectangle is provided
    elif search_rectangle != None:

        return [search_rectangle.x, search_rectangle.y, search_rectangle.width, search_rectangle.height]
    
    # If neither are provided, search the entire screen
    else:
        
        # Get the screen size
        width, height = pyautogui.size()

        # Return the entire screen
        return [0, 0, width, height]



