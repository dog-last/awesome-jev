"""04 — Composite scoring: decompose a big judgment into atomic ones.

Don't ask "is this a good startup pitch?" — ask each factor separately
and combine them with a formula in your code. When priorities change,
you change a coefficient, not a prompt. (Official pattern: composite
scoring — https://docs.typesafe.ai/patterns)

Run:  uv run 04_composite_scoring.py
"""

# /// script
# requires-python = ">=3.10"
# dependencies = ["typesafe-sdk>=0.7.0", "python-dotenv>=1.0", "httpx2>=2.13"]
# ///

from typesafe_sdk import Score

from common import make_client

client = make_client()

WEIGHTS = {"market": 0.4, "feasibility": 0.35, "differentiation": 0.25}
MIN_CONFIDENCE = 0.5

pitch = (
    "We build sidewalk delivery robots for university campuses. "
    "Three campuses signed, $12k MRR, unit economics positive at 40 deliveries/day."
)

levels = ["Very weak", "Weak", "Moderate", "Strong", "Very strong"]
response = client.system_one(
    state=pitch,
    questions={
        dim: Score(instructions=f"Assess the {dim} of this business", criteria=levels)
        for dim in WEIGHTS
    },
)

total, confident = 0.0, True
for dim, weight in WEIGHTS.items():
    ans = response.answers[dim]
    total += weight * ans.score / (len(levels) - 1)
    confident &= ans.confidence >= MIN_CONFIDENCE
    print(f"{dim:>15}: {ans.score:.1f}/4 (confidence {ans.confidence:.2f}) x {weight}")

print(f"composite: {total:.2f} / 1.00 -> {'ACT' if confident else 'REVIEW (low confidence)'}")
