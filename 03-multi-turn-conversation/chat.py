# bring in the Anthropic SDK so we can talk to the Claude API
import anthropic
# bring in load_dotenv so we can read the API key out of a .env file
from dotenv import load_dotenv
# actually read the .env file and load ANTHROPIC_API_KEY into the environment
load_dotenv()
# create the client object we'll use to send every request below
client = anthropic.Anthropic()

# the running conversation: starts empty, grows by one entry per turn
conversation_history = []

# repeat forever, one turn per loop, until the user types "quit"
while True:
    # wait for the user to type something and hit Enter
    user_input = input("You:  ")

    # if they want to leave, stop the loop immediately
    if user_input == "quit" :
        break

    # add the user's message to the running history
    conversation_history.append({"role" : "user" , "content" : user_input})

    # send the ENTIRE history so far (not just this one message) to Claude
    response = client.messages.create(model = "claude-sonnet-5", max_tokens = 1024, messages = conversation_history)

    # go through the reply's content blocks and find the text one(s)
    for block in response.content:
        if block.type == "text" :
            # add Claude's own reply back into the history too, so it can
            # see what it said next time we send the history again
            conversation_history.append({"role" : "assistant", "content" : block.text})
            # show the reply to the user
            print(block.text)
