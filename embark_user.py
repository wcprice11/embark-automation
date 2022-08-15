from dotenv import load_dotenv
load_dotenv()
from os import getenv


# accounts to clone from
class BaseUser():
    def __init__(self) -> None:
        self.ID :int


# accounts to clone to
class User():
    def __init__(self, base_user: BaseUser) -> None:
        self.base_user = base_user
        self.ID :int
        self.username :str
    
    def reset(self) -> None:
        pass
        # Should be a requests call taking the two IDs as parameters
    
    def get_password(self) -> str:
        return getenv(self.username + "_PASSWORD")

blank_user = BaseUser()
blank_user.ID = 1002309856049123

personal_account = User(blank_user)
personal_account.username = "Christian_Price"

test_user_00 = User(blank_user)
test_user_00.username  = "test_embarkUser_00_cp"
