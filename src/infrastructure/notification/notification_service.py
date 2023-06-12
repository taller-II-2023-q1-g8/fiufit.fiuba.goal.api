from google.oauth2 import service_account
import google.auth.transport.requests
import requests


class NotificationService:
    def __init__(self, goal_repository):
        self.goal_repository = goal_repository

    def _get_token(self):
        credentials = service_account.Credentials.from_service_account_file(
            'fiufit-73a11.json', scopes=["https://www.googleapis.com/auth/firebase.messaging"])
        request = google.auth.transport.requests.Request()
        credentials.refresh(request)
        return credentials.token


    def _send_notification_to_user(self, device_token: str, title: str, body: str):
        url = 'https://fcm.googleapis.com/v1/projects/fiufit-73a11/messages:send'

        headers = {
            'Authorization': 'Bearer ' + self._get_token(),
            'Content-Type': 'application/json',
        }

        json = {
            "message":{
                "token": device_token,
                "notification":{
                    "body": body,
                    "title": title
                },
                # "data": {
                #     "id": "1"
                # }
                # },
                # "android": {
                # "notification": {
                #     "click_action":"OPEN_ACTIVITY_3"
                # }
            },
        }

        response = requests.post(url, headers=headers, json=json)
        return response.text

    def new_goal_completed(self, username: str, goal_id: str):
        url = f"https://api-gateway-k1nl.onrender.com/user/device/{username}"
        response = requests.get(url)
        device_token = response.json()['message']

        print(f"Sending New Notification to {username}")
        if device_token is not None:
            goal_type = self.goal_repository.load_by_id(goal_id)['type']
            print(f"{username}'s device Token is: {device_token}")
            notification_body = f"Felicitaciones, haz completado: {goal_type}"
            self._send_notification_to_user(device_token=device_token, title="Meta Completada", body=notification_body)
        else:
            print(f"{username} has no associated device Token")