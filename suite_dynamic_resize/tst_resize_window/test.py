# -*- coding: utf-8 -*-

import names


def main():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
    
    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 32, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 51, 5, Qt.LeftButton)
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
    mouseClick(waitForObject(names.scrollView_MultiEffect), 4, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_image_IconImage), 27, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_image_IconImage_2), 23, 24, Qt.LeftButton)
