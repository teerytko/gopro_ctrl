import sys
import logging
import asyncio
import requests
import json
from pathlib import Path
import cv2

from open_gopro.gopro_wired import WiredGoPro
from open_gopro.logger import setup_logging

GOPRO_BASE_URL = "http://10.5.5.9:8080"
GOPRO_STREAM_URL = "udp://@0.0.0.0:8554"


logger = setup_logging(__name__, Path("my_log.log"))

def restart_preview():
    # Build the HTTP GET request
    url = GOPRO_BASE_URL + "/gopro/camera/stream/stop"
    logger.info(f"Stopping the preview stream: sending {url}")

    # Send the GET request and retrieve the response
    response = requests.get(url, timeout=10)
    # Check for errors (if an error is found, an exception will be raised)
    response.raise_for_status()
    logger.info("Command sent successfully")
    # Log response as json
    logger.info(f"Response: {json.dumps(response.json(), indent=4)}")

    # Build the HTTP GET request
    url = GOPRO_BASE_URL + "/gopro/camera/stream/start"
    logger.info(f"Starting the preview stream: sending {url}")

    # Send the GET request and retrieve the response
    response = requests.get(url, timeout=10)
    # Check for errors (if an error is found, an exception will be raised)
    response.raise_for_status()
    logger.info("Command sent successfully")
    # Log response as json
    logger.info(f"Response: {json.dumps(response.json(), indent=4)}")


async def main() -> None:
    # Put our code here
    gopro = WiredGoPro()
    await gopro.open()
    print("Yay! I'm connected via USB, Wifi, opened, and ready to send / get data now!")
    restart_preview()
    cap = cv2.VideoCapture(GOPRO_STREAM_URL,cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print('VideoCapture not opened')
        exit(-1)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('frame empty')
            break

        cv2.imshow('image', frame)

        if cv2.waitKey(1)&0XFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:  # pylint: disable=broad-exception-caught
        logging.error(e)
        sys.exit(-1)
    else:
        sys.exit(0)
    