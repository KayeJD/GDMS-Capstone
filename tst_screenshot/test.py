# -*- coding: utf-8 -*-

import names

def main():
    test.log("Hello World")

    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    mouseClick(waitForObject(names.thermostat_MultiEffect), 20, 4, Qt.LeftButton)
    mouseClick(waitForObject(names.thermostat_MultiEffect_2), 20, 15, Qt.LeftButton)
    mouseWheel(waitForObject(names.chart_DeclarativeChart), 512, 260, 0, 255, Qt.NoModifier)
    mouseDrag(waitForObject(names.contentItem_Rectangle), 0, 194, 25, -160, Qt.NoModifier, Qt.LeftButton)
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
