import json
from src.services.zoho_client import ZohoClient
from src.utils.response import success, error


def create_candidate(event, context):
    try:
        body = json.loads(event["body"])

        client = ZohoClient()
        candidate_id = client.create_candidate(
            name=body["name"],
            email=body["email"],
            phone=body["phone"],
            job_id=body["job_id"]
        )

        return success(
            {
                "candidate_id": candidate_id,
                "job_id": body["job_id"]
            },
            status=201
        )

    except Exception as e:
        return error(str(e))
