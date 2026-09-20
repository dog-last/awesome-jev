"""03 — RAG reranking: score candidate chunks, keep the useful ones.

Score each candidate against the query, sort by score, and drop anything
the model is unsure about. Cheap enough to run on every retrieval.

Run:  uv run 03_rag_rerank.py
"""

# /// script
# requires-python = ">=3.10"
# dependencies = ["typesafe-sdk>=0.7.0", "python-dotenv>=1.0", "httpx2>=2.13"]
# ///

from typesafe_sdk import Score

from common import make_client

client = make_client()

query = "How do I rotate my API keys?"
candidates = [
    "To rotate an API key, open Settings > Developers, click 'Rotate', and deploy the new key within 24h.",
    "Our pricing starts at $20/month for the basic plan, with volume discounts available.",
    "Old API keys are revoked automatically 24 hours after a rotation is initiated.",
]

for chunk in candidates:
    response = client.system_one(
        state=f"Query: {query}\n\nDocument chunk: {chunk}",
        questions={
            "relevance": Score(
                instructions="How useful is this chunk for answering the query",
                criteria=["Irrelevant", "Tangentially related", "Directly answers the query"],
            )
        },
    )
    ans = response.answers["relevance"]
    print(f"score={ans.score:.1f} confidence={ans.confidence:.2f} | {chunk[:60]}...")
