'''----------------- 
# Author: Parker Clark
# Date: 5/11/2024
# Description: A class for the 'SearchRectangle' object.
-----------------'''

#---Imports---#
import tkinter as tk
from multiprocessing import Process, Event
import pyautogui
from pyautogui import ImageNotFoundException

class SearchRectangle:

    def __init__(self, region : list[int] = None, topLeftImage : str = None, bottomRightImage : str = None, draw : bool = False, timeout : int = 2500):
        '''
        Initialize the 'SearchRectangle' object.

        Parameters
        ----------
        region : list[int]
            A list of four integers that represent a region on the screen.
              The list should be in this format: [x, y, width, height]
        
        Members
        -------
        x : int
            The x-coordinate of the region.
        
        y : int
            The y-coordinate of the region.

        width : int
            The width of the region.
        
        height : int
            The height of the region.
        
        process : Process
            Holds the drawing process of the SR.
        
        draw : bool
            A flag to determine if the SR should be drawn on the screen.

        draw_complete : Event
            An event to determine if the SR has finished drawing, used so
                the program can wait for the SR to finish drawing before continuing.

        timeout : int (Default = 2500)
            The amount of time the SR will be drawn on the screen in milliseconds.
        '''

        # Check if the region is provided
        if region != None:

            # Validate the given points provided
            self._validateSR(region)

            # Assign individual values from the region list
            self.x = region[0]
            self.y = region[1]
            self.width = region[2]
            self.height = region[3]
        
        # Check if the images are provided
        elif topLeftImage != None and bottomRightImage != None:
            # Find the top left and bottom right coordinates of the search rectangle
            try:
                topLeft = pyautogui.locateOnScreen(topLeftImage, confidence=0.9)
                bottomRight = pyautogui.locateOnScreen(bottomRightImage, confidence=0.9)
            except ImageNotFoundException:
                raise InvalidSR("The images provided could not be found on the screen.")
            
            # Assign the values of the search rectangle
            self.x = topLeft[0]
            self.y = topLeft[1]
            self.width = bottomRight[0] + bottomRight[2] - topLeft[0]
            self.height = bottomRight[1] + bottomRight[3] - topLeft[1]
        
        else:
            raise InvalidSR("No region or images were provided to create the search rectangle.")

        # Start a new process to draw the search rectangle
        self.process = None
        self.draw_complete = Event()

        # Draw the search rectangle if the flag is set
        if draw:
            self.drawSR(timeout=timeout)
            self._waitForDraw() 
    
    def drawSR(self, timeout : int = 2500):
        '''
        Draw a representation of the search rectangle on the screen by
         creating a semi-transparent red window that will disappear after a
         given amount of time. Uses multiprocessing to run multiple drawings in the
         background.

        Parameters
        ----------
        timeout : int (Default = 2500)
            The amount of time the SR will be displayed on the screen in milliseconds.
        
        Returns
        -------
        None
        '''

        # Terminate the process if its already running
        if self.process != None:
            self.process.terminate()
            self.process.join()

        # Begin a new process to draw the SR
        self.process = Process(target=self._drawSR, args=(timeout,))
        self.process.start()

    def isWithin(self, point : list[int]) -> bool:
        '''
        Check if a given point is within the search rectangle.

        Parameters
        ----------
        point : list[int]
            A list of two integers that represent a point on the screen.
              The list should be in this format: [x, y]
        
        Returns
        -------
        bool
            True if the point is within the search rectangle, False otherwise.
        '''

        # Check if the point is within the SR
        if self.x <= point[0] <= self.x + self.width and self.y <= point[1] <= self.y + self.height:
            return True
        else:
            return False


    #---Internal Methods---#
    def _drawSR(self, timeout : int):
        '''
        Internal method to actually draw the search rectangle on the screen.
        '''
        # Desginate a timer to show the SR.
        window = tk.Tk()
        window.overrideredirect(True)
        window.attributes('-topmost', True)
        window.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        window.attributes('-alpha', 0.1)
        window.configure(bg='red')

        # Create a Canvas widget with a red border
        canvas = tk.Canvas(window, width=self.width, height=self.height, bd=0, highlightthickness=2, highlightbackground="red")
        canvas.pack()

        window.after(timeout, window.destroy)

        window.mainloop()

        self.draw_complete.set()

    def _validateSR(self, region : list[int]):
        '''
        Checks if the search rectangle is valid on the screen.
        '''

        # Check if the SR is off the screen
        if region[0] < 0 or region[1] < 0:
            raise InvalidSR("The search rectangle is off the screen.")
        elif region[2] == 0 or region[3] == 0:
            raise InvalidSR("The search rectangle has a negative/zero width or height.")
        elif region[0] + region[2] > pyautogui.size()[0] or region[1] + region[3] > pyautogui.size()[1]:
            raise InvalidSR("The search rectangle exceeds the screen.")
        
    def _waitForDraw(self):
        '''
        Wait for the search rectangle to finish drawing.
        '''
        self.draw_complete.wait()
        


#---Exceptions---#
class InvalidSR(RuntimeError):
    '''
    An exception to be raised when a search rectangle is invalid.
     This could be due to the SR being off the screen or having a 
     negative width or height.
    '''
    
    def __init__(self, message : str):
        '''
        Initialize the 'InvalidSR' exception.

        Parameters
        ----------
        message : str
            The message to be displayed when the exception is raised.
        '''
        super().__init__(message)