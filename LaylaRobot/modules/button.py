from telethon import events, Button, client
from LaylaRobot import DEV_USERS

@bot.on(
    events.NewMessage(pattern="^/skem ?(.*)")
)
async def _(event):
  if event.sender_id in DEV_USERS:
      text = event.pattern_match.group(1)
      k = [[Button.text(text)]]
      await BotzHub.send_message(event.chat_id, "😈", buttons=k)
  else:
      await event.reply("**BHAI YAAR THUM GAAND MARAO**")
