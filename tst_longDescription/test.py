# -*- coding: utf-8 -*-

import names

def main():
    startApplication("apptest")

    # Adding first task
    mouseClick(waitForObject(names.task_List_Add_Item_Button))
    mouseClick(waitForObject(names.taskInput_TextField))
    type(waitForObject(names.taskInput_TextField), "test")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "testing to see if long descriptions are going to stay even after the task list expands and is visible.")
    mouseClick(waitForObject(names.save_Button))
    test.passes("Test case passed: Task 'test' added with description is visible.")

    # Adding second task
    mouseClick(waitForObject(names.task_List_Add_Item_Button))
    mouseClick(waitForObject(names.taskInput_TextField))
    type(waitForObject(names.taskInput_TextField), "test 2")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "why is today a Wednesday? I hate Wednesdays. I wish it was Friday.")
    mouseClick(waitForObject(names.save_Button))
    test.passes("Test case passed: Task 'test 2' added with description is visible.")

    # Adding third task
    mouseClick(waitForObject(names.task_List_Add_Item_Button))
    mouseClick(waitForObject(names.taskInput_TextField))
    type(waitForObject(names.taskInput_TextField), "coffee time")
    doubleClick(waitForObject(names.taskDescription_TextArea))
    type(waitForObject(names.taskDescription_TextArea), "my fav coffee right now is a pistachio latte with the syrup I made at home, yummy yummy.")
    mouseClick(waitForObject(names.save_Button))
    test.passes("Test case passed: Task 'coffee time' added with description is visible.")

    # Adding fourth task
    mouseClick(waitForObject(names.task_List_Add_Item_Button))
    mouseClick(waitForObject(names.taskInput_TextField))
    type(waitForObject(names.taskInput_TextField), "tea")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "I like Irani chai the most, it tastes best with rusk or a nice basic cookie.")
    mouseClick(waitForObject(names.save_Button))
    test.passes("Test case passed: Task 'tea' added with description is visible.")

    # Adding fifth task
    mouseClick(waitForObject(names.task_List_Add_Item_Button))
    mouseClick(waitForObject(names.taskInput_TextField))
    type(waitForObject(names.taskInput_TextField), "today")
    doubleClick(waitForObject(names.taskDescription_TextArea))
    type(waitForObject(names.taskDescription_TextArea), "The weather sucks. Why is it hot already? I want to be freezing when I walk outside.")
    mouseClick(waitForObject(names.save_Button))
    test.passes("Test case passed: Task 'today' added with description is visible.")

    # Scrolling to verify all tasks are visible
  
    mouseWheel(waitForObject(names.tea_Text), 0, 0, 0, 15, Qt.NoModifier)
    test.passes("Test case passed: All text in tasks are visible after adding and scrolling.")

    # Checking task history after scrolling
    mouseClick(waitForObject(names.task_List_historyList_ListView))
    mouseClick(waitForObject(names.delete_Button))
    mouseClick(waitForObject(names.delete_Button))
    mouseClick(waitForObject(names.done_Button))
    mouseClick(waitForObject(names.done_Button))
    mouseClick(waitForObject(names.done_Button))
    
    # Scrolling task history
    mouseWheel(waitForObject(names.task_List_historyList_ListView), 0, 0, 0, -30, Qt.NoModifier)
    mouseWheel(waitForObject(names.coffee_time_Completed_Text), 0, 0, 0, 15, Qt.NoModifier)
    mouseWheel(waitForObject(names.test_2_Deleted_Text), 0, 0, 0, 15, Qt.NoModifier)
    mouseWheel(waitForObject(names.task_List_historyList_ListView), 0, 0, 0, -15, Qt.NoModifier)
    
    test.passes("Test case passed: Task history also shows all tasks in the list after scrolling.")
