# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 6, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 15, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 15, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 27, 7, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 25, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 25, 14, Qt.LeftButton)
    
    test.imagePresent("voicemail", {}, waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
    test.imagePresent("video_icon", {}, waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
