from src.services.zoho_client import ZohoClient
from src.utils.response import success, error


def get_jobs(event, context):
    try:
        client = ZohoClient()
        jobs = client.get_jobs()

        # Map Zoho statuses to unified statuses
        status_map = {
            "IN-PROGRESS": "OPEN",
            "OPEN": "OPEN",
            "CLOSED": "CLOSED",
            "DRAFT": "DRAFT"
        }

        unified_jobs = []

        for job in jobs:
            unified_jobs.append({
                "id": job["id"],
                "title": job["Posting_Title"],
                "location": job.get("City", ""),
                "status": status_map.get(
                    job["Job_Opening_Status"].upper(),
                    "OPEN"
                ),
                "external_url": ""
            })

        return success(unified_jobs)

    except Exception as e:
        return error(str(e))
