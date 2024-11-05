# -*- coding: utf-8 -*-

'''
    This test case is a compilation of all other concepts covered in the other .py tests within this directory
'''

import names
import os.path
import sys


def setUp():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnWarning = True
    testSettings.logScreenshotOnPass = True
    testSettings.reportFormat = "html"  # or "xml" for XML reports
    testSettings.reportDir = "/home/kadum"


def verifyToggleSwitchState(toggleSwitch, expectedState):
    """Verifies if the toggle switch is in the expected state (True for checked, False for unchecked)."""
    obj = waitForObject(toggleSwitch)
    currentState = obj.checked  
    
    if currentState != expectedState:
        test.fail("Toggle switch state is incorrect: expected {}, got {}".format(
            toggleSwitch, expectedState, currentState))
        save_screenshot("toggle_CustomSwitch.png")
    else:
                test.passes("Toggle switch state is correct: {}", str(currentState))
        
        
def runTestRecording():
    # start up the gui
    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    snooze(0.5)
    
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 50, 9, Qt.LeftButton) # master room -> OFF
    snooze(0.5)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 45, 8, Qt.LeftButton) # living room -> ON
    snooze(0.5)
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
    snooze(0.5)
    
    # these should both return pass case
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch, True)  
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch_2, False) 
    
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 50, 9, Qt.LeftButton) # living room -> OFF
    snooze(0.5)
    mouseWheel(waitForObject(names.scrollView_background_Rectangle), 465, 156, 0, 135, Qt.NoModifier) 
    snooze(0.5)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 41, 10, Qt.LeftButton) # master room -> ON
    snooze(0.5)
    
    # CustomSwitch should return fail cases
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch, True) # NOTE: change to False to pass case
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch_2, True)  

    snooze(1)
    closeWindow(names.thermostat_QQuickWindowQmlImpl)


def main():
    setUp()
    
    # Register AUT with squishserver:
    aut = "ThermostatApp"
    path = os.path.join('/home/kadum/Qt/Examples/Qt-6.7.3/demos/thermostat/build/Desktop_Qt_6_7_3-Debug')
    registerAUT(aut, path)
    
    runTestRecording()
    

# TODO: THIS NEEDS TO BE REFACTORED TO GENERALIZE
def save_screenshot(filename):
    widget = waitForObject(":scrollView_RoomsScrollView") 
    img = object.grabScreenshot(widget)
    

    screenshot_dir = '/home/kadum/screenshots'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    full_path = os.path.join(screenshot_dir, filename)
    img.save(full_path)
    testData.get(full_path)


def registerAUT(aut, path, squishserver_host=None, squishserver_port=None):
    s = '"' + os.environ["SQUISH_PREFIX"] + '/bin/squishrunner"'
    if squishserver_host is not None:
        s += ' --host ' + squishserver_host
    if squishserver_port is not None:
        s += ' port=' + str(squishserver_port)
    s += ' --config addAUT "' + aut + '" "' + path + '"'
    if sys.platform == "win32" and s.endswith('"'):
        s = '"' + s
    test.log("Executing: " + s)
    os.system(s)




    
    

    


        
        
        