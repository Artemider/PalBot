from PIL import Image, ImageDraw, ImageFont
import os

from user.Midllvary import rate_limit, ThrottlingMiddleware
from create_bot import bot, dp
from config import ignore

from aiogram import types, executor, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
import random

# Commands "Start"
@rate_limit(5, 'pall')
async def pall(message: types.Message):

	user_id = str(message.from_user.id)
	username = message.from_user.username
	first_name = message.from_user.first_name
	chat_id = str(message.chat.id)
	chat_name = message.chat.title

	markup = InlineKeyboardMarkup()
	button = InlineKeyboardButton(text="3", callback_data='btn1')
	button1 = InlineKeyboardButton(text="4", callback_data='btn2')
	markup.add(button, button1)

	await message.reply("Оберіть кількість кольорів", reply_markup=markup)

#Button1
@dp.callback_query_handler(text = 'btn1')
@rate_limit(3, 'btn1')
async def but2(callback_query: types.CallbackQuery):
	
	chat_id = callback_query.message.chat.id

	# Розміри зображення
	width = 900
	height = 300
	
	# Розміри та положення частин зображення
	part_width = width // 3
	part_height = height
	part1_box = (0, 0, part_width, part_height)
	part2_box = (part_width, 0, part_width * 2, part_height)
	part3_box = (part_width * 2, 0, width, part_height)
	
	# Створення зображення та об'єкта для малювання
	image = Image.new("RGB", (width, height))
	draw = ImageDraw.Draw(image)
	
	# Генерація кожної частини зображення
	for part_box in [part1_box, part2_box, part3_box]:
		# Вибір рандомного кольору фону    
		bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		draw.rectangle(part_box, fill=bg_color)
		# Визначення кольору тексту в залежності від яскравості фону    
		brightness = (bg_color[0] * 299 + bg_color[1] * 587 + bg_color[2] * 114) / 1000
		if brightness < 128:
			text_color = (255, 255, 255)  # Якщо фон темний, то текст світлий
		else:
			text_color = (0, 0, 0)  # Якщо фон світлий, то текст темний
		# Запис назви кольору на зображення
		text = f"RGB({bg_color[0]},{bg_color[1]},{bg_color[2]})"    
		font = ImageFont.truetype("arial.ttf", 16)
		text_width, text_height = draw.textsize(text, font=font)    
		text_position = ((part_box[2] - part_box[0] - text_width) // 2, (part_box[3] - part_box[1] - text_height) // 2)
		draw.text((part_box[0] + text_position[0], part_box[1] + text_position[1]), text, font=font, fill=text_color)
	# Збереження зображення
	name = str(random.randint(100000, 999999))+"_img.png"
	image.save(name)

	url_photo = open(name, 'rb')
	await bot.send_photo(chat_id=chat_id, photo=url_photo)
	os.remove(name)

#Button2
@dp.callback_query_handler(text = 'btn2')
@rate_limit(3, 'btn2')
async def but2(callback_query: types.CallbackQuery):
	
	chat_id = callback_query.message.chat.id

	# Розміри зображення
	width = 750
	widt = 1000
	height = 300
	
	# Розміри та положення частин зображення
	part_width = width // 3
	part_height = height
	part1_box = (0, 0, part_width, part_height)
	part2_box = (part_width, 0, part_width * 2, part_height)
	part3_box = (part_width * 2, 0, width, part_height)
	part4_box = (width, 0, part_width * 4, part_height)
	
	# Створення зображення та об'єкта для малювання
	image = Image.new("RGB", (widt, height))
	draw = ImageDraw.Draw(image)
	
	# Генерація кожної частини зображення
	for part_box in [part1_box, part2_box, part3_box, part4_box]:
	    # Вибір рандомного кольору фону
	    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	    draw.rectangle(part_box, fill=bg_color)
	
	    # Визначення кольору тексту в залежності від яскравості фону
	    brightness = (bg_color[0] * 299 + bg_color[1] * 587 + bg_color[2] * 114) / 1000
	    if brightness < 128:
	        text_color = (255, 255, 255)  # Якщо фон темний, то текст світлий
	    else:
	        text_color = (0, 0, 0)  # Якщо фон світлий, то текст темний
	
	    # Запис назви кольору на зображення
	    text = f"RGB({bg_color[0]},{bg_color[1]},{bg_color[2]})"
	    font = ImageFont.truetype("arial.ttf", 16)
	    text_width, text_height = draw.textsize(text, font=font)
	    text_position = ((part_box[2] - part_box[0] - text_width) // 2, (part_box[3] - part_box[1] - text_height) // 2, (part_box[3] - part_box[2] - text_height) // 2)
	    draw.text((part_box[0] + text_position[0], part_box[1] + text_position[1], part_box[2] + text_position[2]), text, font=font, fill=text_color)
	
	# Збереження зображення
	name = str(random.randint(100000, 999999))+"_img.png"
	image.save(name)

	url_photo = open(name, 'rb')
	await bot.send_photo(chat_id=chat_id, photo=url_photo)
	os.remove(name)



'''*******************************************start*****************************************************************'''

def register_handlers_user(dp : Dispatcher):

	#Code
	dp.register_message_handler(pall, commands=["pall"])