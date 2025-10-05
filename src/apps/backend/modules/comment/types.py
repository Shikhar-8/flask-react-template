from typing import TypedDict, List
from datetime import datetime

class Comment(TypedDict):
    id: int
    task_id: int
    content: str
    created_at: datetime
    updated_at: datetime

class CreateCommentPayload(TypedDict):
    task_id: int
    content: str

class UpdateCommentPayload(TypedDict):
    content: str
