# -*- coding: utf-8 -*-

import names

def main():
    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
    closeWindow(names.thermostat_QQuickWindowQmlImpl)
