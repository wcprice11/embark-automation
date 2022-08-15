Selenium
: Open source webdriver software. Using this, a browser can simulate normal user interactions and return information about the page

Selenium-Grid
: A server-client setup that allows for many simultaneous tests to be run at once
: can be local or remote

Appium
: A port of Selenium focused on mobile app testing
: Supports touch gestures as well as the standard selenium tools
: Desktop app available


Docker
: An easy tool to create many virtual machines locally or on a remote server.
: Particularly good and Android emulation

Docker-Android
: available open-source android emulator
: only available for select phones
: Nexus 4 - 7, One
: Galaxy 6 - 7 as of 2019

ADB (Android Debug Bridge)
: Command-line tool to control android devices over USB for physical testing

smoke testing
: preliminary tests. Most basic functions. (check everything didn't explode)

Monkey test
: pseudo-random stream of inputs. meant to stress test an app (actual android package)


## unittest

unittest:
: included python package supplying the testing architecture

TestCase:
: unittest's base class for a test case. 

unittest.TestCase can be extended as follows.
```python
class TestStringMethods(unittest.TestCase):
    # All tests must start with "test" to be run.
    def test_upper(self): 
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

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

Also included are helper methods `setUp()` and `tearDown` which are run before and after each test case

`unittest.main()` is a simple way to run all defined tests and display the results.

test-fixture
: this is the setup necessary for one or more tests. Setting user, prepping webdriver etc.

test-case
: basic unit of a test suite. Verifies given input-output pairs

test-suite
: collection of test cases (or suites) to be run together.

test-runner
: user interface for a test suite. anything from a gui app to just the command line results



continuous integration system
: A development pipeline of merging, unit tests, and integration tests before production. Generally, these will handle git merges, testing, and deployment automatically