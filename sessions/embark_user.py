from dotenv import load_dotenv
load_dotenv()
from os import getenv
import requests


# accounts to clone from. 
# These shouldn't be used except to get to a consistent point to load from.
class BaseUser():
    def __init__(self, id:str) -> None:
        self.id = id


# accounts to clone to.
# These are the accounts that a test should load. 
# They can be reset to whatever BaseUser they are initiated with.

class User():
    def __init__(self, base_user: BaseUser, id:str, username:str) -> None:
        self.base_user = base_user
        self.id = id
        self.username = username

        self.reset_id = self.base_user.id
        self._clone_url = 'https://tall.global/userdata/clone/user'
        self._json_request = {
            "sourceUser": {
                "type": "SRC", 
                "userId": self.reset_id },
            "destUser": {
                "type": "DEST",
                "userId": self.id},
            "courseId": 1,
            "createUser": False,
            "overrideUserCheck": False}
    
    def reset(self) -> None:
        return self._clone_user(self.reset_id, self.id)


    def _clone_user(self, source_user_id:str, target_user_id:str):
        request = self._json_request
        request["sourceUser"]["userId"] = source_user_id
        request["destUser"]["userId"] = source_user_id
        x = requests.post(url=self._clone_url, json=request)
        return x

    def get_password(self) -> str:
        return getenv(self.username + "_PASSWORD")


blank_user = BaseUser(id="3875622384116696")

test_user_00 = User(
    base_user   = blank_user, 
    id          = "3868979468900847",
    username    = "test_embarkUser_00_cp")

test_user_02 = User(
    base_user  = blank_user, 
    id          = "4448979468900444",
    username    = "test_embarkUser_02_cp")
