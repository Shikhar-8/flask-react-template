import json
from server import app
from tests.modules.comment.base_test_comment import BaseTestComment


class TestCommentApi(BaseTestComment):
    def test_create_comment(self):
        account, token = self.create_account_and_get_token()
        task = self.create_test_task(account_id=account["id"])

        with app.test_client() as client:
            response = client.post(
                self.get_comment_api_url(task_id=task["id"]),
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                data=json.dumps({"content": "This is a test comment"}),
            )

            self.assertEqual(response.status_code, 201)
            data = response.get_json()
            self.assertEqual(data["content"], "This is a test comment")
            self.assertEqual(data["task_id"], task["id"])

    def test_get_comments_for_task(self):
        account, token = self.create_account_and_get_token()
        task = self.create_test_task(account_id=account["id"])
        self.create_test_comment(task_id=task["id"], content="Comment 1")
        self.create_test_comment(task_id=task["id"], content="Comment 2")

        with app.test_client() as client:
            response = client.get(
                self.get_comment_api_url(task_id=task["id"]),
                headers={"Authorization": f"Bearer {token}"},
            )

            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(len(data["items"]), 2)

    def test_update_comment(self):
        account, token = self.create_account_and_get_token()
        task = self.create_test_task(account_id=account["id"])
        comment = self.create_test_comment(task_id=task["id"])

        with app.test_client() as client:
            response = client.put(
                self.get_comment_by_id_api_url(task_id=task["id"], comment_id=comment["id"]),
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                data=json.dumps({"content": "Updated comment"}),
            )

            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data["content"], "Updated comment")

    def test_delete_comment(self):
        account, token = self.create_account_and_get_token()
        task = self.create_test_task(account_id=account["id"])
        comment = self.create_test_comment(task_id=task["id"])

        with app.test_client() as client:
            response = client.delete(
                self.get_comment_by_id_api_url(task_id=task["id"], comment_id=comment["id"]),
                headers={"Authorization": f"Bearer {token}"},
            )

            self.assertEqual(response.status_code, 204)
