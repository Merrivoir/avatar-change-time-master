from telethon import TelegramClient, sync, errors
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
import time
from config import *
from generate_time_images import *
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", format="%(asctime)s %(levelname)s %(message)s")

client = TelegramClient('chgTime', api_id, api_hash, system_version="1.1")
client.start()

while True:
    change_img()
    photo = client.upload_file(f"time.png")
    try:
        client(UploadProfilePhotoRequest(file=photo))
        logging.info(f"Фото загружено")
        time.sleep(300)
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        logging.info(f"Фото удалено")
    except errors.FloodWaitError as e:
        print(e.seconds)
        logging.info(f"Ошибка флуда: необходимо подождать {e.seconds} секунд.")
        time.sleep(e.seconds)
    

if __name__ == '__main__':
	pass
