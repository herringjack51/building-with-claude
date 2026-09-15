"""Send one message to Claude and print the reply.

Requires an ANTHROPIC_API_KEY, either set as an environment variable or
in a .env file in this folder (see .env.example).
"""

import anthropic
from dotenv import load_dotenv

# Reads any KEY=value lines out of a .env file in the current directory
# and loads them as environment variables. If there's no .env file, this
# just does nothing (it won't error).
load_dotenv()


def main() -> None:
    # Anthropic() reads your API key from the ANTHROPIC_API_KEY environment
    # variable automatically, so we never write the key itself into the code.
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "In one sentence, what is the Claude API?"}
        ],
    )

    # response.content is a list of content blocks (usually just one, of
    # type "text", for a simple request like this) — we grab the text out.
    for block in response.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()
