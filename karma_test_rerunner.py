"""
So the problem because i want to create this script is, that i don't found
any possibility to rerun frontend karma tests if they were successfully executed.
This application will automatically refresh the browser and rerun the tests if no error could be found on screen.
"""

import pyautogui, os
from PIL import Image
from collections import defaultdict
from time import sleep
import numpy as np

# =======================================
# temp screenshot file name
temFileName = 'test.png'
# rgb color to search for
# please use color picker on screenshot, not on real website
failed_red_rgb = (195, 51, 18) # rgb value can change
# =======================================

class Coordinate:
    BROWSER_IN_DOCK = (1202, 1055) # find browser picture on screen
    BROWSER_REFRESH_ICON = (87, 85) # refresh symbol in browser
    TEST_FAILED = (1915, 375) # pixel on screen != pixel on image

def move_cursor_to_coordinate(coordinate):
    """
    Moves the cursor position to the specified coordinates: tupel (x,y).
    """
    pyautogui.moveTo(coordinate[0], coordinate[1])

def compare_rgb_value(a, b):
    """
    Compare if two tupels contain the same values.
    """
    return a[0] == b[0] and a[1] == b[1] and a[2] == b[2]

def detect_color(rgb, filename):
    """
    Detects the specified rgb value within the pixels of an image.
    """
    img = Image.open(filename)
    img = img.convert('RGBA')
    data = img.getdata()

    for item in data:
        if item[0] == rgb[0] and item[1] == rgb[1] and item[2] == rgb[2]:
            return True
    return False
    
def find_coordinates_on_screen():
    """
    This method will not be used in the real script and is just to grab the
    coordinates of a pixel on the screen.
    Please do not use within an image because it will display the screen coordinates, not the image coordinates.
    """
    try:
        while True:
            x, y = pyautogui.position()
            position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(position_str, end='')
            print('\b' * len(position_str), end='', flush=True)
    except KeyboardInterrupt:
        print('\nDone.')

def print_error():
    """
    Print error text to console.
    """
    print('Error found')

def run_v1():
    """
    First version for rerunning karma tests used a cancel picture and if that can be found in a
    screenshot than there could be an error.
    """
    move_cursor_to_coordinate(Coordinate.BROWSER_IN_DOCK)
    pyautogui.click()
    sleep(1)

    while True:
        move_cursor_to_coordinate(Coordinate.BROWSER_REFRESH_ICON)
        pyautogui.click()
        sleep(3)
        pyautogui.screenshot(temFileName)
        location = pyautogui.locateOnScreen('failed.png')
        if location is not None:
            print_error()
            break
        os.remove(temFileName)

def run_v2():
    """
    Second version for rerunning karma tests checks if the specified pixel has a defined rgb value
    and if that's the case than there could be an error.
    """
    move_cursor_to_coordinate(Coordinate.BROWSER_IN_DOCK)
    pyautogui.click()
    sleep(1)

    while True:
        move_cursor_to_coordinate(Coordinate.BROWSER_REFRESH_ICON)
        pyautogui.click()
        sleep(2)

        pyautogui.screenshot(temFileName)
        im = Image.open(temFileName)
        rgb_im = im.convert('RGB')
        pixel_rgb = rgb_im.getpixel(Coordinate.TEST_FAILED)

        if compare_rgb_value(pixel_rgb, failed_red_rgb):
            print_error()
            break
        os.remove(temFileName)

def run_v3():
    """
    Third version for rerunning karma tests checks if any of the pixels in a screenshot
    has a defined rgb value and if that's the case than there could be an error.
    """
    move_cursor_to_coordinate(Coordinate.BROWSER_IN_DOCK)
    pyautogui.click()
    sleep(1)

    rerun_count = 0
    while True:
        rerun_count+=1
        move_cursor_to_coordinate(Coordinate.BROWSER_REFRESH_ICON)
        pyautogui.click()
        sleep(2)
        pyautogui.screenshot(temFileName)
        if detect_color(failed_red_rgb, temFileName):
            print_error()
            print(f'Karma tests rerunned: {rerun_count} times.')
            break
        os.remove(temFileName)

if __name__ == "__main__":
    run_v3()
