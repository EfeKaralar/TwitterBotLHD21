import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
tweet = "Day %s of MLH Local Hack Day: Share!\n@MLHacks\n#LocalHackDay"

day = 0

while day != 3:
    
    day = datetime.date.day

    if day == 29:
        api.update_status(tweet%'1')

    if day == 30:
        api.update_status(tweet%'2')
    if day == 31:
        api.update_status(tweet%'3')
    if day == 1:
        api.update_status(tweet%'4')
    if day == 2:
        api.update_status(tweet%'5')

    time.sleep(86400)
    print("All done! for today")

print("All done!")


