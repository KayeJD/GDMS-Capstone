# The purpose of this code is to test basic element values.
# This test is also a proof of concept for custom test log/fail messages.
import names
import traceback

# Custom compare function with error logging
def compareWithLog(actual, expected, element_name):
    try:
        if actual == expected:
            test.compare(actual, expected, "This test case passed!")
            test.log(f"Custom success message: {element_name} matches expected value.")
        else:
            raise AssertionError(f"ERROR: Color mismatch for {element_name}. Expected: {expected}, but got: {actual}")
    except AssertionError as e:
        # Log the traceback
        test.fail(f"{str(e)}\nTRACEBACK:\n{traceback.format_exc()}")

# Test welcome page light mode and dark mode
def testWelcome():
    compareWithLog(str(waitForObjectExists(names.toolBar_Rectangle_2).color.name), "#000000", "toolBar_Rectangle_2 in Light Mode") # should be #ffffff
    compareWithLog(str(waitForObjectExists(names.scrollView_background_Rectangle_2).color.name), "#ffffff", "scrollView_background_Rectangle_2 in Light Mode")
    compareWithLog(str(waitForObjectExists(names.scrollView_Master_Label).color.name), "#000000", "scrollView_Master_Label in Light Mode")
    compareWithLog(str(waitForObjectExists(names.background_Rectangle).color.name), "#effcf6", "background_Rectangle in Light Mode")
    compareWithLog(str(waitForObjectExists(names.welcome_Label).color.name), "#000000", "welcome_Label in Light Mode")
    
def testWelcomeDark():
    compareWithLog(str(waitForObjectExists(names.background_Rectangle).color.name), "#000000", "background_Rectangle in Dark Mode")
    compareWithLog(str(waitForObjectExists(names.welcome_Label).color.name), "#ffffff", "welcome_Label in Dark Mode")
    compareWithLog(str(waitForObjectExists(names.scrollView_14_Label).color.name), "#ffffff", "scrollView_14_Label in Dark Mode")
    
# Test thermostat control light mode and dark mode
def testThermostatControl():
    compareWithLog(str(waitForObjectExists(names.background_Rectangle_2).color.name), "#effcf6", "background_Rectangle_2 in Light Mode")
    compareWithLog(str(waitForObjectExists(names.thermostat_Thermostat_Control_Label).color.name), "#000000", "thermostat_Thermostat_Control_Label in Light Mode")
    compareWithLog(str(waitForObjectExists(names.toolBar_Rectangle_2).color.name), "#ffffff", "toolBar_Rectangle_2 in Light Mode")
    
def testThermostatControlDark():
    compareWithLog(str(waitForObjectExists(names.adjust_your_thermostat_settings_Label).color.name), "#d9d9d9", "adjust_your_thermostat_settings_Label in Dark Mode")
    compareWithLog(str(waitForObjectExists(names.thermostat_Thermostat_Control_Label).color.name), "#ffffff", "thermostat_Thermostat_Control_Label in Dark Mode")
    compareWithLog(str(waitForObjectExists(names.delegate_background_Rectangle).color.name), "#002125", "delegate_background_Rectangle in Dark Mode")
    
# Test stats page light mode and dark mode
def testStats():
    compareWithLog(str(waitForObjectExists(names.background_Rectangle_3).color.name), "#effcf6", "background_Rectangle_3 in Light Mode")
    compareWithLog(str(waitForObjectExists(names.statistics_Label).color.name), "#000000", "statistics_Label in Light Mode")
    compareWithLog(str(waitForObjectExists(names.chart_DeclarativeChart).backgroundColor.name), "#ffffff", "chart_DeclarativeChart in Light Mode")
    compareWithLog(str(waitForObjectExists(names.toolBar_Rectangle_2).color.name), "#ffffff", "toolBar_Rectangle_2 in Light Mode")
    
def testStatsDark():
    compareWithLog(str(waitForObjectExists(names.chart_DeclarativeChart).backgroundColor.name), "#002125", "chart_DeclarativeChart in Dark Mode")
    compareWithLog(str(waitForObjectExists(names.background_Rectangle_3).color.name), "#000000", "background_Rectangle_3 in Dark Mode")
    compareWithLog(str(waitForObjectExists(names.statistics_Label).color.name), "#ffffff", "statistics_Label in Dark Mode")

def main():
    startApplication("ThermostatApp")

    testWelcome()

    mouseClick(waitForObject(names.thermostat_Thermostat_Control_Label))
    snooze(0.25)
    
    testThermostatControl()
    
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
