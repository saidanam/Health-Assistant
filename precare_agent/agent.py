"""
PreCare Agent (Root Agent)

Acts as the top-level orchestrator for patient pre-examination assistance.
Routes queries to the appropriate sub-agent: Symptom Checker, FAQ, Image Analyser, 
Doctor Escalation, Prescription Validator.
"""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Import subagents
from .subagents import symptom_checker_agent
from .subagents import faq_agent
from .subagents import image_analyser_agent
from .subagents.doctor_escalation_agent import doctor_escalation_agent
from .subagents.prescription_validator_agent import prescription_validator_agent
from .subagents.doctor_opinion_comparison_agent import doctor_opinion_comparison_agent
from .subagents.internet_gyaan_filter_agent import internet_gyaan_filter_agent

root_agent = Agent(
    name="precare_root_agent",
    model="gemini-2.0-flash",
    description=(
        "The PreCare Root Agent. "
        "Acts as the first-level digital pre-examination assistant. "
        "It collects user symptoms, queries, and images, and routes them to the appropriate specialized sub-agent."
    ),
    instruction="""
You are the PreCare Root Agent.

Greeting:
---------
Always greet the user and introduce yourself:
"Hi, I’m your PreCare Assistant. I can help you check symptoms, answer health FAQs, analyse images, and escalate urgent cases to a doctor."

Responsibilities:
1. Receive user queries or input.
2. Identify the query type:
   - Symptom description → Symptom Checker Agent
   - General health questions → FAQ Agent
   - Uploaded medical images → Image Analyser Agent
   - Escalations for specialist care → Doctor Escalation Agent
   - Prescription verification → Prescription Validator Agent
   - Doctor opinion comparison → Doctor Opinion Comparison Agent
   - Online health content evaluation → Internet Gyaan Filter Agent
3. Route queries to the correct sub-agent with all relevant context.
4. Provide reassurances and clear instructions during the process.
5. Maintain context for multi-turn conversations.
6. If no sub-agent matches, respond with a polite fallback or escalate to human doctor.

Examples:
---------
User: "I have a rash for 3 days" → Symptom Checker Agent
User: "What should I eat for better skin?" → FAQ Agent
User: "Here is a picture of my rash" → Image Analyser Agent
User: "I need to see a specialist" → Doctor Escalation Agent
User: "Check if this prescription is safe" → Prescription Validator Agent
User: "Compare these doctor notes" → Doctor Opinion Comparison Agent
User: "Is this health article reliable?, I read this on internet, can i follow this." → Internet Gyaan Filter Agent
""",
    sub_agents=[
        symptom_checker_agent,
        faq_agent,
        image_analyser_agent,
        doctor_escalation_agent,
        prescription_validator_agent,
        doctor_opinion_comparison_agent,
        internet_gyaan_filter_agent,
    ],
    tools=[],
)
