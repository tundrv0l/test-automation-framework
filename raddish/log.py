'''----------------- 
# Author: Parker Clark
# Date: 5/11/2024
# Description: A class for the 'Log' object.
-----------------'''

#---Imports---#
import logging
import datetime

class Log:
    '''
    A custom logger that will generate messages during runtime to the terminal, and maintain a logfile.
    '''
    def __init__(self):
        '''
        Initialize the 'Log' object.
        '''
        # Create a current date time string
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

        # Create a custom logger
        self.logger = logging.getLogger(__name__)

        # Set the level of this logger
        self.logger.setLevel(logging.DEBUG)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(f'{timestamp}_runtime.log')
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('[%(levelname)s] %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)


    def write(self, message: str, log_type: str = 'INFO'):
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
        if log_type.upper() == 'DEBUG':
            self.logger.debug(message)
        elif log_type.upper() == 'INFO':
            self.logger.info(message)
        elif log_type.upper() == 'WARNING':
            self.logger.warning(message)
        elif log_type.upper() == 'ERROR':
            self.logger.error(message)
        else:
            self.logger.info(message)