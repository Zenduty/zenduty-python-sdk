import logging
from uuid import UUID
from typing import List

from zenduty.apiV2.serializer import JsonSerializable

class AccountRole(JsonSerializable):
    unique_id: UUID
    name: str
    description: str
    permissions: List[str]

    def __init__(
        self,
        unique_id: UUID,
        name: str,
        description: str,
        permissions: List[str],
        **kwargs
    ) -> None:
        self.unique_id = unique_id if isinstance(unique_id, UUID) else UUID(unique_id)
        self.name = name
        self.description = description
        self.permissions = permissions
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')
