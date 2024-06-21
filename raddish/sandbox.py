from search_rectangle import SearchRectangle
import time
import pyautogui
from image_search import *


def main():

    rectangle1 = SearchRectangle(topLeftImage=r'C:\Users\pclark\Desktop\test-automation-framework\raddish\tests\resources\lbl_vscode.png', bottomRightImage=r'C:\Users\pclark\Desktop\test-automation-framework\raddish\tests\resources\lbl_dots.png', draw=False)

    clickImage(r'C:\Users\pclark\Desktop\test-automation-framework\raddish\tests\resources\lbl_dots.png', search_rectangle=rectangle1, timeout=5)
    

if __name__ == '__main__':
    main()