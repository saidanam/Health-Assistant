from google.adk.agents import LlmAgent
from precare_agent.tools.send_email_tool import sendEmailTool

GEMINI_MODEL = "gemini-2.0-flash"

appointment_confirmation_agent = LlmAgent(
    name="AppointmentConfirmationAgent",
    model=GEMINI_MODEL,
    instruction="""
You are an Appointment Confirmation AI.

Given:
- Booking confirmation: {appointment_booking_confirmation}

Generate a patient-friendly confirmation message and send it to the patient via email.

Example output: "Your appointment with Dr. Sharma, Dermatologist, is confirmed for 28 Sept at 10:00 AM at ABC Clinic."
""",
    description="Confirms the booked appointment to the patient and sends an email.",
    output_key="final_confirmation_message",
    tools=[sendEmailTool]
)
