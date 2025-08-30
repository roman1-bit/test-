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
        resp = requests.post(self.url + 'api-v2/projects',
                             json=project, headers=headers)
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
        resp = requests.put(self.url + 'api-v2/projects/' + id_project,
                            json=new_title, headers=headers)
        resp.json()
        id_project = resp.json()
        return resp.status_code, id_project

    def get_by_id(self, token, id_project):
        headers = {
            'Authorization': f"Bearer {token}",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url + 'api-v2/projects/' + id_project,
                            headers=headers)
        info = resp.json()
        return resp.status_code, info


def base_url():
    return None
