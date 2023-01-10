# Creating a User

User objects and options can be found and should be kept in the `sessions/embark_user.py` file.

There are two classes of users, `BaseUser` and `User`.
A session only takes `User` objects, but each `User` has a `BaseUser` that it uses to reset.
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

It's important to not use this account any further or all users based off of it will also inherit any changes.
They can technically be reset, but it's much safer to not risk it.