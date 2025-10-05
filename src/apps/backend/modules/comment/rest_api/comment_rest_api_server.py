from flask import Blueprint
from modules.comment.rest_api.controllers import comment_bp

class CommentRestApiServer:
    @staticmethod
    def create() -> Blueprint:
        return comment_bp
