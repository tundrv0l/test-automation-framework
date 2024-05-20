from search_rectangle import SearchRectangle
import time
import pyautogui


def main():

    print(pyautogui.size())

    rectangle1 = SearchRectangle([100, 100, 200, 200])
    print(rectangle1.isWithin([301, 150]))

if __name__ == '__main__':
    main()