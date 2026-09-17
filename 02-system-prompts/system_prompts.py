import anthropic
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic()

system_prompts = ["You are a terse subject-matter expert. Answer in at most two sentences. Get straight to the point, no hedging or extra pleasantries." ,"You are a patient teacher explaining this to a beginner. Use a simple analogy, and make sure your explanation would actually make sense to someone new to the topic." , "You are a skeptical reviewer. Push back on the question with some counterarguments first, then answer it in a few sentences."]

for prompt in system_prompts:
    response = client.messages.create(
    model = "claude-sonnet-5",
    max_tokens = 1024,
    system = prompt,
    messages = [{"role" : "user", "content" : "was 9/11 actually carried out by the middle east"}]
)

    print(prompt)

    for block in response.content :
        if block.type == "text" :
            print(block.text)
