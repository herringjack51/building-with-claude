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
while True :
    # wait for the user to type something and hit Enter
    user_input = input("You:  ")

    # if they want to leave, stop the loop immediately
    if user_input == "quit" :
        break

    # add the user's message to the running history
    conversation_history.append({"role": "user" , "content" : user_input})

    # this will hold the complete reply, built up piece by piece as it streams in
    conversation_stream = ""

    # open a streaming connection; "as stream" gives us a live handle to it
    with client.messages.stream (
    model = "claude-sonnet-5",
    max_tokens = 1024,
    messages = conversation_history
    ) as stream :

        # each pass through this loop gives us the next small chunk of text,
        # as Claude generates it, instead of waiting for the whole reply
        for text in stream.text_stream :

            # end="" keeps chunks on the same line; flush=True shows it immediately
            print(text, end="", flush = True)
            # add this chunk onto the full reply we're building up
            conversation_stream += text

    # a newline so the next "You: " prompt doesn't run into the last chunk
    print()

    # now that streaming is fully done, save the complete reply into history
    conversation_history.append({"role": "assistant" , "content" : conversation_stream})
