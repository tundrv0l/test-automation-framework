from search_rectangle import SearchRectangle
import time
import pyautogui
from image_search import *
from text_reader import *


def main():

    region = locateImage(r'C:\Users\tundr\Workspaces\test-automation-framework\raddish\tests\resources\btn_Terminal.png')

    print(region)

    text = readText(region)
    print(text)
    

if __name__ == '__main__':
    main()