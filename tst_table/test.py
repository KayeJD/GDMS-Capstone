def main():
    # Start the addressbook application
    startApplication("addressbook")

    # Add the first contact
    clickButton(waitForObject(":Address Book.New_QToolButton"))
    type(waitForObject(":Add a New Contact.Name_QLineEdit"), "John Doe")
    type(waitForObject(":Add a New Contact.Address_QTextEdit"), "123 Main Street\nAnytown")
    clickButton(waitForObject(":Add a New Contact.OK_QPushButton"))

    # Add the second contact
    clickButton(waitForObject(":Address Book.New_QToolButton"))
    type(waitForObject(":Add a New Contact.Name_QLineEdit"), "Jane Smith")
    type(waitForObject(":Add a New Contact.Address_QTextEdit"), "456 Elm Street\nOthertown")
    clickButton(waitForObject(":Add a New Contact.OK_QPushButton"))

    # Verify the contacts in the address book
    # Assuming the contacts are displayed in a QListWidget

    # Find the contact list widget
    contact_list = findObject(":Address Book.listWidget_QListWidget")

    # Collect the displayed contact names
    displayed_contacts = []
    for i in range(contact_list.count):
        item = contact_list.item(i)
        displayed_contacts.append(item.text())

    # Expected contacts
    expected_contacts = ["John Doe", "Jane Smith"]

    # Perform tabular verification
    if displayed_contacts == expected_contacts:
        test.passes("All contacts are correctly displayed.")
    else:
        test.fail("Contacts displayed do not match expected.\nExpected: {}\nActual: {}".format(expected_contacts, displayed_contacts))
        
        