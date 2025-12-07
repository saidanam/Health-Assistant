from google.adk.agents import LlmAgent
from precare_agent.tools.meeting_scheduler_tool import MeetingSchedulerTool

GEMINI_MODEL = "gemini-2.0-flash"

appointment_booking_agent = LlmAgent(
    name="AppointmentBookingAgent",
    model=GEMINI_MODEL,
    instruction="""
You are an Appointment Booking AI.

Given:
- Doctor selection: {doctor_selection}
- Patient issue summary: {patient_issue_summary}
Must Use the meeting scheduling tool to schdule the appointment with respective doctor. 
Book an appointment with the selected doctor.
Output confirmation details including date, time, location, and Google Meet link.

Example output: "Booked appointment with Dr. Sharma, Dermatologist, on 28 Sept at 10:00 AM at Sunrise Medical Center. Google Meet link: https://meet.google.com/xyz"
""",
    description="Books appointment with the selected doctor.",
    output_key="appointment_booking_confirmation",
    tools=[MeetingSchedulerTool],
)
