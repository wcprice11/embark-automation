from typing import Union
from re import match
from dotenv import load_dotenv
load_dotenv()
from os import getenv
import requests

id_regex = r"^[0-9a-fA-F]{24}$"
url_regex = r"^(http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"

# see API documentation at https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post

def create_card(
        name: str                   = None,     description: str            = None, 
        position: Union[int, str]   = None,     due_date: str               = None,
        start_date: str             = None,     due_complete: bool          = None,
        list_id: str                = None,     member_ids: list[str]       = None, 
        label_ids: list[str]        = None,     source_url: str             = None,
        source_file: str            = None,     mime_type: str              = None,
        source_card_id: str         = None,     keep_from_source: str       = "all",
        address: str                = None,     location_name: str          = None,
        coordinates: str            = None
    ):
    request_name:               str
    request_description:        str
    request_position :          Union[int, str]
    request_due_date:           str
    request_start_date:         str
    request_due_complete:       bool
    request_list_id:            str
    request_member_ids:         str
    request_label_ids:          str
    request_source_url:         str
    request_source_file:        str # binary
    request_mime_type:          str
    request_source_card_id:     str
    request_keep_from_source:   str
    request_address:            str
    request_location_name:      str
    request_coordinates:        str

    # validations
    if(name is not None):                       name = request_name
    if(description is not None):                description = request_description
    if(position is not None and (position == "top" or position == "bottom" or position > 0)):             
                                                position = request_position
    if(due_date is not None and True):          due_date = request_due_date     # FIXME Which date format?
    if(start_date is not None and True):        start_date = request_start_date # FIXME ditto
    if(due_complete is not None):               due_complete = request_due_complete
    if(list_id is not None and match(id_regex, list_id)):           
                                                list_id = request_list_id
    if(member_ids is not None and True):        member_ids = request_member_ids # FIXME list comprehension
    if(label_ids is not None and True):         label_ids = request_label_ids   # FIXME ditto
    if(source_url is not None and match(url_regex, source_url)):        
                                                source_url = request_source_url
    if(source_file is not None):                source_file = request_source_file
    if(mime_type is not None and len(mime_type) <= 256):
                                                mime_type = request_mime_type
    if(source_card_id is not None and match(id_regex, source_card_id)):
                                                source_card_id = request_source_card_id
    if(keep_from_source is not None and True):  keep_from_source = request_keep_from_source
    if(address is not None and True):           address = request_address
    if(location_name is not None and True):     location_name = request_location_name
    if(coordinates is not None and True):       coordinates = request_coordinates

    key = getenv("trello_api_key")
    token = getenv("trello_api_token")
    to_replicate_list_id = getenv("trello_to_replicate_list_id")
