# -*- coding: utf-8 -*-

import names


def main():
    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 46, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 54, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.thermostat_MultiEffect), 31, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.o_CustomComboBox), 47, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 64, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.thermostat_MultiEffect_7), 13, 18, Qt.LeftButton)
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
    setWindowSize(waitForObject(names.thermostat_QQuickWindowQmlImpl), 587, 618)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 34, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 38, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.bottomMenu_image_IconImage), 24, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.master_Label))
    mouseClick(waitForObject(names.bottomMenu_image_IconImage_2), 19, 4, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 33, 3, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle), 9, 6, Qt.LeftButton)
    setWindowSize(waitForObject(names.thermostat_QQuickWindowQmlImpl), 1128, 618)
    mouseClick(waitForObject(names.thermostat_MultiEffect_5), 24, 9, Qt.LeftButton)
    mouseClick(waitForObject(names.thermostat_MultiEffect_6), 17, 25, Qt.LeftButton)
    mouseClick(waitForObject(names.o_CustomComboBox), 65, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 37, 26, Qt.LeftButton)
