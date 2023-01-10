# Documentation
This is meant to be a guide to anyone new to the project. It's by no means complete yet but it's getting there!

## Embark Test Classes
This class covers a lot of the boiler plate testing code and gives several helper methods to make the tests that inherit from it simple and straightforward.
It's found [here](/tests/embark_test_classes.py)in the tests directory if you want to check the source code or make changes.

There are four (current) classes that can be inherited from. They are:
- VisualEmbarkProdTest
- EmbarkProdTest
- VisualEmbarkRCTest
- EmbarkRCTest

Each is used for testing on the specified branch and gives the appropriate urls and web elements.
The visual classes are only for developing and debugging. 
They are functionally identical, except they will use the graphical chrome interface and will create a chrome window that you can watch the test execute in.
The non-visual classes will execute "headless" and are preferred for production. 

Make sure to double check your classes before committing! :)

## Objects included in embark_test instances
Any test inherited from one of the `embark_test` classes will have the following objects to access:

- `branch`:
This is an organizational object to wrap the unique urls pages and elements of the individual branches. 
It is unpacked into the test object on initialization.

- `driver`:
`driver` is a selenium webdriver that is automatically downloaded for your system.
It is currently only set up to use chrome for our testing suite, but can run any webdriver for firefox, safari, or some more exotic uses like [Appium](/Documentation/definitions.md#Appium).
Many of the methods the test can use are actually wrappers of driver methods that can also be accessed directly e.g. `self.driver.get("https://www.google.com)`.

- `elements`:
This is an object that contains all the web elements in a given branch.
By using this to access elements, if a ui change is made only the element locator needs changed, and all tests that use it can remain unchanged.
It, like the `urls` object has all elements specific to the session, and can be accessed with dot notation.
```python
if(self.get_title() != "Embark")
    self.click(self.elements.SIGN_IN_BUTTON)
```
If you want to make changes or add new elements check out [this section](#elements). You'll probably do this a lot!

- `urls`:
The individual urls might change by branch, but Embark's url naming scheme remains consistent.
Because of this the exact url needed is pulled from the session but can be accessed by a standard name like `HOME_PAGE`.
These are accessed with dot notation. 
```python
if (self.urls.HOME_PAGE != self.get_url()):
    print(self.get_url())
```
If you need to update a url or add a new one, It can be done in the `pages/URLs.py` file.

- `user`:
This is the object where you can access login information like username or password. 
Most of this is handled in the [login macro](#methods) but can be accessed if you need it.
You can also use the [load_user()](FIX_ME) and [reset_user(FIX_ME)]() methods to change it.

## Methods in Embark Tests
All available methods, but not all are useful.
The useful ones are marked with a star (*).

### *`click()`
#### `click(element, time=30)`
Simulates a click to whatever element is passed in. 
This method will search for the given element for up to `time` seconds until it is found.
It defaults to 30 seconds before giving up.
If no element is found it will fail the test and give a message based on the element passed in.

### *`fill()`
#### `fill(element, text:str, time=30, enter=False)
Fill simulates key presses being sent to the element passed in.
It will first attempt to find the element for up to `time` seconds.
If found it will clear the contents and type in `text`.
If enter is set to `true` it will finish by simulating pushing the enter key.
If the element is not found it will fail the test and give an message based on the passed in element.

### *`find()`
#### `find(element, time=30)`
This method will search for the given element for up to `time` seconds until it is found.
It defaults to 30 seconds before giving up.
If no element is found it will fail the test and give a message based on the element passed in.

### *`get()`
#### get(url:str, tries=0):
This method navigates the webdriver to `url`.
It does attempt catch a specific set of 503 errors common when embark is updating.
It will reload the page up to five times if such errors are noticed.

### *`get_element()`
#### `get_element(element, time=30) -> web_element`
This method is similar to [`find()`](#find), except it returns the selenium web element.

### *`get_title()`
#### `get_title() -> str`
This function returns the title of the current webpage.

### *`get_url()`
#### `get_url() -> str`
This method returns the full url of the current webpage.

### `i_want_to_learn()`
#### `i_want_to_learn(language="spanish")`
This function is a macro to navigate the initial onboarding process.
It enters `language` in the drop down menu and selects the first result.
It then submits the form.

### `load_branch()`
#### `load_branch(branch)`
This will change the current session's branch variables to the new one.

### `load_driver()`
#### `load_driver(driver: Driver)`
Running this method changes the current session's webdriver.
It takes one of the `Driver` objects defined in [`driver.py`](/sessions/driver.py)

### `load_user()`
#### `load_user(user: User)`
Running this method changes the current session's webdriver.
It takes one of the `User` objects defined in [`embark_user.py`](/sessions/embark_user.py)

### *`login()`
#### `login(language=None, attempts=0)`
This is a very useful macro that goes through all the initial steps of logging into Embark.
It will first sign in with the loaded [`user`'s](#embark_user) credentials (attempting up to 4 times if the api is overloaded).
If language is not specified it will stop after confirming it is on the onboarding screen.
If language is specified it will fill out the form appropriately and submit.

### `logout()`
#### `logout()`
This macro assumes the setting menu button is visible, and clicks through to logout the user from embark.

### `quit()`
#### `quit()`
This method kills the webdriver (the webdriver has no permanent cache and restarting resets the cache as well)
This webdriver is ended as each test is closed, so is only necessary if you need close the browser in the middle of a test.

### *`reload()`
#### `reload()`
This method will refresh the current page

### `reset_user()`
#### `reset_user()`
This method resets the session's user to the user's base user via the embark api. 
See [embark user](#embark_user)

### *`save_screenshot()`
#### `save_screenshot(filename)`
This method will save a png screenshot of the current webdriver window (even while headless).
The specified `filename` should supply the path, name, and .png file extension. 
e.g. "~/embark-test/screenshots/my-screenshot.png"

### `setUp()`
#### `setUp()`
This is a method used by the unittest framework to be run before each test method in a given test class.

### `setUpVars()`
#### `setUpVars()`
This is a helper method called by `setUp()` to set up the sessions attributes correctly.

### `start()`
#### `start()`
This is a method to start the webdriver. It is automatically called by the default `setUp()` method.
It's only necessary in a test if the webdriver is quit and needs restarted.

### `tearDown()`
#### `tearDown()`
This is a method used by the unittest framework to be run after each test method in a given test class.

### `validate_element_text()`
#### `validate_element_text(element, truth:str, contains=False)`
This method searches for `element` on the current page. 
If it is found method will compare the text found in `element` against `truth` and fail the test if they are not identical.

### `validate_text()`
#### `validate_text(test:str, truth:str)`
This method compares the string `test` against `truth` and fails the test if they are not identical.

### `validate_text_absent()`
#### `validate_text_absent(test:str, truth:str)`
This method compares the string `test` against `truth` and fails the test if `test` is found in `truth`.

### validate_text_contains()
#### validate_text_contains(test:str, truth:str)
This method compares the string `test` against `truth` and fails the test if `test` is not found in `truth`.

### `validate_url()`
#### `validate_url(truth:str)`
This method compares the current page's url against `truth` and fails the test if it isn't identical.

### `validate_url_contains()`
#### `validate_url_contains(truth:str)`
This method compares the current page's url against `truth` and fails the test if `truth` isn't found in the url.

### **`wait_for_element_to_be_clickable()`
#### `wait_for_element_to_be_clickable(element, time=30)`
This method is a patient way to make sure a page has loaded. 
Since elements can be loaded in the html but still not clickable. This method will wait up to `time` until the `element` is fully visible and clickable before continuing. 

### `wait_for_text_in_element()`
#### `wait_for_text_in_element(element, text: str, time=30)`
This method is a patient way to make sure an element has updated.
This method will wait for up to `time` seconds until `text` is present in the passed element.

### `wait_for_text_in_url()`
#### `wait_for_text_in_url(text:str, time=30)`
This method is a patient way to make sure the driver has made it to the correct page.
This method will wait for up to `time` seconds until `text` is present in the current url.

### _click(self, element, time=30):

### _fill(self, element, text: str, time=30, enter=False):

### _find(self, element, time=30):

### _wait_for_element_to_be_clickable(self, element, time=30):

### _reload(self):

### _wait_for_one_of_two(self, element_a, element_b, time=30):

### _wait_for_text_in_element(self, element, text: str, time=30):

### _wait_for_text_in_url(self, text: str, time=30):

## pages
Most web testing frameworks use the Page-Object Model. 
This testing suite does too, but is only tackling a single website so it may be a little different in a few areas.
Currently the `pages` directory is used as an organization for the URLs and elements of individual branches

### elements
Each test contains an `elements` attribute that gives every element used in tests appropriate to the session.
These elements can be accessed using dot notation.
```python
self.elements.lesson_pass_off_button
```

These can then be passed to any function requiring an element to find.
```python
self.click(self.elements.lesson_pass_off_button)
```

## sessions
This directory contains most of the bones of the automation testing. 
All of the main functionality is implemented here. 
A session is meant to encapsulate the driver, user, and branch being used on a specific test.

### driver
this is the code for loading selenium with the correct driver with the correct options.

### embark_branch
This is an organizational class to group urls, pages, and elements

### embark_session
The `embark_session.py` file contains all of the session-centric methods added to each test class. These include most of the functionality of the test suite. Things like loading or changing users or several of the underlying selenium calls used in get, find, or click.

This is where some the most significant bugs can be fixed (or created) since it effects almost everything else.

### embark_user

The User is an attribute of the session.
You may want to write a test the very first introduction to embark to make sure all the guides are present.
To do this, you would want to login to an account with no progress.
Conversely, you may want to check that something happens when you pass a certain level.
To do this, you would want an account that has had a lot of work put in.

Choosing a user for your session lets you accomplish this.

See also [How to create a new user](/Documentation/how-to-create-a-new-user.md)

## Web Elements
`elements` refers to both Selenium web elements and selectors used to locate said elements. 
Elements are how this testing suite is able to find specific things on a given web page.

They can be located using several of the testing [methods](#methods) that take a locator found in the [elements attribute](#elements).
Once located they have several [built-in attributes](https://www.selenium.dev/documentation/webdriver/elements/information/) that can be accessed in your tests.

## CSS Selectors
The most robust way to find specific elements on a webpage in selenium is to leverage CSS selectors.
There is some information on how to use them here, but [this](https://saucelabs.com/resources/articles/selenium-tips-css-selectors) tutorial from SauceLabs will be more comprehensive.

See also: [How to use and create selectors](/Documentation/how-to-create-selectors.md)

