# embark-automation

### Status: **pre-launch**

## Overview
The embark-automation package is a testing suite intended to work in tandem with the Embark Dev Team by utilizing the Selenium family of webdrivers. This package is meant to excel at integration testing and multi-platform testing.

## Setup
To start, we'll need to write the thing first!

## How to write tests

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
`get([your-url])` will load a webpage.
`find()`, `click()` and `fill()` each take an element as input and respectively:
`find([your-element])` return the element if it is present,
`click([your-element])` sends a click to the element if it is present
`fill([your-element], "[some-string]")` and send key strokes to an element if it is present.
They all will return `None` after a time delay if nothing is found. (default `time=30`)

With just these commands you can pretty effectively simulate a user navigating through a web page.

One thing you may be wondering is how `find`, `click`, and `fill` take "elements". 
Luckily, this is also neatly packaged in the test suite. 
Each element on a webpage can be uniquely identified by a **CSS Selector**. 
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
If that's the case, you'll have to make a new **CSS Selector** in the `pages/elements.py` file.
You can find easy instructions on how to do that (here)[./embark-testing-suite.md#elements]