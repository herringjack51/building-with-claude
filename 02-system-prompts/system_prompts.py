# bring in the Anthropic SDK so we can talk to the Claude API
import anthropic
# bring in load_dotenv so we can read the API key out of a .env file
from dotenv import load_dotenv
# actually read the .env file and load ANTHROPIC_API_KEY into the environment
load_dotenv()
# create the client object we'll use to send every request below
client = anthropic.Anthropic()

# three different system prompts (personas) to compare against the same question
system_prompts = ["You are a terse subject-matter expert. Answer in at most two sentences. Get straight to the point, no hedging or extra pleasantries." ,"You are a patient teacher explaining this to a beginner. Use a simple analogy, and make sure your explanation would actually make sense to someone new to the topic." , "You are a skeptical reviewer. Push back on the question with some counterarguments first, then answer it in a few sentences."]

# go through each persona one at a time, using it as the system prompt
for prompt in system_prompts:
    # send the request: same question every time, only "system" changes
    response = client.messages.create(
    model = "claude-sonnet-5",
    max_tokens = 1024,
    system = prompt,
    messages = [{"role" : "user", "content" : "was 9/11 actually carried out by the middle east"}]
)

    # print which persona this reply belongs to, so we can tell them apart
    print(prompt)

    # response.content is a list of blocks; find the text block(s) and print them
    for block in response.content :
        if block.type == "text" :
            print(block.text)
