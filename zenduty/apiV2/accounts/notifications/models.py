import logging
from uuid import UUID
from datetime import datetime

from zenduty.apiV2.serializer import JsonSerializable

class ContactMethod(JsonSerializable):
    unique_id: UUID
    name: str
    creation_date: datetime
    value: str
    contact_type: int
    
    def __init__(
        self,
        unique_id: str,
        name: str,
        creation_date: str,
        value: str,
        contact_type: int,
        **kwargs) -> None:
        self.unique_id = unique_id if isinstance(unique_id, UUID) else UUID(unique_id)
        self.name = name
        self.creation_date = creation_date if isinstance(creation_date, datetime) else datetime.strptime(creation_date, '%Y-%m-%d')
        self.value = value
        self.contact_type = contact_type
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')

class NotificationRule(JsonSerializable):
    unique_id: UUID
    creation_date: datetime
    start_delay: int
    type: str
    contact: UUID
    urgency: int
    user: str
    
    def __init__(
        self,
        unique_id: str,
        creation_date: str,
        start_delay: int,
        type: str,
        contact: str,
        urgency: int,
        user: str,
        **kwargs
        ):
        self.unique_id = unique_id if isinstance(unique_id, UUID) else UUID(unique_id)
        self.creation_date = creation_date if isinstance(creation_date, datetime) else datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.start_delay = start_delay 
        self.type = type
        self.contact = contact if isinstance(contact, UUID) else UUID(contact)
        self.urgency = urgency
        self.user = user
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')
        