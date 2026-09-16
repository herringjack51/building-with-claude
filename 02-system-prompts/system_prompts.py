"""Compare how a system prompt changes Claude's reply to the same question.

The `system` parameter sets Claude's role/behavior for the whole
conversation — it's separate from the `messages` list, and never
counts as something Claude "said" or the user "asked." Here we hold
the user's question fixed and swap out only the system prompt, to see
how much of the reply's tone and shape comes from that one field.

Requires an ANTHROPIC_API_KEY, either set as an environment variable or
in a .env file in this folder (see .env.example).
"""

import anthropic
from dotenv import load_dotenv

load_dotenv()

USER_QUESTION = "Should I learn to code in 2026, now that AI can write code?"

PERSONAS = {
    "Terse expert": (
        "You are a terse subject-matter expert. Answer in at most two "
        "sentences. No hedging, no pleasantries, no follow-up questions."
    ),
    "Patient teacher": (
        "You are a patient teacher explaining this to someone new to the "
        "topic. Use a simple analogy, and check that your explanation "
        "would make sense to a beginner."
    ),
    "Skeptical reviewer": (
        "You are a skeptical reviewer. Assume the premise in the question "
        "might be flawed, point out what it's missing, and push back "
        "before giving your own take."
    ),
}


def ask(client: anthropic.Anthropic, system_prompt: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": USER_QUESTION}],
    )
    # Concatenate all text blocks in case the reply spans more than one.
    return "".join(block.text for block in response.content if block.type == "text")


def main() -> None:
    client = anthropic.Anthropic()

    print(f'Question: "{USER_QUESTION}"\n')
    for name, system_prompt in PERSONAS.items():
        reply = ask(client, system_prompt)
        print(f"--- {name} ---")
        print(f"[system: {system_prompt}]\n")
        print(reply)
        print()


if __name__ == "__main__":
    main()
