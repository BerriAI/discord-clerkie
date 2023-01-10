import os
import discord
import requests

client = discord.Client(intents=discord.Intents.all())
base_url = "https://clerkieserverchromeextensionv1.krrishdholakia.repl.co/"

def handle_request(error_msg, user_id):
    response = requests.get(base_url + "/discord", params={"user_query": error_msg, "user_id": user_id})
    # Check the status code of the response
    if response.status_code == 200:
        # Print the response body
        clerkie_resp = response.json()["response"]
        return response.json()["response"]
    else:
        return "error from server"

def get_error(message):
    return message.replace("!clerkie", "")

@client.event
async def on_message(message):
    # if the message is from the bot itself, ignore it
    if message.author == client.user:
        return

    if message.content.startswith('!clerkie'):
        print(message.content)
        user_query = get_error(message.content)
        response = f"Hi {message.author} here is your response:" + handle_request(user_query, message.author)
        await message.reply(response)

my_secret = os.environ['DISCORD_TOKEN']
client.run(my_secret)