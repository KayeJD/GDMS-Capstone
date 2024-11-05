# -*- coding: utf-8 -*-

import names

def testWelcome():
    test.compare(str(waitForObjectExists(names.toolBar_Rectangle_2).color.name), "#ffffff")
    test.compare(str(waitForObjectExists(names.scrollView_background_Rectangle_2).color.name), "#ffffff")
    test.compare(str(waitForObjectExists(names.scrollView_Master_Label).color.name), "#000000")
    test.compare(str(waitForObjectExists(names.background_Rectangle).color.name), "#effcf6")
    test.compare(str(waitForObjectExists(names.welcome_Label).color.name), "#000000")
    
def testWelcomeDark():
    test.compare(str(waitForObjectExists(names.background_Rectangle).color.name), "#000000")
    test.compare(str(waitForObjectExists(names.welcome_Label).color.name), "#ffffff")
    test.compare(str(waitForObjectExists(names.scrollView_14_Label).color.name), "#ffffff")
    
def testThermostatControl():
    test.compare(str(waitForObjectExists(names.background_Rectangle_2).color.name), "#effcf6")
    test.compare(str(waitForObjectExists(names.thermostat_Thermostat_Control_Label).color.name), "#000000")
    test.compare(str(waitForObjectExists(names.toolBar_Rectangle_2).color.name), "#ffffff")
    
def testThermostatControlDark():
    test.compare(str(waitForObjectExists(names.adjust_your_thermostat_settings_Label).color.name), "#d9d9d9")
    test.compare(str(waitForObjectExists(names.thermostat_Thermostat_Control_Label).color.name), "#ffffff")
    test.compare(str(waitForObjectExists(names.delegate_background_Rectangle).color.name), "#002125")
    
def testStats():
    test.compare(str(waitForObjectExists(names.background_Rectangle_3).color.name), "#effcf6")
    test.compare(str(waitForObjectExists(names.statistics_Label).color.name), "#000000")
    test.compare(str(waitForObjectExists(names.chart_DeclarativeChart).backgroundColor.name), "#ffffff")
    test.compare(str(waitForObjectExists(names.toolBar_Rectangle_2).color.name), "#ffffff")
    
def testStatsDark():
    test.compare(str(waitForObjectExists(names.chart_DeclarativeChart).backgroundColor.name), "#002125")
    test.compare(str(waitForObjectExists(names.background_Rectangle_3).color.name), "#000000")
    test.compare(str(waitForObjectExists(names.statistics_Label).color.name), "#ffffff")

def main():
    startApplication("ThermostatApp")

    testWelcome()

    mouseClick(waitForObject(names.thermostat_Thermostat_Control_Label))
    snooze(0.25)
    
    testThermostatControl()
    
    # mouseClick(waitForObject(names.thermostat_columnItem_ItemDelegate_2), 210, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.thermostat_columnItem_ItemDelegate_2))
    snooze(0.25)
    
    testStats()
    
    mouseClick(waitForObject(names.thermostat_Settings_Label))
    snooze(0.25)
    mouseClick(waitForObject(names.thermostat_Dark_Light_Label))
    snooze(0.25)
    mouseClick(waitForObject(names.thermostat_Rooms_Label))
    snooze(0.25)
    
    testWelcomeDark()
    
    mouseClick(waitForObject(names.thermostat_Thermostat_Control_Label))
    snooze(0.25)
    
    testThermostatControlDark()
    
    mouseClick(waitForObject(names.thermostat_Stats_Label))
    snooze(0.25)
    
    testStatsDark()
    
    mouseClick(waitForObject(names.thermostat_Settings_Label))
    snooze(0.25)
    mouseClick(waitForObject(names.thermostat_Dark_Light_Label))
    snooze(0.25)
    mouseClick(waitForObject(names.thermostat_Rooms_Label))
    snooze(0.25)
    
    testWelcome()
    
    mouseClick(waitForObject(names.thermostat_Thermostat_Control_Label))
    snooze(0.25)
    
    testThermostatControl()
    
    mouseClick(waitForObject(names.thermostat_Stats_Label))
    snooze(0.25)
    
    testStats()
