import requests


class Pages:

    def __init__(self, base_url) -> None:
        self.url = base_url

    def create(self, token, title):
        headers = {
            'Authorization': f"Bearer {token}",
            'Content-Type': 'application/json'
        }
        project = {
            'title': title
        }
        url = f"{self.url}api-v2/projects"
        resp = requests.post(url, json=project, headers=headers)
        id_project = resp.json()
        return resp.status_code, id_project

    def change(self, token, title2, id_project):
        headers = {
            'Authorization': f"Bearer {token}",
            'Content-Type': 'application/json'
        }
        new_title = {
            'title': title2
        }
        url = f"{self.url}api-v2/projects/{id_project}"
        resp = requests.put(url, json=new_title, headers=headers)
        response_data = resp.json()
        return resp.status_code, response_data

    def get_by_id(self, token, id_project):
        headers = {
            'Authorization': f"Bearer {token}",
            'Content-Type': 'application/json'
        }
        url = f"{self.url}api-v2/projects/{id_project}"
        resp = requests.get(url, headers=headers)
        info = resp.json()
        return resp.status_code, info
