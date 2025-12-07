"""
Send email tool using Gmail API via OAuth.
"""

import base64
from email.mime.text import MIMEText
from typing import Optional, List

from .gmail_utils import get_gmail_service


def sendEmailTool(
    to: str,
    subject: str,
    body: str,
    sender: Optional[str] = None,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
) -> dict:
    """
    Send an email using Gmail API.

    Args:
        to (str): Recipient email address
        subject (str): Email subject
        body (str): Email body
        sender (str, optional): Sender email. Defaults to "me" (authenticated user)
        cc (list, optional): List of CC emails
        bcc (list, optional): List of BCC emails

    Returns:
        dict: Information about email sending status
    """
    try:
        service = get_gmail_service()
        if not service:
            return {"status": "error", "message": "Failed to authenticate Gmail service."}

        sender_email = sender or "me"

        # Build MIME message
        message = MIMEText(body)
        message["to"] = to
        message["from"] = sender_email
        message["subject"] = subject
        if cc:
            message["cc"] = ", ".join(cc)
        if bcc:
            message["bcc"] = ", ".join(bcc)

        encoded_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

        # Send the email
        sent_message = service.users().messages().send(userId="me", body=encoded_message).execute()

        return {
            "status": "success",
            "message": f"Email sent successfully to {to}",
            "message_id": sent_message.get("id"),
        }

    except Exception as e:
        return {"status": "error", "message": f"Error sending email: {str(e)}"}
