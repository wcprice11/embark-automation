### Selenium
: Open source webdriver software. Using this, a browser can simulate normal user interactions and return information about the page

### Selenium-Grid
: A server-client setup that allows for many simultaneous tests to be run at once
: can be local or remote

### Appium
: A port of Selenium focused on mobile app testing
: Supports touch gestures as well as the standard selenium tools
: Desktop app available


### Docker
: An easy tool to create many virtual machines locally or on a remote server.
: Particularly good and Android emulation

### Docker-Android
: available open-source android emulator
: only available for select phones
: Nexus 4 - 7, One
: Galaxy 6 - 7 as of 2019

### ADB (Android Debug Bridge)
: Command-line tool to control android devices over USB for physical testing

### smoke testing
: preliminary tests. Most basic functions. (check everything didn't explode)

### Monkey test
: pseudo-random stream of inputs. meant to stress test an app (actual android package)


## unittest

### unittest
: included python package supplying the testing architecture

### TestCase
: unittest's base class for a test case. 

unittest.TestCase can be extended as follows.
```python
class TestStringMethods(unittest.TestCase):
    # All tests must start with "test" to be run.
    def test_upper(self): 
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_upper(self):
        self.assertTrue('FOO'.is_upper())
        self.assertFalse('Foo'.is_upper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2) 
```

Included are three main methods for testing. Although, many more exist.
* `assertEqual(testedFunction, expectedValue)`
* `assertTrue(condition)`
* `assertFalse(condition)`

Also included are helper methods `setUp()` and `tearDown()` which are run before and after each test case

`unittest.main()` is a simple way to run all defined tests and display the results.

### test-fixture
: this is the setup necessary for one or more tests. Setting user, prepping webdriver etc.

### test-case
: basic unit of a test suite. Verifies given input-output pairs

### test-suite
: collection of test cases (or suites) to be run together.

### test-runner
: user interface for a test suite. anything from a gui app to just the command line results

## PyTest

### PyTest
: a python framework for creating and running tests. PyTest can consume unittest style tests. It also gives extended functionality, like parallel testing, through various plugins.

### continuous integration system
: A development pipeline of merging, unit tests, and integration tests before production. Generally, these will handle git merges, testing, and deployment automatically

### Angular
: Google-made Typescript app development framework 

### Angular components
: Building blocks of the framework. Contain templates and styles


### Ionic
: UI toolkit integrated with Angular

### Lodash
: JS Utility library

### Cordova
: A bridge that wraps the native device code in a JS API so that a webview application can use platform features.

### Page-Object Model
A webdriver design pattern encouraged by Selenium and used widely in the industry. 
It separates web element selectors and page-specific functions into "pages" that reduce code duplication and simplify test writing. 
Side-note: This is the idea behind this test harness architecture but is implemented rather loosely because nearly everything in embark is technically done on the same "page".