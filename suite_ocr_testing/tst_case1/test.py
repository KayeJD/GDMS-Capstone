# -*- coding: utf-8 -*-

import names


def main():
    startApplication("ThermostatApp")
    mouseClick(waitForObject(names.welcome_Label))
    mouseWheel(waitForObject(names.scrollView_Living_Room_Label), 6, 19, 0, 3270, Qt.NoModifier)
    doubleClick(waitForObject(names.here_s_the_list_of_your_Rooms_at_Home_Label))
    mouseWheel(waitForObject(names.scrollView_24_Label), 8, 4, 0, 855, Qt.NoModifier)
    snooze(2.7)
    closeWindow(names.thermostat_QQuickWindowQmlImpl)
