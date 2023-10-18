from pyrogram import Client
from pyrogram.api.errors import FloodWait

# Replace these with your own values
api_id = "26936654"
api_hash = "bbe46e790306860d1fc901e65d3e5327"
phone_number = "+8801738230593"

# Create a Pyrogram client
app = Client(
    "forhadxn",
    api_id=api_id,
    api_hash=api_hash,
    phone_number=phone_number,
)

async def main():
    await app.start()
    me = await app.get_me()
    print(f"Logged in as {me.username} ({me.id})")

    # Save the session to a file
    app.export_session("session.txt")

    await app.send_message(
        "me",  # Replace with the recipient's username or ID
        "Bot session created and saved.",
    )

    await app.stop()

if __name__ == "__main__":
    with app:
        app.loop.run_until_complete(main())
