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
