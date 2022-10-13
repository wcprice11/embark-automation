# Documentation
This is meant to be a guide to anyone new to the project. It's by no means complete yet but it's getting there!

## embark_tests
This class covers a lot of the boiler plate testing code and gives several helper methods to make the tests inherited from it very simple straightforward.

### Objects
- `session`: 

 Session packages the different circumstances of the test, like the branch it's acting on, the user it's acting as, and the browser version it's using.
 Many of the methods the test can use are stored here.

- `urls`:

The individual urls might change by branch, but Embark's url naming scheme remains consistent.
Because of this the exact url needed is pulled from the session but can be accessed by a standard name like `HOME_PAGE`.
These are accessed with dot notation. 
```python
if (self.urls.HOME_PAGE != self.get_url()):
    print(self.get_url())
```
If you need to update a url or add a new one, It can be done in the `pages/URLs.py` file.

- `elements`

This is an object that contains all the web elements in a given branch.
By using this to access elements, if a ui change is made only the element locator needs changed, and all tests that use it can remain unchanged.
It, like the `urls` object has all elements specific to the session, and can be accessed with dot notation.
```python
if(self.get_title() != "Embark")
    self.click(self.elements.SIGN_IN_BUTTON)
```

#### Methods
- `validate_text()`
- `validate_text_contains()`
- `validate_url()`
- `validate_url_contains()`

## pages

### elements