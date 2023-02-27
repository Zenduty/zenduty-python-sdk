import json
from uuid import UUID
from ...client import ZendutyClient, ZendutyClientRequestMethod
from .._models import Team
from .models import TaskTemplate


class TaskTemplateClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_task_template(self) -> list[TaskTemplate]:
        """Get all the tasks templates

        Returns:
            list[TaskTemplate]: List of tasks templates
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/task_templates/"
            % str(self._team.unique_id),
            success_code=200,
        )
        return [TaskTemplate(**r) for r in response]

    def get_task_template_by_id(self, task_template_id: UUID) -> TaskTemplate:
        """Get a task temaplate by ID

        Args:
            task_template_id (UUID): template id for which template has to be fetched.

        Returns:
            TaskTemplate: TaskTemplate object that is fetched.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/task_templates/%s/"
            % (str(self._team.unique_id), str(task_template_id)),
            success_code=200,
        )
        return TaskTemplate(**response)

    def create_task_template(
        self, name: str, summary: str, due_immediately: int = 0, **kwargs
    ) -> TaskTemplate:
        """Create a new Task Template

        Args:
            name (str): name of the template
            summary (str): summary of the template
            due_immediately (int, optional): An integer that represents whether the Task Template object is due immediately or not. 0 is false and 1 is true. Defaults to 0.

        Returns:
            TaskTemplate: TaskTemplate object to return.
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/task_templates/"
            % str(self._team.unique_id),
            request_payload={
                "name": name,
                "summary": summary,
                "due_immediately": due_immediately,
            },
            success_code=201,
        )
        return self.get_task_template_by_id(UUID(response["unique_id"]))

    def update_task_template(self, task_template: TaskTemplate) -> TaskTemplate:
        """Update a TaskTemplate

        Args:
            task_template (TaskTemplate): task template to update.

        Returns:
            TaskTemplate: updated TaskTemplate object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/task_templates/%s/"
            % (str(self._team.unique_id), str(task_template.unique_id)),
            request_payload=json.loads(task_template.to_json()),
            success_code=200,
        )
        return self.get_task_template_by_id(UUID(response["unique_id"]))

    def delete_task_template(self, task_template: TaskTemplate):
        """delete a task template

        Args:
            task_template (TaskTemplate): Task template to delete.
        """
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/task_templates/%s/"
            % (str(self._team.unique_id), str(task_template.unique_id)),
            success_code=204,
        )
