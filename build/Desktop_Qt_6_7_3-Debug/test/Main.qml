
/*
import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 700
    title: "Task List"

    ListModel { id: listModel }  // Active Tasks
    ListModel { id: historyModel }  // Completed/Deleted Tasks

    Column {
        anchors.fill: parent
        spacing: 10
        padding: 20

        Button {
            text: "Add Item"
            width: parent.width - 20
            onClicked: taskPopup.open()  // Open the popup
        }

        Text {
            text: "Tasks"
            font.bold: true
        }

        ListView {
            id: listView
            width: parent.width - 20
            height: 300
            model: listModel

            delegate: Rectangle {
                width: ListView.view.width
                height: textElement.implicitHeight + descriptionElement.implicitHeight + 30  // Adjust dynamically
                color: "light green"
                border.color: "black"
                border.width: 2
                radius: 5

                Column {
                    anchors.fill: parent
                    anchors.margins: 10
                    spacing: 5

                    Text {
                        id: textElement
                        text: model.name
                        font.pixelSize: 16
                        wrapMode: Text.WordWrap
                        elide: Text.ElideNone
                        width: parent.width
                    }

                    Text {
                        id: descriptionElement
                        text: model.description
                        font.pixelSize: 14
                        wrapMode: Text.WordWrap
                        elide: Text.ElideNone
                        color: "gray"
                        width: parent.width
                    }

                    Row {
                        spacing: 10

                        Button {
                            text: "Done"
                            width: 60
                            onClicked: {
                                historyModel.append({ "name": model.name, "description": model.description, "status": "Completed" })
                                listModel.remove(index)
                            }
                        }

                        Button {
                            text: "Delete"
                            width: 80
                            onClicked: {
                                historyModel.append({ "name": model.name, "description": model.description, "status": "Deleted" })
                                listModel.remove(index)
                            }
                        }
                    }
                }
            }
        }

        Text {
            text: "Task History"
            font.bold: true
        }

        ListView {
            id: historyList
            width: parent.width - 20
            height: 200
            model: historyModel

            delegate: Column {
                width: parent.width
                height: textElement.implicitHeight + descriptionElement.implicitHeight + 20
                spacing: 5

                Text {
                    id: textElement
                    text: model.name + " (" + model.status + ")"
                    font.bold: true
                }

                Text {
                    id: descriptionElement
                    text: model.description
                    wrapMode: Text.WordWrap
                    width: parent.width
                    color: "gray"
                }
            }
        }
    }

    // Popup for adding tasks
    Popup {
        id: taskPopup
        width: 300
        height: 250
        modal: true
        focus: true
        anchors.centerIn: parent
        background: Rectangle {
            color: "white"
            radius: 10
            border.color: "green"
        }

        Column {
            spacing: 10
            anchors.fill: parent
            anchors.margins: 20

            Text {
                text: "Enter Task:"
                font.bold: true
            }

            TextField {
                id: taskInput
                width: parent.width
                placeholderText: "Enter task name"
            }

            Text {
                text: "Description:"
                font.bold: true
            }

            TextArea {
                id: taskDescription
                width: parent.width
                placeholderText: "Enter task description"
                wrapMode: TextEdit.WordWrap
            }

            Row {
                spacing: 10
                width: parent.width

                Button {
                    text: "Cancel"
                    onClicked: {
                        taskInput.text = ""
                        taskDescription.text = ""
                        taskPopup.close()
                    }
                }

                Button {
                    text: "Save"
                    onClicked: {
                        if (taskInput.text.trim() !== "") {
                            if (listModel.count < 100) {
                                listModel.append({ "name": taskInput.text, "description": taskDescription.text })
                                taskInput.text = ""
                                taskDescription.text = ""
                                taskPopup.close()
                            } else {
                                console.log("Task Limit Reached")
                            }
                        }
                    }
                }
            }
        }
    }
}
*/


