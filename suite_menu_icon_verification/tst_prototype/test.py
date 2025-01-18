# -*- coding: utf-8 -*-

''' Notes:
    - test.ImagePresent() to to test ocr for icons/images.  Ref: https://doc.qt.io/squish/squish-api.html#findimage-function
    - ParameterMap -> {'param' : 'value', ...}
    - ParameterMap for test,imagePresent is:
    occurrence, interval, timeout, tolerant, threshold, multiscale, minScale, maxScale, message
    
    TODO:
    - Changing interface and create test case for interaction/change upon application state
    - expected icon test logging?? (verbose exporting)
'''

import names

def verifyMenuIcon(icon_name):
    test.imagePresent(f'{icon_name}', {'tolerant': True, 
                                       'multiscale': True, 
                                       'threshold': 99.5})


def main():
    startApplication("appsampleApp")
    # setWindowState(waitForObject(names.mainWindow_MainWindow), WindowState.Maximize)
    
    verifyMenuIcon("alert")
    verifyMenuIcon("notif_off_icon")

    sendEvent("QCloseEvent", waitForObject(names.mainWindow_MainWindow))
