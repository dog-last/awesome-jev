"""01 — Support ticket triage: one call, three question types.

Mix Choice, Score and Noul in a single request. Every question is
evaluated in parallel against the same state, so this costs about the
same latency as asking one question.

Run:  uv run 01_ticket_triage.py
"""

# /// script
# requires-python = ">=3.10"
# dependencies = ["typesafe-sdk>=0.7.0", "python-dotenv>=1.0", "httpx2>=2.13"]
# ///

from typesafe_sdk import Choice, Noul, Score

from common import make_client

client = make_client()

ticket = (
    "Hi, I've been trying to connect my Stripe account for 3 days and the "
    "integration keeps failing. I'm losing sales. Please help ASAP."
)

response = client.system_one(
    state=ticket,
    questions={
        "department": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payment or subscription issues",
                "technical": "Bugs or integration problems",
                "sales": "Pricing or account questions",
            },
        ),
        "frustration": Score(
            instructions="How frustrated the customer appears",
            criteria=["Calm, just stating facts", "Frustrated but civil", "Very angry"],
        ),
        "is_urgent": Noul(
            instructions="The message conveys urgency or time-sensitivity",
        ),
    },
)

dept = response.answers["department"]
print(f"route to:   {dept.choice} (confidence {dept.confidence:.2f})")
print(f"frustration: {response.answers['frustration'].score:.1f} / 2")
print(f"urgent:      {response.answers['is_urgent'].noul:.2f}")
