from search_rectangle import SearchRectangle
import time
import pyautogui


def main():

    print(pyautogui.size())

    rectangle1 = SearchRectangle(topLeftImage=r'C:\Users\pclark\Desktop\test-automation-framework\raddish\tests\resources\lbl_vscode.png', bottomRightImage=r'C:\Users\pclark\Desktop\test-automation-framework\raddish\tests\resources\lbl_dots.png')

if __name__ == '__main__':
    main()