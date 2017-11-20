#https://github.com/python-telegram-bot/python-telegram-bot
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#post-a-text-message
#https://core.telegram.org/bots/api#sendmessage
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



class telegram_bot(object):
	"""docstring for telegram_bot"""
	def __init__(self, token, chat_id):
		self.updater = Updater(token = token)
		self.dispatcher = self.updater.dispatcher
		self.start_handler = CommandHandler('start', self.start)
		self.info_handler = CommandHandler('info', self.info)
		self.echo_handler = MessageHandler(Filters.text, self.echo)
		self.dispatcher.add_handler(self.start_handler)
		self.dispatcher.add_handler(self.echo_handler)
		self.dispatcher.add_handler(self.info_handler)
		self.updater.start_polling()
		self.id = chat_id

	def start(self, bot, update):
		self.reply1 = "Hola, todavia no se hacer mucho (ni siquiera se que todavia va con tilde)"
		bot.send_message(chat_id=update.message.chat_id, text=reply1)

	def info(self, bot, update):
		self.reply2 = "Este comando deberia darte informacion sobre las monedas"
		bot.send_message(chat_id=update.message.chat_id, text=reply2)

	def echo(self, bot, update):
		bot.send_message(chat_id=update.message.chat_id, text='No se responder, sorry bro')

	def send_text(self, data):
		self.updater.bot.send_message(chat_id= self.id, text=data) #mi id

	def send_photo(self, addrs):
		self.updater.bot.send_photo(chat_id=self.id, photo=open(addrs, 'rb')) #mi id






