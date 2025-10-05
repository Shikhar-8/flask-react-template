import json
from typing import Tuple

from server import app
from modules.comment.comment_service import CommentService
from modules.comment.types import CreateCommentPayload, Comment
from tests.modules.task.base_test_task import BaseTestTask


class BaseTestComment(BaseTestTask):
    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    # URL HELPER METHODS

    def get_comment_api_url(self, task_id: int) -> str:
        return f"http://127.0.0.1:8080/api/tasks/{task_id}/comments"

    def get_comment_by_id_api_url(self, task_id: int, comment_id: int) -> str:
        return f"http://127.0.0.1:8080/api/tasks/{task_id}/comments/{comment_id}"

    # COMMENT HELPER METHODS

    def create_test_comment(self, task_id: int, content: str = "Test comment") -> Comment:
        return CommentService.create_comment(
            params=CreateCommentPayload(
                task_id=task_id,
                content=content,
            )
        )
