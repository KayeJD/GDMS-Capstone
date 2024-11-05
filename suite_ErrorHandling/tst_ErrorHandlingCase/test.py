# -*- coding: utf-8 -*-
#Error handling case ensures all windows are still working when the windows are resized
import names
from squish import *

def main():
    test.log("Starting the Thermostat Resize Handling Test...")
    test_thermostat_resize_handling()

def test_thermostat_resize_handling():
    try:
        # Step 1: Start the application
        startApplication("ThermostatApp")
        test.log("Thermostat application started.")

        # Step 2: Define rooms and verify their elements
        rooms = ["LivingRoom", "Master", "Kitchen", "Kid Room", "Kid Room2", "Bedroom"]
        verify_room_elements(rooms)

        # Step 3: Resize window
        resize_application_window()

        # Re-verify visibility after resizing
        verify_room_elements(rooms, resized=True)

    except Exception as e:
        test.fail(f"Test failed due to error: {str(e)}")

def verify_room_elements(rooms, resized=False):
    for room in rooms:
        try:
            temp_display = waitForObject(f":ThermostatApp_MainWindow.{room}.temp")
            toggle_switch = waitForObject(f":ThermostatApp_MainWindow.{room}.toggle")

            # Verify that temperature display and toggle switch are visible
            assert temp_display.visible, f"{room} temperature display should {'still be' if resized else 'be'} visible."
            assert toggle_switch.visible, f"{room} toggle switch should {'still be' if resized else 'be'} visible."

            test.log(f"{room}: Temperature display and toggle switch verified as visible.")

        except LookupError:
            test.fail(f"Elements for {room} not found. Please check object paths.")
        except AssertionError as e:
            test.fail(str(e))

def resize_application_window():
    main_window = waitForObject(":ThermostatApp_MainWindow")
    main_window.resize(300, 400)  # Resize to smaller dimensions
    test.log("Resized application window.")

if __name__ == "__main__":
    main()






