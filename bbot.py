from email.mime import image
from PIL import Image, ImageDraw, ImageFont
from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime 


#token='5120681427:AAGXP4ot8jonWk-tjoIWS5QUKS8QrmD6FWM'
bot = Bot(token='5120681427:AAGXP4ot8jonWk-tjoIWS5QUKS8QrmD6FWM')

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hello, send me a code")

@dp.message_handler()
async def get_photo(message: types.Message):
    img = Image.open("TicketBase.jpg")
    width, height = img.width, img.height

    draw = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("FontPrice.ttf", 28)
    font2 = ImageFont.truetype("FontTime.ttf", 30)
    x, y = (width - 297, height- 1487)
    x1, y1 = (width - 767, height - 1760)   #767,1760
    x2, y2 = (width - 302, height - 1422)            
    text = message.text
    texttime = str(message.date)
    textdate = str(message.date)

    w, h = font1.getsize(text)
    w2, h2 = font2.getsize(texttime)
    draw.rectangle((300,y, x + w + 20, y + h), fill='white')
    draw.text((x + 1,y), text[0:1], fill=(66, 66, 66), font=font1)
    draw.text((x + 12,y), text[1:2], fill=(66, 66, 66), font=font1)
    draw.text((x + 29,y), text[2:3], fill=(66, 66, 66), font=font1)
    draw.text((x + 48,y), text[3:4], fill=(66, 66, 66), font=font1)
    draw.text((x + 64,y), text[4:5], fill=(66, 66, 66), font=font1)


    draw.rectangle((350,y2, x2 + 500, y2 + 50), fill='white')
    draw.text((x2,y2), textdate[8:10], fill=(66, 66, 66), font=font1)
    draw.text((x2+35,y2), textdate[5:7], fill=(66, 66, 66), font=font1)
    draw.text((x2+78,y2), textdate[0:4], fill=(66, 66, 66), font=font1)
    draw.text((x2+167, y2),textdate[11:13], fill=(66, 66, 66), font=font1)
    draw.text((x2+206, y2),textdate[14:16], fill=(66, 66, 66), font=font1)
    draw.text((x2+198,y2-3), ":", fill=(66,66,66), font=font1)
    draw.text((x2+26.5,y2), ".", fill=(66,66,66), font=font1)
    draw.text((x2+69,y2), ".", fill=(66,66,66), font=font1)

    #w2, h2 = font2.getsize(texttime)
    draw.rectangle((x1, y1, x1 + w2, y1 + h2), fill='white')
    draw.text((x1+40,y1-3), ":", fill=(0,0,0), font=font2)
    draw.text((x1,y1), texttime[11:13], fill=(0,0,0), font=font2)
    draw.text((x1+50,y1), texttime[14:16], fill=(0,0,0), font=font2)



    img.save('photo.jpg', format='JPEG', quality=75)
    #img.save("edited.jpg")
    
    await bot.send_photo(chat_id=message.chat.id, photo=open('photo.jpg', 'rb'))


       

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
