'''----------------- 
# Author: Parker Clark
# Date: 5/11/2024
# Description: A class for the 'SearchRectangle' object.
-----------------'''

#---Imports---#
import pyautogui
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
import threading

class SearchRectangle:

    def __init__(self, region : list[int]):
        '''
        Initialize the 'SearchRectangle' object.

        Parameters
        ----------
        region : list[int]
            A list of four integers that represent a region on the screen.
              The list should be in this format: [x, y, width, height]
        
        Returns
        -------
        None
        '''

        # Assign individual values from the region list
        self.x = region[0]
        self.y = region[1]
        self.width = region[2]
        self.height = region[3]

        self.drawSR()

    #TODO Implement the isWithin method, which will check if a given point is within the search rectangle.
    #TODO Add a way to verify that the SR is valid on the screen.
    #TODO Maybe draw a representation of where the SR is??
    #TODO Implement getters for width and height.


    
    def drawSR(self):
        '''
        Draw a representation of the search rectangle on the screen.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        '''

        #WIP