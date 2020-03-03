from fbchat import log, Client
import random	
import getpass
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

#response = ''
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        
        if author_id != self.uid:
        	chatbot = ChatBot("*Your name*")
        	chatbot.set_trainer(ChatterBotCorpusTrainer)
        	chatbot.train("chatterbot.corpus.english")
        	received = chatbot.get_response(message_object.text)
	        message_object.text = received
	        self.send(message_object, thread_id=thread_id, thread_type=thread_type)
	        	


email = input('Email:')
password = getpass.getpass()


client.listen()
