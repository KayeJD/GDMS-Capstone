# encoding: UTF-8

from objectmaphelper import *

# names.py

# Main application window
MAIN_WINDOW = ":ThermostatApp_MainWindow"

# Room elements
LIVING_ROOM_TEMP = f"{MAIN_WINDOW}.LivingRoom.temp"
LIVING_ROOM_TOGGLE = f"{MAIN_WINDOW}.LivingRoom.toggle"

KITCHEN_TEMP = f"{MAIN_WINDOW}.Kitchen.temp"
KITCHEN_TOGGLE = f"{MAIN_WINDOW}.Kitchen.toggle"

MASTER_TEMP = f"{MAIN_WINDOW}.Master.temp"
MASTER_TOGGLE = f"{MAIN_WINDOW}.Master.toggle"

KID_ROOM_TEMP = f"{MAIN_WINDOW}.KidRoom.temp"
KID_ROOM_TOGGLE = f"{MAIN_WINDOW}.KidRoom.toggle"

KID_ROOM2_TEMP = f"{MAIN_WINDOW}.KidRoom2.temp"
KID_ROOM2_TOGGLE = f"{MAIN_WINDOW}.KidRoom2.toggle"

BEDROOM_TEMP = f"{MAIN_WINDOW}.Bedroom.temp"
BEDROOM_TOGGLE = f"{MAIN_WINDOW}.Bedroom.toggle"

# Add more rooms if necessary
thermostat_QQuickWindowQmlImpl = {"title": "Thermostat", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
thermostat_MultiEffect = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 20, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_ThermostatView = {"container": thermostat_QQuickWindowQmlImpl, "type": "ThermostatView", "unnamed": 1, "visible": True}
delegate_ThermostatScrollView = {"container": thermostat_ThermostatView, "id": "delegate", "type": "ThermostatScrollView", "unnamed": 1, "visible": True}
delegate_image_IconImage = {"container": delegate_ThermostatScrollView, "objectName": "image", "source": "qrc:/qt/qml/content/images/power.svg", "type": "IconImage", "visible": True}
delegate_handleItem_Rectangle = {"container": delegate_ThermostatScrollView, "id": "handleItem", "type": "Rectangle", "unnamed": 1, "visible": True}
o_CustomComboBox = {"container": thermostat_ThermostatView, "type": "CustomComboBox", "unnamed": 1, "visible": True}
thermostat_Overlay = {"container": thermostat_QQuickWindowQmlImpl, "type": "Overlay", "unnamed": 1, "visible": True}
comboBoxItem_ItemDelegate = {"checkable": False, "container": thermostat_Overlay, "id": "comboBoxItem", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
comboBoxItem_ItemDelegate_2 = {"checkable": False, "container": thermostat_Overlay, "id": "comboBoxItem", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
delegate_Power_CustomRoundButton = {"checkable": True, "container": delegate_ThermostatScrollView, "id": "powerButton", "text": "Power", "type": "CustomRoundButton", "unnamed": 1, "visible": True}
thermostat_RoomsView = {"container": thermostat_QQuickWindowQmlImpl, "type": "RoomsView", "unnamed": 1, "visible": True}
scrollView_RoomsScrollView = {"container": thermostat_RoomsView, "id": "scrollView", "type": "RoomsScrollView", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle = {"container": scrollView_RoomsScrollView, "id": "circle", "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "type": "CustomSwitch", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch_2 = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "occurrence": 2, "type": "CustomSwitch", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle_2 = {"container": scrollView_RoomsScrollView, "id": "circle", "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle_3 = {"container": scrollView_RoomsScrollView, "id": "circle", "occurrence": 3, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch_3 = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "occurrence": 4, "type": "CustomSwitch", "unnamed": 1, "visible": True}
scrollView_Kid_Room_Label = {"container": scrollView_RoomsScrollView, "text": "Kid Room", "type": "Label", "unnamed": 1, "visible": True}
delegate_background_Rectangle = {"container": delegate_ThermostatScrollView, "id": "background", "occurrence": 12, "type": "Rectangle", "unnamed": 1, "visible": True}
delegate_Kid_Room_Label = {"container": delegate_ThermostatScrollView, "text": "Kid Room", "type": "Label", "unnamed": 1, "visible": True}
thermostat_toolBar_ToolBar = {"container": thermostat_QQuickWindowQmlImpl, "id": "toolBar", "type": "ToolBar", "unnamed": 1, "visible": True}
toolBar_Rectangle = {"color": "#ffffff", "container": thermostat_toolBar_ToolBar, "type": "Rectangle", "unnamed": 1, "visible": True}
thermostat_MultiEffect_2 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 6, "type": "MultiEffect", "unnamed": 1, "visible": True}
