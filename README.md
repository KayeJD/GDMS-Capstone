# GDMS-Capstone

## Customized test logs

The function "compareWithLog" inside of test.py compares an element with its expected and actual value, and returns a log message.
When failing a test, it returns a message stating that the element name, the expected value, and actual value. It also provides a traceback of where the error originated.

## Automated testing of element properties

The test process is split into functions which test different elements on the specific page. This is so that the actual test code just needs to navigate to the page in question, 
and then invoke the function which tests the page.

## Environment Set-up Requirements

### OCR Testing

In order to utilize Squish's OCR functionality, tesseract needs to be installed and configured. See ocr_setup.md file for more details. 

## Dev Reminders

### Branch naming convention
- **TG-{ticketNumber}**: ticketNumber corresponds to Tiga backlog ticket number. 
- **testsuite_{lastName}**: individual branches for experimental test cases (experimental code)

### Commit message template
```
# Title: Summary, imperative, start upper case, don't end with a period
# No more than 50 chars. #### 50 chars is here:    #

TG-{###} {#ready, #closed, #etc.}
# Body: 'What' and 'Why', not 'How'. Add TG-{###} {#ready, #closed, #etc.}
# convention to reflect issue, task, user story or epic status on Taiga
# Wrap at 72 chars. ################################## which is here:    #

# At the end: Include Co-authored-by for all contributors. 
# Include at least one empty line before it. Format: 
# Co-authored-by: name <user@users.noreply.github.com>
```


### Taiga Integrations
#### Capabilities
- Change the status of an epic, user story, issue, or task in Taiga with the commit message: you may want to read more about this feature in the article "Changing elements status via commit message".
- Attach commits in an epic, user story, issue, or task of Taiga with the commit message: you may want to read more about this feature in the article "Attach commits to elements via commit message".
- Create issues on Taiga when they are created on GitHub.
- Add comments to the connected issues on Taiga when they are created on GitHub.

#### Cannot...
- Dual synchronization: currently the integration functionality only allows receiving messages from GitHub. Taiga can’t communicate with GitHub (the one-way communication is from Github to Taiga), so changes made in Taiga won’t be reflected in GitHub.
- Show commit links in Taiga issues: If you name a story, task or issue in a commit message (by its reference number) a link to commit won’t appear in Taiga.
- Sync current GitHub issues and comment when the integration module in Taiga is enabled: the integration only works with the future issues and comments added in GitHub.

