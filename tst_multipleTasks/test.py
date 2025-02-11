# -*- coding: utf-8 -*-

import names

def main():
    startApplication("apptest")
    
    # Add first task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 225, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 106, 7, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "task 1")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "task 1 oh this is the description hahaha")
    mouseClick(waitForObject(names.save_Button), 45, 13, Qt.LeftButton)
    test.passes("Test case passed: Task 1 text and description visible in list")
    
    # Add second task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 124, 22, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 73, 20, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "task 2")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "hi")
    mouseClick(waitForObject(names.save_Button), 38, 13, Qt.LeftButton)
    test.passes("Test case passed: Task 2 text and description visible in list")
    
    # Add third task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 158, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 97, 18, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "checking ")
    doubleClick(waitForObject(names.taskDescription_TextArea), 106, 4, Qt.LeftButton)
    type(waitForObject(names.taskDescription_TextArea), "checking checking")
    mouseClick(waitForObject(names.save_Button), 47, 8, Qt.LeftButton)
    test.passes("Test case passed: Task 3 text and description visible in list")
    
    # Add fourth task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 211, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 145, 12, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "hello")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "to say hi")
    mouseClick(waitForObject(names.save_Button), 45, 11, Qt.LeftButton)
    test.passes("Test case passed: Task 4 text and description visible in list")
    
    # Add fifth task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 162, 10, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 90, 6, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "brew coffee")
    mouseClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "make new coffee")
    mouseClick(waitForObject(names.save_Button), 34, 12, Qt.LeftButton)
    test.passes("Test case passed: Task 5 text and description visible in list")
    
    # Add sixth task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 165, 3, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 89, 8, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "make breakfast")
    mouseClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "yummy yummy")
    mouseClick(waitForObject(names.save_Button), 29, 12, Qt.LeftButton)
    test.passes("Test case passed: Task 6 text and description visible in list")
    
    # Add seventh task
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 179, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.taskInput_TextField), 101, 14, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "tea time")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "sip sip")
    mouseClick(waitForObject(names.save_Button), 50, 13, Qt.LeftButton)
    test.passes("Test case passed: Task 7 text and description visible in list")
    
    # Scroll through list to ensure all items are visible
    mouseWheel(waitForObject(names.listView_Rectangle_2), 252, 58, 0, 15, Qt.NoModifier)
    test.passes("Test case passed: Scroll passed - all items are visible in list after scroll")
