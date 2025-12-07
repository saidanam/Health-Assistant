"""
Doctor Appointment Scheduler Sequential Agent
"""

from google.adk.agents import SequentialAgent

from .subagents.patient_issue_summary_agent import patient_issue_summary_agent
from .subagents.doctor_finding_agent import doctor_finding_agent
from .subagents.appointment_booking_agent import appointment_booking_agent
from .subagents.appointment_confirmation_agent import appointment_confirmation_agent

doctor_appointment_scheduler_agent = SequentialAgent(
    name="DoctorAppointmentSchedulerPipeline",
    sub_agents=[
        patient_issue_summary_agent,
        doctor_finding_agent,
        appointment_booking_agent,
        appointment_confirmation_agent
    ],
    description="Sequential pipeline for booking doctor appointments: summarises issue, finds doctor, books appointment, confirms to patient."
)
