# -*- coding: utf-8 -*-
#from toplevelwindow import *
#from squish import *

import names

def main():  
    # Start ThermostatApp
    startApplication("ThermostatApp")
  
    # Maximize application window
    # Window must be 1920x1080
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    
    # Turn on all power buttons in Rooms tab
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_2), 16, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_3), 14, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_4), 16, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_5), 3, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle), 10, 9, Qt.LeftButton)
    
    # Navigate to ThermostatControl tab
    mouseClick(waitForObject(names.thermostat_Thermostat_Control_Label))
    
    # Check if all power buttons are on
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, True)
    mouseClick(waitForObject(names.o_CustomComboBox), 67, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 52, 19, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, True)
    mouseClick(waitForObject(names.o_CustomComboBox), 71, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 54, 18, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, True)
    mouseClick(waitForObject(names.o_CustomComboBox), 47, 24, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 38, 19, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, True)
    mouseClick(waitForObject(names.o_CustomComboBox), 50, 24, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 47, 17, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, True)
    mouseClick(waitForObject(names.o_CustomComboBox), 54, 26, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 33, 18, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, True)
    
    # Navigate to Rooms tab
    mouseClick(waitForObject(names.thermostat_Rooms_Label))
    
    # Turn off all power buttons in Rooms tab
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_2), 9, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_6), 11, 10, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_3), 10, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_4), 11, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_5), 9, 9, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle), 11, 8, Qt.LeftButton)
    
    # Navigate to ThermostatControl tab
    mouseClick(waitForObject(names.thermostat_Thermostat_Control_Label))
    
    # Check if all power buttons are off
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, False)
    mouseClick(waitForObject(names.o_CustomComboBox), 33, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 30, 17, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, False)
    mouseClick(waitForObject(names.o_CustomComboBox), 31, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 49, 23, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, False)
    mouseClick(waitForObject(names.o_CustomComboBox), 54, 20, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 47, 30, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, False)
    mouseClick(waitForObject(names.o_CustomComboBox), 80, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 39, 23, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, False)
    mouseClick(waitForObject(names.o_CustomComboBox), 68, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 46, 27, Qt.LeftButton)
    test.compare(waitForObjectExists(names.delegate_Power_CustomRoundButton).checked, False)
    