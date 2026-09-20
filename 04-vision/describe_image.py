# bring in the Anthropic SDK so we can talk to the Claude API
import anthropic
# bring in load_dotenv so we can read the API key out of a .env file
from dotenv import load_dotenv
# actually read the .env file and load ANTHROPIC_API_KEY into the environment
load_dotenv()

# create the client object we'll use to send the request
client = anthropic.Anthropic()

# one message, whose "content" is a list of two blocks: the image, then the
# text question about it -- both are read together as one combined turn
messages = [
{"role" : "user", "content" : [
    {"type" : "text" , "text" : "please describe what is going on in the picture"},
    {"type" : "image", "source" : {"type" : "url", "url" : "https://www.w3schools.com/w3images/lights.jpg"}
}
]
}
]

# send the request: model, a token ceiling, and our image+text message
response = client.messages.create(
    model = "claude-sonnet-5",
    max_tokens = 1024,
    messages = messages)

# response.content only contains text blocks here -- Claude describes the
# image in words, it doesn't send an image back
for block in response.content :
    if block.type == "text" :
        print(block.text)
