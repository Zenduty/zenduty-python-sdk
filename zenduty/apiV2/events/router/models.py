import logging
from uuid import UUID

from zenduty.apiV2.serializer import JsonSerializable


class Router(JsonSerializable):
    unique_id: UUID
    name: str
    description: str
    account: UUID
    is_enabled: bool
    integration_key: str
    created_at: str
    account_identifier: str

    def __init__(
        self,
        unique_id: UUID,
        name: str,
        description: str,
        account: UUID,
        is_enabled: bool,
        integration_key: str,
        created_at: str,
        account_identifier: str,
        **kwargs
    ) -> None:
        self.unique_id = unique_id if isinstance(unique_id, UUID) else UUID(unique_id)
        self.name = name
        self.description = description
        self.account = account if isinstance(account, UUID) else UUID(account)
        self.is_enabled = is_enabled
        self.integration_key = integration_key
        self.created_at = created_at
        self.account_identifier = account_identifier
        if kwargs:
            logging.info(f'Received unexpected return values for {self.__class__.__name__}: {list(kwargs.keys())}')
        
