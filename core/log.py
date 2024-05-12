'''----------------- 
# Author: Parker Clark
# Date: 5/11/2024
# Description: A class for the 'Log' static object.
-----------------'''

#---Imports---#
import logging


class Log:
    '''A class for the 'Log' static object.'''

    def __init__(self):
        '''
        Initialize the 'Log' object.
        '''

        self.logger = logging.getLogger(__name__)

        # Set a default log level
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler



    @staticmethod
    def write(message: str, log_type: str = 'LOG'):
        '''
        Write a general message to the console.

        TODO: Incorporate pass fail criteria.

        Parameters
        ----------
        message : str
            The message to write to the console.
        
        log_type : str (Optional)
            The type of message to write to the console, default is LOG

        '''
        print(f'[{log_type}] {message}')