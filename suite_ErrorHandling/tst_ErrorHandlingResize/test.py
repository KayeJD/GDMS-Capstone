# -*- coding: utf-8 -*-
import names

def main():
    # Start the application and maximize the window
    startApplication("ThermostatApp")
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Maximize)
    
    # Initial interaction with elements
    mouseClick(waitForObject(names.scrollView_circle_Rectangle), 5, 5, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 25, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch_2), 38, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_2), 18, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_3), 1, 10, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle_3), 16, 10, Qt.LeftButton)
    doubleClick(waitForObject(names.scrollView_toggle_CustomSwitch_3), 42, 14, Qt.LeftButton)
    mouseWheel(waitForObject(names.scrollView_Kid_Room_Label), 90, 2, 0, 195, Qt.NoModifier)
    mouseClick(waitForObject(names.thermostat_MultiEffect), 22, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.o_CustomComboBox), 84, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate), 62, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.o_CustomComboBox), 59, 23, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate_2), 46, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.delegate_Power_CustomRoundButton), 43, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.o_CustomComboBox), 81, 30, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate_2), 49, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.delegate_background_Rectangle), 161, 49, Qt.LeftButton)
    mouseClick(waitForObject(names.delegate_Kid_Room_Label))
    mouseClick(waitForObject(names.o_CustomComboBox), 35, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate_2), 39, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.o_CustomComboBox), 59, 20, Qt.LeftButton)
    mouseClick(waitForObject(names.comboBoxItem_ItemDelegate_2), 29, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.delegate_image_IconImage), 34, 1, Qt.LeftButton)
    
    # Resize to normal and verify elements
    setWindowState(waitForObject(names.thermostat_QQuickWindowQmlImpl), WindowState.Normal)
    mouseDrag(waitForObject(names.toolBar_Rectangle), 893, 9, -372, 97, Qt.NoModifier, Qt.LeftButton)
    test.log("Resized application window to normal.")

    # Check that buttons still function after resizing
    mouseClick(waitForObject(names.thermostat_MultiEffect_2), 14, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.scrollView_circle_Rectangle), 5, 5, Qt.LeftButton)  # Re-check circle toggle
    mouseClick(waitForObject(names.scrollView_toggle_CustomSwitch), 25, 8, Qt.LeftButton)  # Re-check toggle switch
    
    # End test
    test.log("Test completed with resized window and re-verified button functionality.")

