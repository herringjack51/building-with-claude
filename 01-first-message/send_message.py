"""Send one message to Claude and print the reply.

Requires the ANTHROPIC_API_KEY environment variable to be set.
"""

import anthropic


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
