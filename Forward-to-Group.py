import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from moviepy.video.io.VideoFileClip import VideoFileClip

app = Client("my_bot", api_id=3910389, api_hash="86f861352f0ab76a251866059a6adbd6", bot_token="6094352096:AAEXAgqJ7nZ0u1c-4mPanbipduiCbcwB8Kk")

@app.on_message(filters.video)
def cut_video(client, message):
    chat_id = message.chat.id
    video_path = client.download_media(message=message)
    video = VideoFileClip(video_path)
    cut_video = video.subclip(0, 15)
    cut_video_path = f"{chat_id}.mp4"
    cut_video.write_videofile(cut_video_path)
    caption = "# មើល Video នេះ Full តាម Bots\nរក្សាសិទ្ធដោយ @JVPCAMBODIAI_BOT"

    buttons = [
        [InlineKeyboardButton("📺របៀបចូលមើលរឿង", url="t.me/tech"), InlineKeyboardButton("មើលរឿងពេញតាម Bots🔞", url="t.me/JVPCAMBODIAI_Bot")]
    ]

    group_id = 'Khmer289'
    client.send_video(chat_id=chat_id, video=cut_video_path, caption=caption, reply_markup=InlineKeyboardMarkup(buttons))
    client.send_video(chat_id=group_id, video=cut_video_path, caption=caption, reply_markup=InlineKeyboardMarkup(buttons))

    os.remove(video_path)
    os.remove(cut_video_path)

app.run()