import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Postmortem


class PostmortemClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_postmortem(self) -> list[Postmortem]:
        """Get a list of all postmortem

        Returns:
            list[Postmortem]: List of postmortems
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/postmortem/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Postmortem(**r) for r in response]

    def get_postmortem_by_id(self, postmortem_id: UUID) -> Postmortem:
        """Get a postmortem by ID

        Args:
            postmortem_id (UUID): Postmoterm ID to fetch

        Returns:
            Postmortem: Postmoterm object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/postmortem/%s/"
            % (str(self._team.unique_id), str(postmortem_id)),
            success_code=200,
        )
        return Postmortem(**response)

    def create_postmortem(
        self,
        author: str,
        status: str,
        postmortem_data: str,
        incidents: list[str],
        title: str,
        download_status: int = 0,
        **kwargs
    ) -> Postmortem:
        """Create a postmortem

        Args:
            author (str): A system-generated string that represents the User object's username
            status (str): A string that represents the Postmortem object's status
            postmortem_data (str): A string that represents the Postmortem object's postmortem_data
            incidents (list[str]): An array of Postmortem Incident Unique IDs
            title (str): A string that represents the Postmortem object's title
            download_status (int, optional): An integer that represents the Postmortem object's download_status. 1 is uninitiated, 2 is initiated, 3 is finished and 4 is error. Defaults to 0.

        Returns:
            Postmortem: Created Postmotem object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/postmortem/" % str(self._team.unique_id),
            request_payload={
                "author": author,
                "status": status,
                "postmortem_data": postmortem_data,
                "incidents": [{"incident": i} for i in incidents],
                "title": title,
                "download_status": download_status,
            },
            success_code=201,
        )
        return self.get_postmortem_by_id(UUID(response["unique_id"]))

    def update_postmortem(self, postmortem: Postmortem) -> Postmortem:
        """Update a postmortem object passed

        Args:
            postmortem (Postmortem): Postmortem object to update

        Returns:
            Postmortem: Created postmortem object.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/postmortem/%s/"
            % (str(self._team.unique_id), str(postmortem.unique_id)),
            request_payload=json.loads(postmortem.to_json()),
            success_code=200,
        )
        return self.get_postmortem_by_id(UUID(response["unique_id"]))

    def delete_postmortem(self, postmortem: Postmortem):
        """Delete a postmotem object

        Args:
            postmortem (Postmortem): postmotem to delete
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/postmortem/%s/"
            % (str(self._team.unique_id), str(postmortem.unique_id)),
            success_code=204,
        )
