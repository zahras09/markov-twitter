import os
import twitter

api = twitter.Api(
    consumer_key=os.environ["YeEHNPQVhfQA51HtPHiDABEci"]
    consumer_secrete=os.environ["o8EduEqaShggQfrTTvnzvhznHFUbDCiHislbpiqSuUEkAaZRBJ"]
    access_token_key=os.environ["753366326928744448-XX9pZQ0QXEbrEjai9JnHXo9yMYra8hL"]
    access_token_secrete=os.environ["afucqeigSrn94GtdotE111o91SNHf4vNxSpzL03axFCaB"])

print api.VarifyCredentials()

status = api.PostUpdate("your tweet goes here.")
print status.text