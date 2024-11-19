# GDMS-Capstone

## Customized test logs

The function compareWithLog compares an element with its expected and actual value, and returns a log message.
When failing a test, it returns a message stating that the element name, the expected value, and actual value. It also provides a traceback of where the error originated.

## Automated testing of element properties

The test process is split into functions which test different elements on the specific page. This is so that the actual test code just needs to navigate to the page in question, 
and then invoke the function which tests the page.

### Branch naming convention
- **t-#[ticketNumber]**: ticketNumber corresponds to Tiga backlog ticket number. 
- **testsuite_[lastName]**: individual branches for experimental test cases (experimental code)

