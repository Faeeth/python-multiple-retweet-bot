import sys, getopt, json, tweepy

def print_usage():
    print ("twitterbotretweet.py -i <id> -b <bot>")

def main(argv):
   idd = ''
   bot = '0'
   y = 0
   try:
      opts, args = getopt.getopt(argv,"hi:b:",["id","bot="])
   except getopt.GetoptError:
     print_usage()
     print (args) #Debug
     sys.exit(2)
   if not opts:
     print_usage()
     sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("twitterbotretweet.py -i <id> -b <bot>")
         sys.exit()
      elif opt in ("-i","--id"):
         if idd:
            print("You can't use url AND id at the same time")
            sys.exit(2)
         idd = arg
         if idd.isdigit() == False:
            print("Id value after -i must be Integer")
            sys.exit(2)
      elif opt in ("-b","--bot"):
         bot = arg
         if bot.isdigit() == False:
            print("Bot value after -b must be Integer")
            sys.exit(2)
   if bot == '0':
      bot = '1'

   with open('acc.json') as json_file:
      data = json.load(json_file)
   CONSUMER_KEY_LIST = []
   CONSUMER_SECRET_LIST = []
   ACCESS_TOKEN_LIST = []
   ACCESS_TOKEN_SECRET_LIST = []
   for (k,v) in data.items(): # key / value
       CONSUMER_KEY_LIST.append(data[k]["CONSUMER_KEY"])
       CONSUMER_SECRET_LIST.append(data[k]["CONSUMER_SECRET"])
       ACCESS_TOKEN_LIST.append(data[k]["ACCESS_TOKEN"])
       ACCESS_TOKEN_SECRET_LIST.append(data[k]["ACCESS_TOKEN_SECRET"])
       if data[k]["CONSUMER_KEY"] and data[k]["CONSUMER_SECRET"] and data[k]["ACCESS_TOKEN"] and data[k]["ACCESS_TOKEN_SECRET"]:
         y = y + 1
   if int(bot) > y:
      print("You don't have enough accounts")
      print("Nb of accounts available : ",y)
      print("Nb of accounts chosen : ",bot)
      sys.exit(2)
   print ("id : ", idd)
   print ("bot : ", bot)
   for i in range(int(bot)):
      consumer_key = CONSUMER_KEY_LIST[i]
      consumer_secret = CONSUMER_SECRET_LIST[i]
      access_token = ACCESS_TOKEN_LIST[i]
      access_token_secret = ACCESS_TOKEN_SECRET_LIST[i]
      auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      auth.set_access_token(access_token, access_token_secret)
      api = tweepy.API(auth)
      ID = int(idd)
      api.retweet(ID)

if __name__ == "__main__":
    main(sys.argv[1:])
