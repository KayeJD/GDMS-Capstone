# -*- coding: utf-8 -*-
import names


def main():
    startApplication("ThermostatApp")
    mouseClick(waitForObject(names.thermostat_Stats_Label))
    snooze(0.25)
   
    test.vp("VP1") # Test living room stats
   
    mouseClick(waitForObject(names.comboBox_CustomComboBox), 30, 21, Qt.LeftButton)
    snooze(0.25)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 48, 19, Qt.LeftButton)
    snooze(0.25)
   
    test.vp("VP2") # Test master stats
   
    mouseClick(waitForObject(names.comboBox_CustomComboBox), 60, 20, Qt.LeftButton)
    snooze(0.25)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate_2), 70, 19, Qt.LeftButton)
    snooze(0.25)
   
    test.vp("VP3") # Test kitchen stats