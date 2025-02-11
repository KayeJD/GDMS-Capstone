# encoding: UTF-8

from objectmaphelper import *

task_List_QQuickApplicationWindow = {"title": "Task List", "type": "QQuickApplicationWindow", "unnamed": 1, "visible": True}
task_List_Add_Item_Button = {"checkable": False, "container": task_List_QQuickApplicationWindow, "text": "Add Item", "type": "Button", "unnamed": 1, "visible": True}
task_List_Overlay = {"container": task_List_QQuickApplicationWindow, "type": "Overlay", "unnamed": 1, "visible": True}
taskInput_TextField = {"container": task_List_Overlay, "echoMode": 0, "id": "taskInput", "type": "TextField", "unnamed": 1, "visible": True}
enter_task_description_PlaceholderText = {"container": task_List_Overlay, "text": "Enter task description", "type": "PlaceholderText", "unnamed": 1, "visible": True}
taskDescription_TextArea = {"container": task_List_Overlay, "id": "taskDescription", "type": "TextArea", "unnamed": 1, "visible": True}
save_Button = {"checkable": False, "container": task_List_Overlay, "text": "Save", "type": "Button", "unnamed": 1, "visible": True}
task_List_historyList_ListView = {"container": task_List_QQuickApplicationWindow, "id": "historyList", "type": "ListView", "unnamed": 1, "visible": True}
o_Rectangle = {"color": "#000000", "container": task_List_Overlay, "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
o_Rectangle_2 = {"color": "#000000", "container": task_List_Overlay, "type": "Rectangle", "unnamed": 1, "visible": True}
o_Flickable = {"container": task_List_Overlay, "type": "Flickable", "unnamed": 1, "visible": True}
task_List_listView_ListView = {"container": task_List_QQuickApplicationWindow, "id": "listView", "type": "ListView", "unnamed": 1, "visible": True}
listView_Rectangle = {"color": "#90ee90", "container": task_List_listView_ListView, "index": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
listView_Rectangle_2 = {"color": "#90ee90", "container": task_List_listView_ListView, "index": 4, "type": "Rectangle", "unnamed": 1, "visible": True}
task_4_Text = {"container": listView_Rectangle_2, "text": "task 4", "type": "Text", "unnamed": 1, "visible": True}
checking_Text = {"container": listView_Rectangle, "text": "checking ", "type": "Text", "unnamed": 1, "visible": True}
listView_Rectangle_3 = {"color": "#90ee90", "container": task_List_listView_ListView, "index": 1, "type": "Rectangle", "unnamed": 1, "visible": True}
why_is_today_a_wednesday_i_hate_wednesdays_i_wish_it_was_friday_Text = {"container": listView_Rectangle_3, "text": "why is today a wednesday i hate wednesdays i wish it was friday", "type": "Text", "unnamed": 1, "visible": True}
listView_Rectangle_4 = {"color": "#90ee90", "container": task_List_listView_ListView, "index": 3, "type": "Rectangle", "unnamed": 1, "visible": True}
tea_Text = {"container": listView_Rectangle_4, "text": "tea", "type": "Text", "unnamed": 1, "visible": True}
listView_Rectangle_5 = {"color": "#90ee90", "container": task_List_listView_ListView, "index": 0, "type": "Rectangle", "unnamed": 1, "visible": True}
delete_Button = {"checkable": False, "container": listView_Rectangle_5, "text": "Delete", "type": "Button", "unnamed": 1, "visible": True}
done_Button = {"checkable": False, "container": listView_Rectangle_5, "text": "Done", "type": "Button", "unnamed": 1, "visible": True}
historyList_Column = {"container": task_List_historyList_ListView, "index": 2, "type": "Column", "unnamed": 1, "visible": True}
coffee_time_Completed_Text = {"container": historyList_Column, "text": "coffee time (Completed)", "type": "Text", "unnamed": 1, "visible": True}
historyList_Column_2 = {"container": task_List_historyList_ListView, "index": 1, "type": "Column", "unnamed": 1, "visible": True}
test_2_Deleted_Text = {"container": historyList_Column_2, "text": "test 2 (Deleted)", "type": "Text", "unnamed": 1, "visible": True}
i_love_pistachio_lattes_at_the_moment_i_made_pistachio_syrup_at_home_with_pistachio_water_and_sugar_it_came_out_good_Text = {"container": listView_Rectangle, "text": "i love pistachio lattes at the moment. i made pistachio syrup at home with pistachio water and sugar it came out good", "type": "Text", "unnamed": 1, "visible": True}
