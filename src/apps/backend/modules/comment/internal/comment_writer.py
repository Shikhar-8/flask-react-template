from modules.application.database import db
from modules.comment.internal.store.comment import Comment as CommentStore
from modules.comment.types import CreateCommentPayload, UpdateCommentPayload, Comment
from modules.task.internal.task_reader import TaskReader
from modules.task.types import GetTaskParams

class CommentWriter:
    @staticmethod
    def create_comment(*, params: CreateCommentPayload) -> Comment:
        # Ensure task exists
        TaskReader.get_task(params=GetTaskParams(id=params["task_id"]))

        comment = CommentStore(
            task_id=params["task_id"],
            content=params["content"],
        )
        db.session.add(comment)
        db.session.commit()
        return comment.to_dict()

    @staticmethod
    def update_comment(comment_id: int, *, params: UpdateCommentPayload) -> Comment:
        comment = CommentStore.query.get(comment_id)
        if not comment:
            raise Exception("Comment not found") # TODO: proper error
        
        comment.content = params["content"]
        db.session.commit()
        return comment.to_dict()

    @staticmethod
    def delete_comment(comment_id: int) -> None:
        comment = CommentStore.query.get(comment_id)
        if not comment:
            raise Exception("Comment not found") # TODO: proper error

        db.session.delete(comment)
        db.session.commit()
