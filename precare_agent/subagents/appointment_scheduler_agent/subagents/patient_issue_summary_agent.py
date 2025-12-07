"""
Patient Issue Summary Agent
"""

from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

patient_issue_summary_agent = LlmAgent(
    name="PatientIssueSummaryAgent",
    model=GEMINI_MODEL,
    instruction="""
You are a Patient Issue Summary AI.

Summarise the patient's issue clearly and concisely, including:
- Symptoms
- Duration
- Urgency
- Location
- Relevant history

Example output: "Patient reports rash on left arm for 3 days, mild itching, no fever."
""",
    description="Summarises the patient's health issue for scheduling.",
    output_key="patient_issue_summary"
)
