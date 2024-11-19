# encoding: UTF-8

from objectmaphelper import *

thermostat_QQuickWindowQmlImpl = {"title": "Thermostat", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
thermostat_RoomsView = {"container": thermostat_QQuickWindowQmlImpl, "type": "RoomsView", "unnamed": 1, "visible": True}
scrollView_RoomsScrollView = {"container": thermostat_RoomsView, "id": "scrollView", "type": "RoomsScrollView", "unnamed": 1, "visible": True}
scrollView_Flickable = {"container": scrollView_RoomsScrollView, "type": "Flickable", "unnamed": 1, "visible": True}
scrollView_background_Rectangle = {"container": scrollView_RoomsScrollView, "id": "background", "occurrence": 3, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_background_Rectangle_2 = {"container": scrollView_RoomsScrollView, "id": "background", "occurrence": 5, "type": "Rectangle", "unnamed": 1, "visible": True}
scrollView_oC_Label = {"container": scrollView_RoomsScrollView, "occurrence": 3, "text": "oC", "type": "Label", "unnamed": 1, "visible": True}
scrollView_MultiEffect = {"container": scrollView_RoomsScrollView, "occurrence": 10, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_toolBar_ToolBar = {"container": thermostat_QQuickWindowQmlImpl, "id": "toolBar", "type": "ToolBar", "unnamed": 1, "visible": True}
toolBar_Rectangle = {"color": "#ffffff", "container": thermostat_toolBar_ToolBar, "type": "Rectangle", "unnamed": 1, "visible": True}
thermostat_MultiEffect = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 20, "type": "MultiEffect", "unnamed": 1, "visible": True}
scrollView_oC_Label_2 = {"container": scrollView_RoomsScrollView, "text": "oC", "type": "Label", "unnamed": 1, "visible": True}
scrollView_toggle_CustomSwitch = {"checkable": True, "container": scrollView_RoomsScrollView, "id": "toggle", "type": "CustomSwitch", "unnamed": 1, "visible": True}
thermostat_MultiEffect_2 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 6, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_columnItem_ItemDelegate = {"checkable": False, "container": thermostat_QQuickWindowQmlImpl, "id": "columnItem", "type": "ItemDelegate", "unnamed": 1, "visible": True}
thermostat_MultiEffect_3 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 7, "type": "MultiEffect", "unnamed": 1, "visible": True}
welcome_Label = {"container": thermostat_RoomsView, "text": "Welcome", "type": "Label", "unnamed": 1, "visible": True}
scrollView_Living_Room_Label = {"container": scrollView_RoomsScrollView, "text": "Living Room", "type": "Label", "unnamed": 1, "visible": True}
here_s_the_list_of_your_Rooms_at_Home_Label = {"container": thermostat_RoomsView, "text": "Here's the list of your Rooms at Home", "type": "Label", "unnamed": 1, "visible": True}
scrollView_24_Label = {"container": scrollView_RoomsScrollView, "text": 24, "type": "Label", "unnamed": 1, "visible": True}
