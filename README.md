# Building with Claude

This is my personal repo for a course where I'm learning to build applications
with the [Claude API](https://docs.claude.com/) (Anthropic's SDK). Each
numbered folder is a small, self-contained exercise from the course.

## Exercises

- [`01-first-message/`](./01-first-message) — the "hello world" of the Claude
  API: send one message, print the reply.
- [`02-system-prompts/`](./02-system-prompts) — same question, three
  different `system` prompts (terse expert, patient teacher, skeptical
  reviewer), to compare how much tone/shape comes from that one field.
- [`03-multi-turn-conversation/`](./03-multi-turn-conversation) — a CLI
  chat loop that proves the API is stateless: it resends the whole
  conversation history on every turn so Claude "remembers" earlier turns.
- [`04-vision/`](./04-vision) — sends an image (via URL) alongside a text
  question, and asks Claude to describe what's in it.
- [`05-streaming/`](./05-streaming) — the p2s2 chatbot, upgraded to stream
  the reply piece by piece (`client.messages.stream(...)`) instead of
  waiting for the whole thing.

## Setup

Each exercise has its own `requirements.txt`. From the exercise folder:

```bash
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

You'll also need an Anthropic API key set as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

See the exercise's own README/comments for how to get a key and run the
script.

More exercises will be added here as the course progresses.
