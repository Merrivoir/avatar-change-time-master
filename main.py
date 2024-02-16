from telethon import TelegramClient, sync, errors
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
import time
from config import *
from generate_time_images import *

client = TelegramClient('chgTime', api_id, api_hash, system_version="1.1")
client.start()

while True:
    change_img()
    photo = client.upload_file(f"time.png")
    try:
        client(UploadProfilePhotoRequest(file=photo))
    except errors.FloodWaitError as e:
        time.sleep(e.seconds)
        print(e.seconds)
    time.sleep(59)
    client(DeletePhotosRequest(client.get_profile_photos('me')))

if __name__ == '__main__':
	pass
