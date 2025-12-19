import requests
from src.config import (
    ZOHO_CLIENT_ID,
    ZOHO_CLIENT_SECRET,
    ZOHO_REFRESH_TOKEN,
    ZOHO_BASE_URL
)


class ZohoClient:
    def __init__(self):
        self.access_token = self._get_access_token()
        self.headers = {
            "Authorization": f"Zoho-oauthtoken {self.access_token}",
            "Content-Type": "application/json"
        }

    def _get_access_token(self):
        url = "https://accounts.zoho.in/oauth/v2/token"
        payload = {
            "refresh_token": ZOHO_REFRESH_TOKEN,
            "client_id": ZOHO_CLIENT_ID,
            "client_secret": ZOHO_CLIENT_SECRET,
            "grant_type": "refresh_token"
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json()["access_token"]

    # ---------------- GET JOBS ----------------
    def get_jobs(self):
        params = {
            "fields": "id,Posting_Title,City,Job_Opening_Status",
            "page": 1,
            "per_page": 200
        }

        response = requests.get(
            f"{ZOHO_BASE_URL}/JobOpenings",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json().get("data", [])

    # ---------------- CREATE CANDIDATE ----------------
    def create_candidate(self, name, email, phone, job_id):
        """
        Creates a candidate and automatically associates them with a job.
        Zoho Recruit automatically creates the application when Job_Opening_Id is provided.
        """
        payload = {
            "data": [
                {
                    "Last_Name": name,
                    "Email": email,
                    "Mobile": phone,
                    "Job_Opening_Id": job_id  # ✅ IMPORTANT
                }
            ]
        }

        response = requests.post(
            f"{ZOHO_BASE_URL}/Candidates",
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()

        return response.json()["data"][0]["details"]["id"]

    # ---------------- GET APPLICATIONS ----------------
    def get_applications(self, job_id):
        params = {
            "job_id": job_id,
            "page": 1,
            "per_page": 200
        }

        response = requests.get(
            f"{ZOHO_BASE_URL}/Applications",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json().get("data", [])
