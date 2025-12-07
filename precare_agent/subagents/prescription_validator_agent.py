from google.adk.agents import Agent

prescription_validator_agent = Agent(
    name="prescription_validator_agent",
    model="gemini-2.0-flash",
    description="Validates prescriptions for safety and interactions.",
    instruction="""
You are the Prescription Validator Agent.
1. Verify authenticity of prescriptions.
2. Check for drug interactions.
3. Flag unsafe or duplicate medicines.
""",
    sub_agents=[],
    tools=[]
)
