# -*- coding: utf-8 -*-

import names

def setUp():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnWarning = True
    testSettings.logScreenshotOnPass = True
    testSettings.reportFormat = "html"  # or "xml" for XML reports
    testSettings.reportDir = "/home/kadum"
    
def runTestRecording():
    startApplication("ThermostatApp")
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 38, 4, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_background_Rectangle), 465, 20, Qt.LeftButton)
    mouseClick(waitForObject(names.thermostat_MultiEffect_2), 14, 19, Qt.LeftButton)
    
    # Testing to see 'Thermostat Control' in page 2
    if test.ocrTextPresent("Thermostat Control"):
        test.log("Page 2 displays correct heading value")
    else:
        test.log("Page 2 displays incorrect heading value")
    
    closeWindow(names.thermostat_QQuickWindowQmlImpl)

def main():
    setUp()
    runTestRecording()
