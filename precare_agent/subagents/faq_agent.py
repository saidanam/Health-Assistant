from google.adk.agents import Agent

faq_agent = Agent(
    name="faq_agent",
    model="gemini-2.0-flash",
    description="Handles general health queries with self-service answers.",
    instruction="""
You are the FAQ Agent.
1. Answer common health and preventive care questions.
2. Reduce doctor workload by providing clear answers.
""",
    sub_agents=[],
    tools=[]
)
