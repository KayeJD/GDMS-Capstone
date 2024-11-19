# -*- coding: utf-8 -*-

import names


def start_and_prepare_application():
    """Start the application and prepare the dialog for adding a new contact."""
    startApplication("addressbook")
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "New"))
    activateItem(waitForObjectItem(names.address_Book_Unnamed_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.address_Book_Unnamed_Edit_QMenu, "Add..."))
    sendEvent("QMoveEvent", waitForObject(names.address_Book_Add_Dialog), 286, 186, 148, 100)


def fill_contact_form(first_name, last_name, email, phone):
    """Fill the contact form with given details."""
    type(waitForObject(names.forename_LineEdit), first_name)
    mouseClick(waitForObject(names.surname_LineEdit), 39, 4, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.surname_LineEdit), last_name)
    mouseClick(waitForObject(names.email_LineEdit), 17, 14, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.email_LineEdit), email)
    mouseClick(waitForObject(names.phone_LineEdit), 22, 2, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.phone_LineEdit), phone)


def validate_phone_and_email(phone, email):
    """Validate the phone number and email format."""
    # Phone validation: must be exactly 10 digits and numeric
    if not phone.isdigit() or len(phone) != 10:
        test.fail(f"Phone validation failed. Provided phone: '{phone}' (must be 10 digits)")
        return False

    # Email validation: must contain '@' symbol in the correct format
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        test.fail(f"Email validation failed. Provided email: '{email}' (must contain '@')")
        return False

    return True


def submit_contact_form():
    """Submit the contact form."""
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))


def verify_submission(expected_result, phone, email):
    """Verify the result of the submission based on validations."""
    # Validate phone and email before checking for submission success
    if not validate_phone_and_email(phone, email):
        test.fail("Validation failed for phone or email.")
        return

    if expected_result == "fail":
        try:
            error_message = waitForObject(names.error_dialog)
            test.compare(error_message.visible, True, "Error dialog should be visible.")
        except LookupError:
            test.fail("Expected an error dialog, but none was found.")
    else:
        test.vp("VP1")


def test_with_valid_data():
    """Test case with valid phone and email."""
    start_and_prepare_application()
    fill_contact_form("Ritvik", "Warrier", "ritvikw@xyz.com", "1234567890")
    submit_contact_form()
    verify_submission("pass", "1234567890", "ritvikw@xyz.com")


def test_with_invalid_phone_and_email():
    """Test case with invalid phone and/or email."""
    start_and_prepare_application()
    fill_contact_form("Ritvik", "Warrier", "invalidemail.com", "1234AB5678") 
    submit_contact_form()
    verify_submission("fail", "1234AB5678", "invalidemail.com")


def main():
    """Main function to execute the tests."""
    test_with_valid_data()
    test_with_invalid_phone_and_email()


if __name__ == "__main__":
    main()
