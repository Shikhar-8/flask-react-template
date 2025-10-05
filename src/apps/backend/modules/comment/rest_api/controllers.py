from flask import Blueprint, request, jsonify
from modules.comment.comment_service import CommentService
from modules.comment.types import CreateCommentPayload, UpdateCommentPayload

comment_bp = Blueprint('comments', __name__, url_prefix='/tasks/<int:task_id>/comments')

@comment_bp.route('/', methods=['POST'])
def create_comment(task_id):
    data = request.get_json()
    payload = CreateCommentPayload(task_id=task_id, content=data['content'])
    comment = CommentService.create_comment(params=payload)
    return jsonify(comment), 201

@comment_bp.route('/', methods=['GET'])
def get_comments(task_id):
    comments = CommentService.get_comments_for_task(task_id)
    return jsonify(comments)

@comment_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(task_id, comment_id):
    data = request.get_json()
    payload = UpdateCommentPayload(content=data['content'])
    comment = CommentService.update_comment(comment_id, params=payload)
    return jsonify(comment)

@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(task_id, comment_id):
    CommentService.delete_comment(comment_id)
    return '', 204
