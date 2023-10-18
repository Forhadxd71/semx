from pyrogram import Client

# Replace these with your own API ID, API Hash, and phone number
api_id = "26936654"
api_hash = "bbe46e790306860d1fc901e65d3e5327"
phone_number = "+8801738230593"

# Create a Pyrogram bot session
with Client(":memory:", api_id=api_id, api_hash=api_hash, phone_number=phone_number) as app:
    # Start the bot session to get the session string
    session_string = app.export_session_string()
    
# Save the session string to a file (e.g., session.txt)
with open("session.txt", "w") as file:
    file.write(session_string)

print("Session file created successfully.")
