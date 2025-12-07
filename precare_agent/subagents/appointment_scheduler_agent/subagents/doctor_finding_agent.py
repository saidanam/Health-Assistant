"""
Doctor Finding Agent
"""

import json
from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

# Load doctor data directly from your provided path
with open("/Users/sideman/adk/HealthCareADK/Health-Assistant/precare_agent/data/doctors.json", "r", encoding="utf-8") as f:
    doctors_data = json.load(f)

doctor_finding_agent = LlmAgent(
    name="DoctorFindingAgent",
    model=GEMINI_MODEL,
    instruction=f"""
You are a Doctor Finding AI.

Given the patient's issue summary:
{{patient_issue_summary}}

From the following list of doctors:
{json.dumps(doctors_data, indent=2)}

Identify the most suitable doctor based on:
- Specialty relevant to the issue
- Location preference
- Availability
- Urgency

Output: Doctor name, specialty, hospital name, location, and available time in plain text.

Example output: "Dr. Sharma, Dermatologist, Sunrise Medical Center, Bangalore, India, available 28 Sept 10:00 AM."
""",
    description="Finds a doctor matching the patient's issue.",
    output_key="doctor_selection"
)
