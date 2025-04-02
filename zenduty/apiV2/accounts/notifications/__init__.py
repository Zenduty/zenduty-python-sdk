from zenduty.apiV2.accounts.members import AccountMember
from .models import ContactMethod, NotificationRule
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod


class AccountNotificationClient:
    def __init__(self, client: ZendutyClient, member: AccountMember):
        self._client = client
        self._member = member

    def list_member_contact_methods(self) -> list[ContactMethod] :
        """list members contact methods
        Returns:
            list [ContactMethodObject]: list of Contact Method objects
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET, 
            endpoint=f"/api/account/users/{self._member.user.username}/contacts/"
            )
        
        return [ContactMethod(**contact) for contact  in response]

    def get_member_contact_method(self, contact_method_id: str) -> ContactMethod:
        """Get member contact method object by contact_method_id

        Args:
            contact_method_id (str): the unique id of contact method

        Returns:
            ContactMethod: Contact Method object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET, 
            endpoint=f"/api/account/users/{self._member.user.username}/contacts/{contact_method_id}/"
            )
        return ContactMethod(**response)

    def create_member_contact_method(self, name: str, value: str, contact_type: int) -> ContactMethod:
        """Create member contact method

        Args:
            contact_method_id (str): the unique id of contact method
            name (str): name of the contact method
            value (str): value for the contact method
            contact_type (int): contact type

        Returns:
            ContactMethod: Contact Method object
        """

        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST, 
            endpoint=f"/api/account/users/{self._member.user.username}/contacts/",
            request_payload={
                "name":name,
                "value": value,
                "contact_type": contact_type
            },
            success_code=201
            )
        return ContactMethod(**response)
    
    def delete_member_contact_method(self, contact_method_id: str) -> None:
        """Delete member contact method

        Args:
            contact_method_id (str): the unique id of contact method

        Returns:
            None
        """

        response = self._client.execute(
            method=ZendutyClientRequestMethod.DELETE, 
            endpoint=f"/api/account/users/{self._member.user.username}/contacts/{contact_method_id}",
            )
        return None
    
    def list_member_notification_rules(self) -> list[NotificationRule]:

        """list members notification rules
        Returns:
            list [NotificationRules]: list of Notification Rule objects
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET, 
            endpoint=f"/api/account/users/{self._member.user.username}/notification_rules/"
            )
        return [NotificationRule(**contact) for contact  in response]
    
    def get_member_notification_rules(self, notification_rule_id: str) -> NotificationRule:
        """Get member nottification rule object by notification_rule_id

        Args:
            notification_rule_id (str): the unique id of notification rule

        Returns:
            ContactMethod: Contact Method object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET, 
            endpoint=f"/api/account/users/{self._member.user.username}/notification_rules/{notification_rule_id}/"
            )
        
        return NotificationRule(**response)
    
    def create_member_notification_rules(self, start_delay: int, contact_method: str, urgency: int) -> NotificationRule:
        """create member nottification rule object by notification_rule_id

        Args:
            start_delay (int): the unique id of notification rule
            contact_method (ContactMethod):
            urgency (int): urgency

        Returns:
            ContactMethod: Contact Method object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST, 
            endpoint=f"/api/account/users/{self._member.user.username}/notification_rules/",
            request_payload = {
                "contact" : contact_method,
                "start_delay": start_delay,
                "urgency": urgency
            },
            success_code=201
            )
        
        return NotificationRule(**response)
    

    def delete_member_notification_rule(self, notification_rule_id: str) -> None:
        """Delete member notification rule

        Args:
            notification_rule_id (str): the unique id of notification rule

        Returns:
            None
        """

        response = self._client.execute(
            method=ZendutyClientRequestMethod.DELETE, 
            endpoint=f"/api/account/users/{self._member.user.username}/notification_rules/{notification_rule_id}",
            success_code=204
            )
        return None