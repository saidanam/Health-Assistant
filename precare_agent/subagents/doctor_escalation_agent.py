from google.adk.agents import Agent
from precare_agent.subagents.appointment_scheduler_agent import doctor_appointment_scheduler_agent

doctor_escalation_agent = Agent(
    name="doctor_escalation_agent",
    model="gemini-2.0-flash",
    description="Routes escalations to the right specialist with full context and images.",
    instruction="""
You are the Doctor Escalation Agent.
Responsibilities:
1.Summarize the issue from the chat history. and call Doctor Appointment Scheduler for finding and booking appointment with the right specialist.
""",
    sub_agents=[doctor_appointment_scheduler_agent],
    tools=[]
)
