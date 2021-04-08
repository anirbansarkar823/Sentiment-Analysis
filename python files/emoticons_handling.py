# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:06:07 2019

@author: Enter My World


"""
tweet = ":L :-) :3 =] :@ :"
print(tweet)
import re
#for cleaning the tweets
#import preprocessor as p
#clean_text = p.clean(tweet)
#removing urls(http:..) 

twt = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', tweet)


#HappyEmoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])


# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])


#Emoji patterns
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)



#replacing emojis
for emoji in emoticons_happy:
    tweet = tweet.replace(emoji,'happy')

for emoji in emoticons_sad:
    tweet = tweet.replace(emoji,'sad')

#combine sad and happy emoticons

#emoticons = emoticons_happy.union(emoticons_sad)

#after tweepy preprocessing the colon symbol left remain after      #removing mentions
tweet = re.sub(r':', '', tweet)
tweet = re.sub(r'‚Ä¶', '', tweet)
#replace consecutive non-ASCII characters with a space
tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)

#remove emojis from tweet
tweet = emoji_pattern.sub(r'', tweet)

print(tweet)

