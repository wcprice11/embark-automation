# How to Create Selectors

## How to Create Selectors
Before we start one extremely useful tool is the [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo) chrome extension.
It can be used to test different selectors live on a website or generate working (if, on embark, incomprehensible) css selectors.
Once installed, it can be used by right clicking on a page and opening the inspect panel (⌘⌥ C on Mac or Ctl Shift c on windows)
Once the inspect panel is open, ChroPath can be found as the last tab under the Elements section.
![where to find ChroPath](/Documentation/images/open-chopath.png)
Test selectors can then be entered in the selector field.
![using ChroPath](/Documentation/images/use-chropath.png)


A CSS Selector is simply stored as a string. 
To select a certain type of html element, all you need is that element's html tag.
```python
# HTML <ion-card>some card</ion-card>
my_selector = "ion-card"
```

Several special characters are used to encode different attributes.

`#` proceeds ids.
```python
# <ion-card id=embark-card>
my_selector = "#embark-card"
```

`.` is used before classes.
```python
# <ion-card class=title>
my_selector = ".title"
```

All of these can then be used in tandem.
```python
# <ion-card class=title>
my_selector = "ion-card.title"
```

This is a great start, but unless you are lucky, these will usually select several elements.
Selenium will only function correctly if each of the locators are specific to the precise element you are trying to select.

To be more specific we can use relational locators.
The most simple relational locator is simply a space.
A space signifies that the second item is the child or sub-child of the first.

```python
# <body>
#   <ion-ribbon>
#       <ion-card class=title>
#   </ion-ribbon>
# </body>

my_selector = "body ion-card.title"
```

We can then be more specific with `>` to signify direct a child.
```python
# <body>
#   <ion-ribbon>
#       <ion-card class=title> I'm selected </ion-card>
#       <div>
#           <ion-card class=title> I'm not </ion-card>
#       </div>
#   </ion-ribbon>
# </body>

my_selector = "ion-ribbon>ion-card.title"
```

With these you should be able to select most things.
However, there are still more precise selectors such as `nth-of-type()` or selecting by attribute. 
For more details on these see the [tutorial]() mentioned above.

A couple last notes. If the element you are trying to find is inside a shadow root element, you may want to find a different element.
shadow root elements cause a lot of problems when searching.
Generally selecting the element above is the best you can expect without going deep in the weeds.
Also, be sure that you don't get multiple results when testing the page. 
Just because only one element is visible does not mean it is the only one loaded on the webpage.
It's very easy to select a hidden element and cause some hard to diagnose bugs.

### Adding The Selector to `elements.py`

Now that you have a working selector you can add it to the elements file.

First determine if this is an element that is in only one branch or both and add it to the appropriate object.

[The `elements.py` file](/pages/elements.py) in the `pages` directory contains every web element used in any test. 
The file is broken down into three classes
* `Elements`
Web elements used in every branch
* `ProdElements`
Web elements specific to the prod branch
* `RC elements`
Web elements specific to the RC branch

Both of the latter inherit from `Elements` so anything in `Elements` will be included and potentially overwritten by redefinitions in the branch specific classes.

To add your element group it with related elements so it's a bit easier to read.
Follow the comments to find the general sections.
Give it a unique identifying name.
```python
lesson_pass_off_button=()
```

Set the first element of its tuple to `By.CSS_SELECTOR`, unless you are reeaally desperate.
```python
lesson_pass_off_button=(By.CSS_SELECTOR)
```

Then, add your selector string.
```python
lesson_pass_off_button=(By.CSS_SELECTOR, "app-task-nav-button:nth-of-type(3)>ion-button")
```

Finally, add some notes to identify this element.
These will show up when an error occurs with this element, so they can be very helpful in diagnosing bugs.
An `og:` tag at the end for what page you used to create the tag is encouraged
```python
lesson_pass_off_button=(By.CSS_SELECTOR, "app-task-nav-button:nth-of-type(3)>ion-button", "lesson page button (og: spanish alphabet)")
```

With that you are done, and should be able to use this element in a test.








