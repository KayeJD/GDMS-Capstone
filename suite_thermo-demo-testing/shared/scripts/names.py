# encoding: UTF-8

from objectmaphelper import *

thermostat_QQuickWindowQmlImpl = {"title": "Thermostat", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
thermostat_RoomsView = {"container": thermostat_QQuickWindowQmlImpl, "type": "RoomsView", "unnamed": 1, "visible": True}
scrollView_RoomsScrollView = {"container": thermostat_RoomsView, "id": "scrollView", "type": "RoomsScrollView", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle = {"container": scrollView_RoomsScrollView, "id": "circle", "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_background_Rectangle = {"container": scrollView_RoomsScrollView, "id": "background", "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
thermostat_MultiEffect = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 20, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_MultiEffect_2 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 8, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_MultiEffect_3 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 31, "type": "MultiEffect", "unnamed": 1, "visible": True}
kitchen_Label = {"container": thermostat_RoomsView, "index": 2, "text": "Kitchen", "type": "Label", "unnamed": 1, "visible": True}
kid_Room_Label = {"container": thermostat_RoomsView, "index": 3, "text": "Kid Room", "type": "Label", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "type": "CustomSwitch", "unnamed": 1, "visible": True}
thermostat_columnItem_ItemDelegate = {"checkable": False, "container": thermostat_QQuickWindowQmlImpl, "id": "columnItem", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
thermostat_MultiEffect_4 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 4, "type": "MultiEffect", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch_2 = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "occurrence": 2, "type": "CustomSwitch", "unnamed": 1, "visible": True}
thermostat_bottomMenu_BottomBar = {"container": thermostat_QQuickWindowQmlImpl, "id": "bottomMenu", "type": "BottomBar", "unnamed": 1, "visible": True}
bottomMenu_image_IconImage = {"container": thermostat_bottomMenu_BottomBar, "objectName": "image", "source": "qrc:/qt/qml/content/images/thermostat.svg", "type": "IconImage", "visible": True}
thermostat_ThermostatView = {"container": thermostat_QQuickWindowQmlImpl, "type": "ThermostatView", "unnamed": 1, "visible": True}
master_Label = {"container": thermostat_ThermostatView, "index": 1, "text": "Master", "type": "Label", "unnamed": 1, "visible": True}
kitchen_Label_2 = {"container": thermostat_ThermostatView, "index": 2, "text": "Kitchen", "type": "Label", "unnamed": 1, "visible": True}
living_Room_Label = {"container": thermostat_ThermostatView, "index": 0, "text": "Living Room", "type": "Label", "unnamed": 1, "visible": True}
bottomMenu_image_IconImage_2 = {"container": thermostat_bottomMenu_BottomBar, "objectName": "image", "source": "qrc:/qt/qml/content/images/home.svg", "type": "IconImage", "visible": True}
scrollView_Flickable = {"container": scrollView_RoomsScrollView, "type": "Flickable", "unnamed": 1, "visible": True}
thermostat_MultiEffect_5 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 21, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_MultiEffect_6 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 5, "type": "MultiEffect", "unnamed": 1, "visible": True}
delegate_ThermostatScrollView = {"container": thermostat_ThermostatView, "id": "delegate", "type": "ThermostatScrollView", "unnamed": 1, "visible": True}
delegate_background_Rectangle = {"container": delegate_ThermostatScrollView, "id": "background", "occurrence": 12, "type": "Rectangle", "unnamed": 1, "visible": True}
o_CustomComboBox = {"container": thermostat_ThermostatView, "type": "CustomComboBox", "unnamed": 1, "visible": True}
thermostat_Overlay = {"container": thermostat_QQuickWindowQmlImpl, "type": "Overlay", "unnamed": 1, "visible": True}
comboBoxItem_ItemDelegate = {"checkable": False, "container": thermostat_Overlay, "id": "comboBoxItem", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
comboBoxItem_ItemDelegate_2 = {"checkable": False, "container": thermostat_Overlay, "id": "comboBoxItem", "type": "ItemDelegate", "unnamed": 1, "visible": True}
thermostat_MultiEffect_7 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 6, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_columnItem_ItemDelegate_2 = {"checkable": False, "container": thermostat_QQuickWindowQmlImpl, "id": "columnItem", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle_2 = {"container": scrollView_RoomsScrollView, "id": "circle", "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
bottomMenu_menuItem_TabButton = {"checkable": True, "container": thermostat_bottomMenu_BottomBar, "id": "menuItem", "occurrence": 2, "type": "TabButton", "unnamed": 1, "visible": True}
bottomMenu_menuItem_TabButton_2 = {"checkable": True, "container": thermostat_bottomMenu_BottomBar, "id": "menuItem", "type": "TabButton", "unnamed": 1, "visible": True}
