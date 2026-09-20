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

## Phase 2, Session 2 — Multi-turn Conversations

- **stateless** — the API has no memory of its own between requests. Every
  call to `client.messages.create(...)` is completely independent; Claude
  doesn't "remember" anything from an earlier request unless you resend it
  yourself as part of `messages`.
- **conversation history** — a list you build and grow yourself (starting
  empty: `history = []`), holding every user and assistant turn so far. You
  resend the *whole* list on every request (`messages=history`) — that's
  what makes it look like Claude "remembers" the conversation, when really
  your code is just showing it everything again each time.
- **`.append(item)`** — a method every list has built in, used to add one
  new item onto the end of an existing list (`history.append({...})`).
  Different from creating a list with items already in it (`[a, b, c]`) —
  this adds to a list that already exists, one item at a time.
- **`while True:`** — a loop that repeats forever, unlike `for`, which stops
  after going through a fixed list. Used when you don't know in advance how
  many times something needs to run (like a chat that continues until the
  user decides to quit).
- **`break`** — immediately exits the loop it's inside, skipping any
  remaining code in that loop, and continues with whatever comes after it.
- **`input(...)`** — a built-in function that pauses the program, waits for
  someone to type something and press Enter, and returns what they typed as
  a string. The text passed to it (e.g. `input("You: ")`) is shown as a
  prompt right before the cursor.
- **method vs. function call** — `input(...)` and `client.messages.create(...)`
  are both "calls," but `.append(...)` is specifically a *method*: an action
  that belongs to a particular object (here, a list) and is called with a
  dot, `object.method(...)`, rather than standing alone.

## Phase 2, Session 3 — Vision (Images)

- **`content` as a list of blocks** — up to now, `"content"` in a message has
  always been a plain string. To send an image alongside text, `"content"`
  becomes a *list* holding multiple blocks instead — one describing the
  image, one describing the text question — so a single turn can carry more
  than one kind of thing at once.
- **image block** — `{"type": "image", "source": {...}}`, one item inside a
  `content` list. Its `"source"` is itself a nested dictionary describing
  *where* the image data comes from.
- **`source` types: `"url"` vs. `"base64"`** — `"url"` points to an image
  already hosted online (`{"type": "url", "url": "https://..."}`) — no file
  reading needed. `"base64"` is for a local image file: you read its raw
  bytes and encode them as text so they can travel inside a JSON request.
  URL is simpler when the image is already online; base64 is needed for a
  file that only exists on your own disk.
- **why the reply is still `"text"` only** — Claude describes an image in
  words; it doesn't send an image back. So when reading `response.content`,
  only `"text"` blocks ever show up here, even though the *request* you sent
  contained an `"image"` block.
