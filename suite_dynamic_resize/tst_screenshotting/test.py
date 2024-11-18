import os.path
import sys

def main():
    # Register AUT with squishserver:
    aut = "addressbook"
    path = os.path.join(os.environ["SQUISH_PREFIX"], "examples", "qt", "addressbook")
    registerAUT(aut, path)

    startApplication("addressbook")
    save_screenshot({"type": "QMenuBar"}, "qmenubar.png")

def save_screenshot(obj_name, filename):
    widget = waitForObject(obj_name)
    img = object.grabScreenshot(widget)
    img.save(filename)
    testData.get(filename)

def registerAUT(aut, path, squishserver_host=None, squishserver_port=None):
    s = '"' + os.environ["SQUISH_PREFIX"] + '/bin/squishrunner"'
    if squishserver_host is not None:
        s += ' --host ' + squishserver_host
    if squishserver_port is not None:
        s += ' port=' + str(squishserver_port)
    s += ' --config addAUT "' + aut + '" "' + path + '"'
    if sys.platform == "win32" and s.endswith('"'):
        s = '"' + s
    test.log("Executing: " + s)
    os.system(s)



