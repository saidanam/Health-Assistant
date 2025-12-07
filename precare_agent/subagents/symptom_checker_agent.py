from google.adk.agents import Agent

symptom_checker_agent = Agent(
    name="symptom_checker_agent",
    model="gemini-2.0-flash",
    description="Analyzes reported symptoms and suggests possible conditions or escalation.",
    instruction="""
You are the Symptom Checker Agent.
1. Ask clarifying questions about symptoms.
2. Provide possible conditions (not diagnosis).
3. Give urgency advice.
4. Escalate to Doctor Escalation Agent if needed.
""",
    sub_agents=[],
    tools=[]
)
