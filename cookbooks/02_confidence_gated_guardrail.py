"""02 — Confidence-gated guardrail.

Ask atomic Noul questions about each policy category, then let *your
code* decide what happens: act on high-confidence hits, send uncertain
cases to a human instead of guessing.

Run:  uv run 02_confidence_gated_guardrail.py
"""

# /// script
# requires-python = ">=3.10"
# dependencies = ["typesafe-sdk>=0.7.0", "python-dotenv>=1.0", "httpx2>=2.13"]
# ///

from typesafe_sdk import Noul

from common import make_client

client = make_client()

AUTO_BLOCK = 0.9   # act without a human above this
REVIEW = 0.5       # below this, treat as "model doesn't know"

post = "Great news! I made $8,000 last week trading with this bot, DM me 'profit' to get in."

response = client.system_one(
    state=post,
    questions={
        "scam": Noul(instructions="The content is a financial scam or 'get rich quick' scheme"),
        "hate": Noul(instructions="The content contains hateful or harassing language"),
        "sexual": Noul(instructions="The content contains sexual or adult material"),
    },
)

for name, answer in response.answers.items():
    p = answer.noul
    if p >= AUTO_BLOCK:
        verdict = "BLOCK"
    elif p >= REVIEW:
        verdict = "REVIEW"
    else:
        verdict = "PASS"
    print(f"{name:>8}: p={p:.2f} -> {verdict}")
