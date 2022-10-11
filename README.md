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

`self` contains several useful objects and methods

 * `session` 
 * `urls`
 * `elements`
 * `validate_text()`
 * `validate_text_contains()`
 * `validate_url()`
 * `validate_url_contains()`
