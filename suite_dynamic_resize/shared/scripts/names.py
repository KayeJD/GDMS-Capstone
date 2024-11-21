# encoding: UTF-8

from objectmaphelper import *

thermostat_QQuickWindowQmlImpl = {"title": "Thermostat", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
thermostat_RoomsView = {"container": thermostat_QQuickWindowQmlImpl, "type": "RoomsView", "unnamed": 1, "visible": True}
scrollView_RoomsScrollView = {"container": thermostat_RoomsView, "id": "scrollView", "type": "RoomsScrollView", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "type": "CustomSwitch", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch_2 = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "occurrence": 2, "type": "CustomSwitch", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle = {"container": scrollView_RoomsScrollView, "id": "circle", "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_circle_Rectangle_2 = {"container": scrollView_RoomsScrollView, "id": "circle", "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_MultiEffect = {"container": scrollView_RoomsScrollView, "occurrence": 2, "type": "MultiEffect", "unnamed": 1, "visible": True}
scrollView_image_IconImage = {"container": scrollView_RoomsScrollView, "objectName": "image", "source": "qrc:/qt/qml/content/images/Heat.svg", "type": "IconImage", "visible": True}
scrollView_image_IconImage_2 = {"container": scrollView_RoomsScrollView, "objectName": "image", "source": "qrc:/qt/qml/content/images/Auto.svg", "type": "IconImage", "visible": True}
thermostat_MultiEffect = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 19, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_MultiEffect_2 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 20, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_MultiEffect_3 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 6, "type": "MultiEffect", "unnamed": 1, "visible": True}
background_Rectangle = {"container": thermostat_RoomsView, "id": "background", "occurrence": 8, "type": "Rectangle", "unnamed": 1, "visible": True}
thermostat_bottomMenu_BottomBar = {"container": thermostat_QQuickWindowQmlImpl, "id": "bottomMenu", "type": "BottomBar", "unnamed": 1, "visible": True}
bottomMenu_image_IconImage = {"checkable": True, "container": thermostat_bottomMenu_BottomBar, "id": "menuItem", "occurrence": 2, "type": "TabButton", "unnamed": 1, "visible": True}
bottomMenu_image_IconImage_2 = {"container": thermostat_bottomMenu_BottomBar, "objectName": "image", "source": "qrc:/qt/qml/content/images/home.svg", "type": "IconImage", "visible": True}
scrollView_background_Rectangle = {"container": scrollView_RoomsScrollView, "id": "background", "type": "Rectangle", "unnamed": 1, "visible": True}
thermostat_columnItem_ItemDelegate = {"checkable": False, "container": thermostat_QQuickWindowQmlImpl, "id": "columnItem", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
thermostat_MultiEffect_4 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 7, "type": "MultiEffect", "unnamed": 1, "visible": True}
scrollView_background_Rectangle_2 = {"container": scrollView_RoomsScrollView, "id": "background", "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_Fan_RoomOption = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "roomOption", "text": "Fan", "type": "RoomOption", "unnamed": 1, "visible": True}
scrollView_Dry_RoomOption = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "roomOption", "text": "Dry", "type": "RoomOption", "unnamed": 1, "visible": True}
scrollView_Humidity_32_Label = {"container": scrollView_RoomsScrollView, "text": "Humidity: 32%", "type": "Label", "unnamed": 1, "visible": True}
scrollView_oC_Label = {"container": scrollView_RoomsScrollView, "text": "oC", "type": "Label", "unnamed": 1, "visible": True}
thermostat_ThermostatView = {"container": thermostat_QQuickWindowQmlImpl, "type": "ThermostatView", "unnamed": 1, "visible": True}
delegate_ThermostatScrollView = {"container": thermostat_ThermostatView, "id": "delegate", "type": "ThermostatScrollView", "unnamed": 1, "visible": True}
delegate_background_Rectangle = {"container": delegate_ThermostatScrollView, "id": "background", "occurrence": 12, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_Flickable = {"container": scrollView_RoomsScrollView, "type": "Flickable", "unnamed": 1, "visible": True}
scrollView_Master_Label = {"container": scrollView_RoomsScrollView, "text": "Master", "type": "Label", "unnamed": 1, "visible": True}
delegate_handleItem_Rectangle = {"container": delegate_ThermostatScrollView, "id": "handleItem", "type": "Rectangle", "unnamed": 1, "visible": True}
thermostat_columnItem_ItemDelegate_2 = {"checkable": False, "container": thermostat_QQuickWindowQmlImpl, "id": "columnItem", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
thermostat_StatisticsView = {"container": thermostat_QQuickWindowQmlImpl, "type": "StatisticsView", "unnamed": 1, "visible": True}
o_StatisticsScrollView = {"container": thermostat_StatisticsView, "type": "StatisticsScrollView", "unnamed": 1, "visible": True}
chart_DeclarativeChart = {"container": o_StatisticsScrollView, "id": "chart", "type": "DeclarativeChart", "unnamed": 1, "visible": True}
thermostat_MultiEffect_5 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 5, "type": "MultiEffect", "unnamed": 1, "visible": True}
delegate_background_Rectangle_2 = {"container": delegate_ThermostatScrollView, "id": "background", "occurrence": 4, "type": "Rectangle", "unnamed": 1, "visible": True}
delegate_15_Label = {"container": delegate_ThermostatScrollView, "text": 15, "type": "Label", "unnamed": 1, "visible": True}
background_Rectangle_2 = {"container": thermostat_ThermostatView, "id": "background", "occurrence": 18, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_24_Label = {"container": scrollView_RoomsScrollView, "text": 24, "type": "Label", "unnamed": 1, "visible": True}
thermostat_Control_Label = {"container": thermostat_ThermostatView, "text": "Thermostat Control", "type": "Label", "unnamed": 1, "visible": True}
