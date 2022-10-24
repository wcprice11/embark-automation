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
        # TO_DO
        pass
        # Should be a requests call taking the two IDs as parameters

    def copy_user(source_user_id, target_user_id):
        # TO_DO
        pass
    
    def get_password(self) -> str:
        return getenv(self.username + "_PASSWORD")

blank_user = BaseUser()
blank_user.ID = 1002309856049123

personal_account = User(blank_user)
personal_account.username = "Christian_Price"

test_user_00 = User(blank_user)
test_user_00.username  = "test_embarkUser_00_cp"

test_user_01 = User(blank_user)
test_user_01.username = "test_embarkUser_01_cp"