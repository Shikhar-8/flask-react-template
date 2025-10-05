from modules.application.common.types import PaginationResult
from modules.comment.internal.store.comment import Comment as CommentStore
from modules.comment.types import Comment

class CommentReader:
    @staticmethod
    def get_comments_for_task(task_id: int) -> PaginationResult[Comment]:
        comments = CommentStore.query.filter_by(task_id=task_id).all()
        return PaginationResult(
            items=[c.to_dict() for c in comments],
            page=1,
            per_page=len(comments),
            total_items=len(comments),
            total_pages=1,
        )
