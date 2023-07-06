from google.oauth2 import service_account
import google.auth.transport.requests
import requests, os


SEND_NOTIFICATIONS_URL = os.environ.get("SEND_NOTIFICATIONS_URL")
if SEND_NOTIFICATIONS_URL is None:
    print("SEND_NOTIFICATIONS_URL not found in Environment")

DEVICE_TOKEN_URL = os.environ.get("DEVICE_TOKEN_URL")
if DEVICE_TOKEN_URL is None:
    print("DEVICE_TOKEN_URL not found in Environment")

PRIVATE_KEY_PATH = "/etc/secrets/fiufit-73a11.json"

class NotificationService:
    def __init__(self, goal_repository):
        self.goal_repository = goal_repository

    def _get_token(self):
        credentials = service_account.Credentials.from_service_account_file(
            PRIVATE_KEY_PATH,
            scopes=["https://www.googleapis.com/auth/firebase.messaging"],
        )
        request = google.auth.transport.requests.Request()
        credentials.refresh(request)
        return credentials.token

    def _send_notification_to_user(self, device_token: str, title: str, body: str):
        url = SEND_NOTIFICATIONS_URL
        if url is None:
            return

        headers = {
            "Authorization": "Bearer " + self._get_token(),
            "Content-Type": "application/json",
        }

        json = {
            "message": {
                "token": device_token,
                "notification": {"body": body, "title": title},
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

    def parsed_goal_title(self, goal):
        if goal["type"] == "max_weight_lifted_in_exercise":
            return f"Hacer {goal['exercise_title']} con {goal['goal_weight_in_kg']}kg"
        if goal["type"] == "training_plan_completion":
            return (
                f"Completar {goal['goal_num_of_completions']} planes de entrenamiento"
            )

        raise ValueError(f"Invalid goal type {goal['type']} (ID: f{goal['_id']})")

    def new_goal_completed(self, username: str, goal_id: str):
        if DEVICE_TOKEN_URL is None:
            return
        
        url = f"{DEVICE_TOKEN_URL}/{username}"
        print("URL: ", url)
        response = requests.get(url)
        device_token = response.json()["message"]

        print(f"Sending New Notification to {username}")
        if device_token is not None:
            completed_goal = self.goal_repository.load_by_id(goal_id)
            completed_goal_title = self.parsed_goal_title(completed_goal)
            print(f"{username}'s device Token is: {device_token}")
            notification_body = (
                f"Felicitaciones, haz logrado: {completed_goal_title}"
            )
            self._send_notification_to_user(
                device_token=device_token,
                title="Meta Completada",
                body=notification_body,
            )
        else:
            print(f"{username} has no associated device Token")
