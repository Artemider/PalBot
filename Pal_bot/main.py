from create_bot import bot, storage, dp
from user.Midllvary import rate_limit, ThrottlingMiddleware

from user.user import register_handlers_user

import asyncio
from aiogram import Bot, Dispatcher, types, executor

import datetime

'''*******************************************start*****************************************************************'''

register_handlers_user(dp)

'''*******************************************init*****************************************************************'''

if __name__ == '__main__':
	# Setup middleware
	dp.middleware.setup(ThrottlingMiddleware())

	# Start long-polling
	executor.start_polling(dp, skip_updates=True)