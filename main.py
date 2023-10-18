from pyrogram import Client

# Replace these values with your API ID, API Hash, and phone number.
api_id = "26936654"
api_hash = "bbe46e790306860d1fc901e65d3e5327"
phone_number = "+8801738230593"

# Create a Pyrogram client session and get the session string.
with Client("my_bot", api_id, api_hash, phone_number) as app:
    session_string = app.export_session_string()
    print("Your Pyrogram Bot Session String:")
    print(session_string)
