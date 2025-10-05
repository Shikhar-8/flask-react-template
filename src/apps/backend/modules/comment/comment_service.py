from modules.application.common.types import PaginationResult
from modules.comment.internal.comment_reader import CommentReader
from modules.comment.internal.comment_writer import CommentWriter
from modules.comment.types import (
    Comment,
    CreateCommentPayload,
    UpdateCommentPayload,
)


class CommentService:
    @staticmethod
    def create_comment(*, params: CreateCommentPayload) -> Comment:
        return CommentWriter.create_comment(params=params)

    @staticmethod
    def get_comments_for_task(task_id: int) -> PaginationResult[Comment]:
        return CommentReader.get_comments_for_task(task_id=task_id)

    @staticmethod
    def update_comment(comment_id: int, *, params: UpdateCommentPayload) -> Comment:
        return CommentWriter.update_comment(comment_id=comment_id, params=params)

    @staticmethod
    def delete_comment(comment_id: int) -> None:
        return CommentWriter.delete_comment(comment_id=comment_id)
