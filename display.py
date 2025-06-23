
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
from weatherScript import currentWeather
from notionCalendarScript import todaysEvents
from waveshareEPD import epd2in13_V4
import time

# === Fonts ===
fontPath = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
smallFont = ImageFont.truetype(fontPath, 16)
mediumFont = ImageFont.truetype(fontPath, 18)
largeFont = ImageFont.truetype(fontPath, 22)

# === Initialize e-ink display ===
epd = epd2in13_V4.EPD()
epd.init()
epd.Clear(0xFF)
width, height = epd.height, epd.width

# === Full Screen Drawing Function ===
def drawFullScreen():
    image = Image.new('1', (width, height), 255)
    draw = ImageDraw.Draw(image)

    now = datetime.now()
    dateStr = now.strftime("%A, %d %B")
    timeStr = now.strftime("%H:%M")

    # LEFT SIDE
    draw.text((2, 2), dateStr, font=largeFont, fill=0)
    draw.text((2, 28), f"Time: {timeStr}", font=mediumFont, fill=0)

    draw.text((2, 52), "Events:", font=smallFont, fill=0)
    y = 70
    events = todaysEvents()
    if not events:
        draw.text((4, y), "• None", font=smallFont, fill=0)
    else:
        for event in events[:3]:
            draw.text((4, y), f"• {event}", font=smallFont, fill=0)
            y += 16

    # RIGHT SIDE
    weatherStr = currentWeather()
    rightX = width - 110
    y = 28
    try:
        tempPart, rainPart = weatherStr.split("—")
    except ValueError:
        tempPart, rainPart = weatherStr, ""
    draw.text((rightX, y), tempPart.strip(), font=mediumFont, fill=0)
    y += 24
    draw.text((rightX, y), rainPart.strip(), font=smallFont, fill=0)

    epd.init()
    rotatedImage = image.rotate(180)
    epd.display(epd.getbuffer(rotatedImage))
    epd.sleep(3600)

    return rotatedImage

# === Partial Time Update Function ===
def updateTime(baseImage):
    now = datetime.now()
    timeStr = now.strftime("%H:%M")

    partialImage = baseImage.copy()
    draw = ImageDraw.Draw(partialImage)

    # Clear old time
    draw.rectangle((2, 28, 130, 50), fill=255)
    draw.text((2, 28), f"Time: {timeStr}", font=mediumFont, fill=0)

    try:
        epd.init_partial()
    except AttributeError:
        epd.init()
    epd.display(epd.getbuffer(partialImage.rotate()))
    epd.sleep(60)

# === Main Loop ===
if __name__ == "__main__":
    lastFullRefresh = datetime.now() - timedelta(hours=1)
    baseImage = drawFullScreen()

    while True:
        now = datetime.now()

        if (now - lastFullRefresh).total_seconds() >= 3600:
            baseImage = drawFullScreen()
            lastFullRefresh = now
            epd.sleep(3600)
        updateTime(baseImage)

        nextMinute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
        time.sleep((nextMinute - datetime.now()).total_seconds())
