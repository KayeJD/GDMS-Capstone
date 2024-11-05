# encoding: UTF-8

from objectmaphelper import *

thermostat_QQuickWindowQmlImpl = {"title": "Thermostat", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
thermostat_MultiEffect = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 21, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_MultiEffect_2 = {"container": thermostat_QQuickWindowQmlImpl, "occurrence": 6, "type": "MultiEffect", "unnamed": 1, "visible": True}
thermostat_StatisticsView = {"container": thermostat_QQuickWindowQmlImpl, "type": "StatisticsView", "unnamed": 1, "visible": True}
o_StatisticsScrollView = {"container": thermostat_StatisticsView, "type": "StatisticsScrollView", "unnamed": 1, "visible": True}
chart_DeclarativeChart = {"container": o_StatisticsScrollView, "id": "chart", "type": "DeclarativeChart", "unnamed": 1, "visible": True}
contentItem_Rectangle = {"container": o_StatisticsScrollView, "id": "contentItem", "type": "Rectangle", "unnamed": 1, "visible": True}
background_Rectangle = {"container": thermostat_StatisticsView, "id": "background", "occurrence": 6, "type": "Rectangle", "unnamed": 1, "visible": True}
o_Flickable = {"container": o_StatisticsScrollView, "type": "Flickable", "unnamed": 1, "visible": True}
thermostat_toolBar_ToolBar = {"container": thermostat_QQuickWindowQmlImpl, "id": "toolBar", "type": "ToolBar", "unnamed": 1, "visible": True}
toolBar_Rectangle = {"color": "#ffffff", "container": thermostat_toolBar_ToolBar, "type": "Rectangle", "unnamed": 1, "visible": True}
