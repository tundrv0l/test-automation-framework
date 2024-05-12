# A test of pyautogui

import pyautogui
import os

def test():
    pyautogui.moveTo(100, 100, duration=1)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, 'resources', 'btn_search.png')
    foundImage = pyautogui.locateOnScreen(image_path, confidence = 0.9)
    print(foundImage)

    pyautogui.click(foundImage)















if __name__ == '__main__':
    test()