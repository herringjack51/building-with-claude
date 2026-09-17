# Vocabulary

A running glossary of terms and concepts, added to after each session. Newest
sessions are added at the bottom.

## Phase 1 — Setup & Orientation

- **import** — brings an outside library into your script so you can use it
  (e.g. `import anthropic`). Goes at the top of the file.
- **client** — an object that holds your connection/credentials to an API.
  Created once (`client = anthropic.Anthropic()`), then reused for every
  request instead of recreating it each time.
- **environment variable** — a value stored in your terminal/shell session
  (or a container), readable by any program running there, without being
  written into your code. `ANTHROPIC_API_KEY` is one.
- **`.env` file / `load_dotenv()`** — a way to store environment variables in
  a file on disk instead of typing `export` every time. `load_dotenv()`
  reads that file and loads its `KEY=value` lines as environment variables.
  The `.env` file itself should always be gitignored, never committed.
- **keyword argument** (`name=value`) — inside a function call, this fills in
  one of that function's predefined, labeled inputs. The label (`model`,
  `max_tokens`, `messages`, `system`) is fixed by whoever wrote the function
  — you don't invent it, you just supply the value.
- **`model`** — which Claude model handles the request (e.g.
  `"claude-sonnet-5"`).
- **`max_tokens`** — a hard ceiling on how long the reply can be. It's a
  limit, not a target — hitting it cuts the reply off mid-thought instead of
  shortening it cleanly.
- **`messages`** — a list of dictionaries representing the conversation.
  Each dictionary has a `"role"` (`"user"` or `"assistant"`) and `"content"`
  (the actual text).
- **`response.content`** — the reply comes back as a *list* of content
  blocks (not a plain string), since a response can in principle contain
  more than one kind of content. Each block has a `.type` (e.g. `"text"`)
  and, for text blocks, a `.text`.
- **`stop_reason`** — tells you *why* the model stopped generating (e.g.
  `"end_turn"` vs. `"max_tokens"`), useful for detecting truncation in code.

## Phase 2, Session 1 — System Prompts

- **`system`** — a separate top-level field (not part of `messages`) that
  sets Claude's standing behavior/persona for the whole request — *how* to
  respond, as opposed to `messages`, which is *what* is actually being
  asked.
- **list** (`[ ]`) — an ordered collection of items, separated by commas.
- **dictionary** (`{ }`) — a collection of `"key": value` pairs. Brackets
  nest and must close in the reverse order they opened (e.g. a dict inside
  a list closes `}]`, not `]}`).
- **`for` loop** — repeats a block of code once for every item in a list:
  `for item in some_list:`. The loop variable (`item`, or whatever name you
  pick) takes on a different value from the list each pass, automatically —
  you don't need to index into the list yourself (no `some_list[0]` needed).
- **`if` statement** — runs a block of code only when a condition is true:
  `if condition:`.
- **`==` vs. `=`** — `==` asks "is this equal to that?" (a comparison, used
  in conditions); `=` means "store this value" (assignment). Mixing them up
  is one of the most common beginner bugs.
- **indentation** — Python uses spaces (not `{ }` or `end`) to mark what
  code is "inside" a loop/if/function. Each level of nesting adds 4 more
  spaces. Lines inside an *open* `( )` or `[ ]` are an exception — Python
  ignores their indentation since it already knows the statement continues
  until the matching closing bracket.
- **trailing commas in function calls** — every keyword argument inside a
  function call needs a comma after it, except the very last one — even
  when each argument is on its own line.
