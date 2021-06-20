import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)
from twilio.rest import Client

load_dotenv()
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"


TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client()

def get_sent_messages():
    # TODO: Make this return a collection of messages that were sent from the number
    messages = client.messages.list(from_=TWILIO_PHONE_NUMBER) # or limit=<some number, to limit number of msgs visible>

#     for record in messages:      this line of code print out list of all msgs in the top of complimenter app UI, which is visible from external surses as well. 
#         print(record.sid)
    # return messages
    # messages = []
    # return messages

def send_message(to, body):
    # TODO: Send the text message
    
     client.messages.create(
       to=to,
       body=body,
       from_=TWILIO_PHONE_NUMBER
       
    )


@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)

@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender', 'Someone')
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to = request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
