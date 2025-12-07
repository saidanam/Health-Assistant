"""
Create meeting tool for Google Meet (via Google Calendar integration).
"""

import datetime
import json
from typing import Optional

from .calendar_utils import get_calendar_service, parse_datetime

DOCTORS_FILE_PATH = "/Users/sideman/adk/HealthCareADK/Health-Assistant/precare_agent/data/doctors.json"


def load_doctors_data():
    try:
        with open(DOCTORS_FILE_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Error loading doctors data: {e}")
        return []


def get_doctor_email(doctor_name: str) -> Optional[str]:
    doctors_data = load_doctors_data()
    for doctor in doctors_data:
        if doctor.get("name") == doctor_name:
            return doctor.get("email")
    return None


def MeetingSchedulerTool(
    summary: str,
    start_time: str,
    end_time: str,
    doctor_name: str,
) -> dict:
    """
    Create a new Google Meet meeting using Calendar API and
    add the doctor as an attendee.

    Args:
        summary (str): Meeting title/summary
        start_time (str): Start time (YYYY-MM-DD HH:MM)
        end_time (str): End time (YYYY-MM-DD HH:MM)
        doctor_name (str): Name of the doctor

    Returns:
        dict: Information about the created meeting or error details
    """
    try:
        service = get_calendar_service()
        if not service:
            return {"status": "error", "message": "Failed to authenticate with Google Calendar."}

        calendar_id = "primary"

        start_dt = parse_datetime(start_time)
        end_dt = parse_datetime(end_time)

        if not start_dt or not end_dt:
            return {"status": "error", "message": "Invalid date/time format. Please use YYYY-MM-DD HH:MM."}

        timezone_id = "America/New_York"
        try:
            settings = service.settings().list().execute()
            for setting in settings.get("items", []):
                if setting.get("id") == "timezone":
                    timezone_id = setting.get("value")
                    break
        except Exception:
            pass

        doctor_email = get_doctor_email(doctor_name)
        attendees = [{"email": doctor_email}] if doctor_email else []

        event_body = {
            "summary": summary,
            "start": {"dateTime": start_dt.isoformat(), "timeZone": timezone_id},
            "end": {"dateTime": end_dt.isoformat(), "timeZone": timezone_id},
            "conferenceData": {
                "createRequest": {
                    "requestId": f"meet-{datetime.datetime.now().timestamp()}",
                    "conferenceSolutionKey": {"type": "hangoutsMeet"},
                }
            },
        }

        if attendees:
            event_body["attendees"] = attendees

        event = (
            service.events()
            .insert(calendarId=calendar_id, body=event_body, conferenceDataVersion=1)
            .execute()
        )

        return {
            "status": "success",
            "message": "Meeting created successfully",
            "meeting_id": event["id"],
            "meeting_link": event.get("hangoutLink", ""),
            "event_link": event.get("htmlLink", ""),
        }

    except Exception as e:
        return {"status": "error", "message": f"Error creating meeting: {str(e)}"}
