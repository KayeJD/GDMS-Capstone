# -*- coding: utf-8 -*-

# Test: Checking for Room toggle functionality after window resizing

import names
import os
import os.path
import sys


def setUp():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnWarning = True
    testSettings.logScreenshotOnPass = True
    testSettings.reportFormat = "html"  # or "xml" for XML reports
    # testSettings.reportDir = "/path/to/your/report/directory"


def verifyToggleSwitchState(toggleSwitch, expectedState):
    """Verifies if the toggle switch is in the expected state (True for checked, False for unchecked)."""
    obj = waitForObject(toggleSwitch)
    currentState = obj.checked  
    
    if currentState != expectedState:
        test.fail("Toggle switch '{}' state is incorrect: expected {}, got {}".format(
            toggleSwitch, expectedState, currentState))
        save_
    else:
        test.passes("Toggle switch '{}' state is correct: {}".format(toggleSwitch, currentState))
        
        
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
    runTestRecording()
    
    

    


        
        
        