import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import Tag


class TagClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_tags(self) -> list[Tag]:
        """Get all the tags

        Returns:
            list[Tag]: List of tags
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/tags/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Tag(**r) for r in response]

    def get_tag_by_id(self, tags_id: UUID) -> Tag:
        """Get a tag by ID

        Args:
            tags_id (UUID): tag id for which to fetch tag

        Returns:
            Tag: Tag object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/tags/%s/"
            % (str(self._team.unique_id), str(tags_id)),
            success_code=200,
        )
        return Tag(**response)

    def create_tag(self, name: str, color: str, **kwargs) -> Tag:
        """Create a tag object

        Args:
            name (str): Name of the tag
            color (str): color of the tag

        Returns:
            Tag: Tag object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/tags/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "color": color,
            },
            success_code=201,
        )
        return Tag(**response)

    def update_tag(self, tag: Tag) -> Tag:
        """Update a tag

        Args:
            tag (Tag): tag to be updated

        Returns:
            Tag: _description_
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/tags/%s/"
            % (str(self._team.unique_id), str(tag.unique_id)),
            request_payload=json.loads(tag.to_json()),
            success_code=200,
        )
        return Tag(**response)

    def delete_tag(self, tag: Tag):
        """Delete a tag

        Args:
            tag (Tag): Tag object to be deleted
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/tags/%s/"
            % (str(self._team.unique_id), str(tag.unique_id)),
            success_code=204,
        )
