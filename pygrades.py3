#! /usr/bin/python3
from flask import Flask, request
from pymessenger.bot import Bot
import random

app = Flask(__name__)
ACCESS_TOKEN = 'EAAEYCy6sKrIBANZCPNBQcljqsD4S7HO6r1ESvJAifmSRqWBJCxXwdesqn8TZAYtXTOjZC6DqZCvMVjWfppxCMBm96EafHynoRNLZBJJUwquSFZCSiweBO0PKjncBxx3ZBJBq5Q4fhvSak58Yvu17BUe9elnp9FkG1fAVsLygV1ShQZDZD'
VERIFY_TOKEN = 'REHAM_NOUR'
bot = Bot(ACCESS_TOKEN)

@app.route('/pygrades', methods=['GET', 'POST'])
def retreive_data():
	if request.method == 'GET':

		token_sent = request.args.get("hub.verify_token")
		return verify_fb_token(token_sent)
	else:
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):
					recipient_id = message['sender']['id']
					if message['message'].get('text'):
						response_sent_text = get_message()
						send_message(recipient_id, response_sent_text)
					elif message['message'].get('attachments'):
						response_sent_nontext = get_message()
						send_message(recipient_id, response_sent_nontext)
	return "Message Sent"

def verify_fb_token(token_sent):
	if token_sent == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Ivalid verification token'

def send_message(recipient_id, response):
	bot.send_text_message(recipient_id, response)
	return "success" 

def get_message():

	sample_responses =  ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    
    return random.choice(sample_responses)


if __name__ == '__main__':
	app.run()
