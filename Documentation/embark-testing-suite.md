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

## sessions

### driver

### embark_branch

### embark_session

### embark_user

The User is the last element of the session.
You may want to write a test the very first introduction to embark to make sure all the guides are present.
To do this, you would want to login to an account with no progress.
Conversely, you may want to check that something happens when you pass a certain level.
To do this, you would want an account that has had a lot of work put in.

Choosing a user for your session lets you accomplish this.

User objects and options can be found and should be kept in the `sessions/embark_user.py` file.

There are two classes of users, `BaseUser` and `User`.
A session only takes `User` objects, but each `User` has a `BaseUser` that it uses.
You can make a new `User` pretty easily. 

The first step is to make sure it has an account. 
Go to `https://id.churchofjesuschrist.org/` and click **Sign up**.
Choose a location, and then fill in the account information.
The username *must* start with "test" in order to function properly.
test_embarkUser_[number]_[initials] is a good way to keep track of which one is which.

keep track of the password (I'd recommend a password manager) and remember to not store it anywhere in the repository.
Instead store it in the `.env` file with this formatting.
`[username]_PASSWORD = '[password]'`

For the next step select "I am NOT a member of The Church of Jesus Christ of Latter-day Saints.".
You may be, but our little testing bot is not.

From there select a name; it can be anything you want.
Now, add a recovery email and hit next.

You will need to confirm the account from that email before continuing.

Once the account is confirmed we can get the user id.

go to the tall sign in page, and enter the login information on the church authentication page.

**Before you submit** open the network tab on the inspection tool.

hit the submit button and look for a `user` item in the network history. 
Inside the response payload, you can find an 16 digit id. 
Copy this and we're ready to make our embark user.

At the bottom of the file type the following:
``` python
[your test user] = User(
    baseUser    =
    id          =
    username    =
)
```
Paste your id as a string, and set the username.
``` python
[your test user] = User(
    baseUser    =
    id          = "1234567890123456"
    username    = "test_example_03_aa"
)
```
Choose a `BaseUser` you want this account to be able to reset to. 

``` python
[your test user] = User(
    baseUser    = MyBaseUser
    id          = "1234567890123456"
    username    = "test_example_03_aa"
)
```

Now you are good to go!


You can create your own `BaseUser` by following the steps above, and getting the account to the state you want.
You only need the id to create a `BaseUser`.
`[your base user] = BaseUser(id = "1122334455667788")`