import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 700
    title: "Task List"

    ListModel { id: listModel }
    ListModel { id: historyModel }

    Column {
        anchors.fill: parent
        spacing: 10
        padding: 20

        Button {
            text: "Add Item"
            width: parent.width - 20
            onClicked: taskPopup.open()
        }

        Text {
            text: "Tasks"
            font.bold: true
        }

        ListView {
            id: listView
            width: parent.width - 20
            height: 300
            model: listModel

            delegate: Rectangle {
                width: ListView.view.width
                height: textElement.implicitHeight + descriptionElement.implicitHeight + 30
                color: "light green"
                border.color: "black"
                border.width: 2
                radius: 5

                Column {
                    anchors.fill: parent
                    anchors.margins: 10
                    spacing: 5

                    Text {
                        id: textElement
                        text: model.name
                        font.pixelSize: 16
                        wrapMode: Text.WordWrap
                        elide: Text.ElideNone
                        width: parent.width
                    }

                    Text {
                        id: descriptionElement
                        text: model.description
                        font.pixelSize: 14
                        wrapMode: Text.WordWrap
                        elide: Text.ElideNone
                        color: "gray"
                        width: parent.width
                    }

                    Row {
                        spacing: 10

                        Button {
                            text: "Done"
                            width: 60
                            onClicked: {
                                historyModel.append({ "name": model.name, "description": model.description, "status": "Completed" })
                                listModel.remove(index)
                            }
                        }

                        Button {
                            text: "Delete"
                            width: 80
                            onClicked: {
                                historyModel.append({ "name": model.name, "description": model.description, "status": "Deleted" })
                                listModel.remove(index)
                            }
                        }
                    }
                }
            }
        }

        Text {
            text: "Task History"
            font.bold: true
        }

        ListView {
            id: historyList
            width: parent.width - 20
            height: 150
            model: historyModel

            delegate: Column {
                width: parent.width
                height: textElement.implicitHeight + descriptionElement.implicitHeight + 20
                spacing: 5

                Text {
                    id: textElement
                    text: model.name + " (" + model.status + ")"
                    font.bold: true
                }

                Text {
                    id: descriptionElement
                    text: model.description
                    wrapMode: Text.WordWrap
                    width: parent.width
                    color: "gray"
                }
            }
        }

        Button {
            text: "Clear History"
            width: parent.width - 20
            onClicked: historyModel.clear()
            visible: historyModel.count > 0
        }
    }

    // Popup for adding tasks
    Popup {
        id: taskPopup
        width: 320
        height: 350
        modal: true
        focus: true
        anchors.centerIn: parent
        background: Rectangle {
            color: "white"
            radius: 10
            border.color: "green"
        }

        Column {
            spacing: 10
            anchors.fill: parent
            anchors.margins: 20

            Text {
                text: "Enter Task:"
                font.bold: true
            }

            TextField {
                id: taskInput
                width: parent.width
                placeholderText: "Enter task name"
            }

            Text {
                text: "Description:"
                font.bold: true
            }

            Flickable {
                width: parent.width
                height: 100  // Fixed height so text area doesn’t shrink
                contentHeight: taskDescription.implicitHeight
                clip: true

                TextArea {
                    id: taskDescription
                    width: parent.width
                    placeholderText: "Enter task description"
                    wrapMode: TextEdit.Wrap
                    focus: true
                }
            }

            Row {
                spacing: 10
                width: parent.width

                Button {
                    text: "Cancel"
                    onClicked: {
                        taskInput.text = ""
                        taskDescription.text = ""
                        taskPopup.close()
                    }
                }

                Button {
                    text: "Save"
                    onClicked: {
                        if (taskInput.text.trim() !== "") {
                            listModel.append({ "name": taskInput.text, "description": taskDescription.text })
                            taskInput.text = ""
                            taskDescription.text = ""
                            taskPopup.close()
                        }
                    }
                }
            }
        }
    }
}
