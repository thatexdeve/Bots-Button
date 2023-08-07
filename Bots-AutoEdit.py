import random
import asyncio

from telethon import TelegramClient, events

# Define the API ID and hash for the TelegramClient
api_id = 3910389
api_hash = "86f861352f0ab76a251866059a6adbd6"

# Create a TelegramClient instance
client = TelegramClient('session', api_id, api_hash)

# Define the source channels and the target group
source_channels = ['zzzonlyfans', 'zzzhub00','SV983']
target_group = '@EditorJVPBOT'

# Define a function to forward a random video from a source channel
async def forward_random_video():
    # Get all the messages from a random source channel
    messages = await client.get_messages(random.choice(source_channels), limit=100)
    # Filter out the messages that are videos
    videos = [m for m in messages if m.video]
    # Choose a random video from the list
    video = random.choice(videos)
    # Forward the video to the target group
    await client.forward_messages(target_group, video)

# Define a function to run the forward_random_video function every 2 minutes
async def run_every_2_minutes():
    while True:
        # Call the forward_random_video function
        await forward_random_video()
        # Wait for 2 minutes (120 seconds)
        await asyncio.sleep(700)

# Start the client and run the run_every_2_minutes function
with client:
    client.loop.run_until_complete(run_every_2_minutes())