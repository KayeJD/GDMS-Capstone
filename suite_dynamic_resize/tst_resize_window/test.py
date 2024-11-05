# -*- coding: utf-8 -*-

import names

def main():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnWarning = True

    # start up the gui
    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    snooze(1)
    
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 50, 9, Qt.LeftButton) # master room -> OFF
    snooze(1)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 45, 8, Qt.LeftButton) # living room -> ON
    snooze(1)
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
    snooze(1)
    
    # these should both return pass case
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch, True)  
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch_2, False) 
    
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 50, 9, Qt.LeftButton) # living room -> OFF
    snooze(1)
    mouseWheel(waitForObject(names.scrollView_background_Rectangle), 465, 156, 0, 135, Qt.NoModifier) 
    snooze(1)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 41, 10, Qt.LeftButton) # master room -> ON
    snooze(1)
    
    # CustomSwitch should return fail cases
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch, True) 
    verifyToggleSwitchState(names.scrollView_toggle_CustomSwitch_2, True)  

    snooze(1.9)
    closeWindow(names.thermostat_QQuickWindowQmlImpl)


def verifyToggleSwitchState(toggleSwitch, expectedState):
    """Verifies if the toggle switch is in the expected state (True for checked, False for unchecked)."""
    obj = waitForObject(toggleSwitch)
    currentState = obj.checked  
    
    if currentState != expectedState:
        test.fail("Toggle switch '{}' state is incorrect: expected {}, got {}".format(
            toggleSwitch, expectedState, currentState))
    else:
        test.log("Toggle switch '{}' state is correct: {}".format(toggleSwitch, currentState))