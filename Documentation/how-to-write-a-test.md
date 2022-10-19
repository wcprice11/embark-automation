This testing framework is specially built for embark. 
It runs using the unittest package and will take unittest tests, but for basic testing most of the base functionality is already included.

To start create a `.py` file in the tests folder. This file should start with "test..". 
Once you have the file you can start by creating a class that inherits from one of the pre-made test templates. 
You can find these in the `embark_tests.py` file. 
It should look something like this

```python
from tests.embark_tests import EmbarkDevTest

class TestingFeatureX(EmbarkDevTest):
    pass
```

The templates take care of some of the organization and give you helpful methods.

Next, inside this class add a method. Its name should also start with "test" and explain what the test will be checking. 
Make sure that it has access to `self`.

```python
from tests.embark_tests import EmbarkDevTest

class TestingFeatureX(EmbarkDevTest):
    def test_adding_phrases(self):
        pass
```

`self` contains several useful objects and methods that you can find [here](./Documentation/embark-testing-suite.md#embark_tests)

The four basic methods are `get()`, `find()`, `click()` and `fill()`.
* `get(your-url)` will load a webpage.
`find()`, `click()` and `fill()` each take an element as input and respectively:
* `find(your-element)` return the element if it is present,
* `click(your-element)` sends a click to the element if it is present
* `fill(your-element, some-string)` and send key strokes to an element if it is present.
They all will return `None` after a time delay if nothing is found. (default `time=30`)

One thing you may be wondering is how `find`, `click`, and `fill` take "elements". 
Luckily, this is also neatly packaged in the test suite. 
Each element on a webpage can be uniquely identified by a [**CSS Selector**](https://saucelabs.com/resources/articles/selenium-tips-css-selectors). 
You don't have to know what that is unless you are trying to make a new selection, but under the hood they are how each test can find the individual element it's looking for.
When your test needs to interact with an element, you can use the `elements` object to find it. 
This is loaded from each test template and can be accessed from self like this:

```python
from tests.embark_tests import EmbarkDevTest

class TestingFeatureX(EmbarkDevTest):
    def test_adding_phrases(self):
        self.elements
```

The elements object contains every web element that has been used in tests so far.
You can access any of them using dot notation.

```python
from tests.embark_tests import EmbarkDevTest

class TestingFeatureX(EmbarkDevTest):
    def test_adding_phrases(self):
        self.find(self.elements.WHATS_NEW_CARD_LEARN_MORE_BUTTON)
```

This gives the web driver everything it needs to do it's job.
You can than create a chain of actions however long you want to test anything you need.

You may run into the issue that the web element you want to use is not listed. 
If that's the case, you'll have to make a new [**CSS Selector**](https://saucelabs.com/resources/articles/selenium-tips-css-selectors) in the `pages/elements.py` file.
You can find easy instructions on how to do that (here)[./embark-testing-suite.md#elements]

There are several other useful ways to interact with the web page. They are all described in detail [here](/Documentation/embark-testing-suite.md#methods)

* `validate_text(string_to_test, expected_string)`: Confirms two strings exactly match and fails with a message if they do not.
* `validate_text_contains(string_to_test, expected_string)`: Confirms one string is found in another and fails with a message if they do not.
* `validate_url(expected_url)`: Confirms the current url and expected url exactly match and fails with a message if they do not.
* `validate_url_contains()`: Confirms the a string is found in the url and fails with a message if it does not.
* `get_element`: Returns the selenium webelement of the supplied object.
* `login(language)`: Macro to simplify the login process.