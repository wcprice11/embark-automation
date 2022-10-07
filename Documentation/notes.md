Browser Testing should take higher precedence than Simulated App Testing
Simulated App Testing should take higher precedence than Physical Device Testing

#### **Mobile Test Paradigm**
Pyramid of testing
            Last and least  real devices, real conditions
        Supporting that,    real devices, controlled use
    Supporting those,       Simulated Devices
And Most importantly,          Web tests

Web tests should primarily test systems and responsive designs
Simulated devices are best focused on user flow and visuals (**touch interactions**)
Real devices are where visual validation and usability is best done.
Real devices is where things get messy incoming calls, background apps, native apis

Docker version is important 

Docker is good, but it needs to be able to see the USB port
[enable USB](https://youtu.be/jE4oSetvzfQ?t=449)

This guy also teaches how to connect over wifi instead of USB for physical devices

If we do go with farmed testing (pretty much the only option for mass ios tests), we'll have plenty of options. 
AWS         - $250/deviceMonth
LambdaTest  - $125/deviceMonth
Perfecto    - $125/deviceMonth

Xcode9+ supports parallel iOS Tests. Both Real and Simulated

Emulators do little for production, they should be the quick regression test while developing

Use more than one device
Use more than one screen size or resolution
more than one OS version

document **everything** especially use cases

Stretch it. use messy caches, barely supported os versions. Make it suffer!

Connectivity communication. If the user starts offline or goes through a tunnel they should be informed why things aren't working. No crashes or silent dead loading

Check background usage. Memory leaks and battery drain won't be found if you are constantly resetting

#### class structure
* Session
    * Branch
    * User
    * Driver (selenium)
    * actions()
        * Load User
        * Reset User

* Branch
    * Pages : list/dict?
    * version : str
    * OS : enum ?

* Page
    * elements
    * url
    * actions()
        * title is
        * refresh

* element
    * actions()
        * click
        * is visible
        * fill
        * is present
    * Selector

* Selector (Good place for waits)

* User
    * ID
    * userName
    * password
    * actions()
        * reset


    
test_template(User, Branch) -> tests self methods (
    reset, 
    refresh
    correct version...)
    
    if clean:
    Load userData
    Launch emulation/physical routine
    smoke check

    {remaining test}
        
Save test to database: ID, date, OS, Branch, User, test_name, test_duration, test_description, photos...

### unittest
It looks like in order to be run from the command line. Tests must be packaged in modules or specified by path

sub-tests could be useful for checking if each element is present.

I would prefer a way to not hard-code the entire site layout. 
Instead, a database of each branch, page, element that could be updated would be much preferable. What I have should work, but in the future, a db would be better


### Embark test accounts
Go here: [new login](https://account.churchofjesuschrist.org/register)
Create your test account.
Make sure that the first or last name contains the text “test”. As a precaution, the request will only clone data onto a destination account that contains the text ’test” in the first or last name.

#### Copying user data to a test account:
In Postman, select “POST” from the dropdown
Enter request URL: `https://tall.global/userdata/clone/user`
Click the request “Body” tab
Paste the following into the text area
```json
{
    "sourceUser": {
        "type": "SRC",
        "userId": "YOUR_USER_ID_HERE"
    },
    "destUser": {
        "type": "DEST",
        "userId": "YOUR_USER_ID_HERE"
    },
    "courseId": 1,
    "createUser": false,
    "overrideUserCheck": false
}
```
Change the user ids to your values
Make sure the “raw” radio button is selected
The content encoding dropdown should be set to “JSON”
#### NOTES:
If “overrideUserCheck” is false, and the user does not have “test” in their first or last name, the correct response should be a 403 - Forbidden, otherwise a 200, and the SRC user’s data should be copied onto the DEST user’s name.
“createUser” defaults to false, only include it (and change it to true) if you are copying onto a non-existent user that you want to create (without creating an LDS account to go along with it). IT WILL OVERWRITE THE DEST USER’S NAME. In other words, if you created a test user with “test” in their name, and passed “createUser”: true.. the target user’s name will no long contain “test”.. and subsequent calls would fail. (This feature is more helpful in the testing that John does, which is why it is included. For everyday cloning needs, testers will probably only want to send a POST object that looks like this (using the defaults)).
Uninstall Embark on your device
Download Embark and log in to your test account

### Session
Since session is going to be the framework the tests are built on it should have easy methods to do so.
``` python
import elements as E

# Basic interaction
elem = session.find(E.sign-in)
elem.text()
elem.click()
elem.fill()

# alternate form
session.click(E.sign-in)
session.fill(E.user-name, self.user.get_pass())

# navigation
session.get()

# page info
session.get_url()
session.get_title()

# high level situations
session.simulate_sound()
session.screenshot()

# macros
session.login()
session.change_language()
```

No need to worry about clearing the browser cache. Each instance of the driver starts fresh.

# tech stack
Angular
ionic
 - native
 - storage
 - angular
ionicons
lodash
cordova
 - android
 - browser
 - ios
 - plugin
    - app-version
    - background-mode
    - device
    - dialogs
    - extended-device-information
    - file
    - globalization
    - inappbrowser
    - ionic
    - keyboard
    - ionic-webview
    - media
    - media-capture
    - nativeaudio
    - network-information
    - speechrecognition
    - splashscreen
    - statusbar
    - whitelist
 - sqlite-storage
dragula
rx-js
sw-toolbox
zone.js
ng-select
ajv
core-js
instabug-cordova
ng-circle-progress
ng2-pdf-viewer
ng2-dragula
ngx-logger
ngx-translate
videogular2
open-native-settings

# Direction
What needs to be implemented is as follows:
* Strong support for the Page Object Model.
* Test runner which can take in sessions and tests and run everything appropriately.

## Wednesday
- [ ] Reorganize to fit POM as close as possible.
    - []

However, there needs to be some visual sharing of results soon. Thus this will need to be broken down into more manageable tasks to get a MVP out ASAP.

# Road blocks

* Login and API handling of Users
* fragile tests due to ionic
* cross platform implementation.