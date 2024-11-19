# -*- coding: utf-8 -*-

# This template 

import names


def main():
    startApplication("ThermostatApp")
    mouseClick(waitForObject(names.thermostat_MultiEffect), 15, 12, Qt.LeftButton)
    test.ocrTextPresent("Thermostat Control");
    mouseClick(waitForObject(names.thermostat_columnItem_ItemDelegate), 47, 32, Qt.LeftButton)
    snooze(3.1)
    closeWindow(names.thermostat_QQuickWindowQmlImpl)
