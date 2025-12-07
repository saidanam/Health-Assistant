from google.adk.agents import Agent

from .doctor_escalation_agent import doctor_escalation_agent


image_analyser_agent = Agent(
    name="image_analyser_agent",
    model="gemini-2.0-flash",
    description="Analyses uploaded medical images using LLM and escalates if needed.",
    instruction="""
You are the Image Analyser Agent.
1. Accept uploaded medical images.
2. Analyse using your general LLM knowledge.
3. Provide descriptive summary.
4. Escalate severe/unclear cases to Doctor Escalation Agent with stored data. 
5. Confirm with the before escalating.
""",
    sub_agents=[],
    tools=[]
)
