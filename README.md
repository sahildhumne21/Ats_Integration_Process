\# ATS Unified API – Zoho Recruit Integration



\## Overview

This project implements a unified ATS (Applicant Tracking System) API layer using Python.

It integrates with Zoho Recruit using OAuth2 (Refresh Token flow) and exposes standardized REST APIs.



The goal is to abstract ATS-specific logic and provide a consistent API interface that can be extended to other ATS platforms in the future.



---



\## Tech Stack

\- Python 3.10

\- Serverless Framework

\- Zoho Recruit API

\- OAuth2 (Refresh Token Flow)

\- serverless-offline (local testing)



---



\## APIs Implemented



\### 1. GET /jobs

Returns a unified list of job openings.



\*\*Response format:\*\*

```json

{

&nbsp; "id": "string",

&nbsp; "title": "string",

&nbsp; "location": "string",

&nbsp; "status": "OPEN | CLOSED | DRAFT",

&nbsp; "external\_url": "string"

}



