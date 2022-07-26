#string concatention (aka how to put strings together)
# create a string that says "subscribe to ____-"
youtuber = "Justin Chau" #some string variable

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
celebrity = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {celebrity}!"

print(madlib)
