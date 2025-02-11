# -*- coding: utf-8 -*-

import names

def main():
    startApplication("apptest")
    
    # Add first task
    mouseClick(waitForObject(names.taskInput_TextField), 71, 21, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "testing")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "testing description, testing description, testing description testing description testing description testing description")
    mouseClick(waitForObject(names.save_Button), 43, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 152, 9, Qt.LeftButton)
    
    # Add second task
    mouseClick(waitForObject(names.taskInput_TextField), 61, 21, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "ice cream")
    mouseClick(waitForObject(names.o_Rectangle), 10, 9, Qt.LeftButton)
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "favorite flavor is talenti caramel cookie cream, or whatever the name is. It tastes good with the right amount of caramel and cookie")
    mouseClick(waitForObject(names.save_Button), 17, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 194, 8, Qt.LeftButton)
    
    # Add third task
    mouseClick(waitForObject(names.taskInput_TextField), 69, 18, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "coffee")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "I love pistachio lattes at the moment.I made pistachio syrup at home with pistachios, sugar and water and it came out well")
    mouseClick(waitForObject(names.save_Button), 35, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 178, 19, Qt.LeftButton)
    
    # Add fourth task
    mouseClick(waitForObject(names.taskInput_TextField), 121, 15, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "chai")
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "The real chai vs the American chai is always a dilemma. However, I enjoy both and they both taste yummy regarless")
    mouseClick(waitForObject(names.save_Button), 48, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.task_List_Add_Item_Button), 196, 13, Qt.LeftButton)
    
    # Add fifth task
    mouseClick(waitForObject(names.taskInput_TextField), 52, 4, Qt.LeftButton)
    type(waitForObject(names.taskInput_TextField), "tres leches")
    mouseClick(waitForObject(names.o_Flickable), 61, 36, Qt.LeftButton)
    doubleClick(waitForObject(names.enter_task_description_PlaceholderText))
    type(waitForObject(names.taskDescription_TextArea), "Tres leches cake is amazing! I love it so much, especially with fruits on top, been craving it")
    mouseClick(waitForObject(names.save_Button), 30, 13, Qt.LeftButton)
    
    # Verify all items are visible before scrolling
    test.passes("Task 'testing' is visible", object.exists(names.testing_Text))
    test.passes("Task 'ice cream' is visible", object.exists(names.ice_cream_Text))
    test.passes("Task 'coffee' is visible", object.exists(names.coffee_Text))
    test.passes("Task 'chai' is visible", object.exists(names.chai_Text))
    test.passes("Task 'tres leches' is visible", object.exists(names.tres_leches_Text))
    
    # Scroll list
    mouseWheel(waitForObject(names.listView_Rectangle_4), 181, 74, 0, -30, Qt.NoModifier)
    mouseWheel(waitForObject(names.listView_Rectangle_4), 181, 74, 0, 15, Qt.NoModifier)
    
    # Verify items remain visible after scrolling
    test.passes("Task 'testing' is still visible after scrolling", object.exists(names.testing_Text))
    test.passes("Task 'ice cream' is still visible after scrolling", object.exists(names.ice_cream_Text))
    test.passes("Task 'coffee' is still visible after scrolling", object.exists(names.coffee_Text))
    test.passes("Task 'chai' is still visible after scrolling", object.exists(names.chai_Text))
    test.passes("Task 'tres leches' is still visible after scrolling", object.exists(names.tres_leches_Text))
