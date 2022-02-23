import random

playlists = ["Happy", "Love", "Sad", "Throwback", "Jazz",
             "Rock", "Instrumental", "Chill", "LoFi"]
Happy_playlist = ["Happy", "Love", "Chill", "Instrumental"]
Melancholy = ["Sad", "Lofi"]
Throwback = ["Throwback", "Jazz", "Rock"]
Relaxful = ["Jazz", "Instrumental", "Chill", "LoFi"]
day = ["Morning", "Afternoon", "Evening", "Night"]
weather = ["Sunny", "Cloudy", "Windy", "Rainy", "Foggy"]

name = input("Hello! What is your name? ")

user_input = input(f"Hi {name}! Are you going for a drive? \
'Y' for Yes or 'N' for No: \n").lower()
for parts_of_day in day:
    if user_input == 'y':
        user_input = input(f"How's the weather outside? \
Sunny, Foggy, Windy, Rainy, or Cloudy? ")
        if user_input == "Sunny":
            happy = random.choice(Happy_playlist)
            part_of_day = random.choice(day)
            print(f"The playlist you should listen to is {happy} \
this {part_of_day}")
        elif user_input == "Foggy":
            Relaxing = random.choice(Relaxful)
            part_of_day = random.choice(day)
            print(f"The playlist you should listen to is {Relaxing} \
this {part_of_day}")
        elif user_input == "Windy":
            Chillin = random.choice(Throwback + Melancholy)
            part_of_day = random.choice(day)
            print(f"The playlist you should listen to is {Chillin} \
this {part_of_day}")
        elif user_input == "Rainy":
            rainy_playlist = random.choice(Melancholy)
            part_of_day = random.choice(day)
            print(f"The playlist you should listen to is {rainy_playlist} \
this {part_of_day}")
        elif user_input == "Cloudy":
            cloudy_playlist = random.choice(Melancholy + Relaxful)
            part_of_day = random.choice(day)
            print(f"The playlist you should listen to is {cloudy_playlist} \
this {part_of_day}")
        else:
            print("That's not a proper response, I'll choose for you!")
            print(random.choice(playlists))
        Another = input("Did you want to try another playlist? \
(y/n)").lower()
        if Another == "n":
            print("Have a wonderful day!")
        else:
            print("Let's try another one then Run the program again!")
        break
else:
    print("Ok you should just stay inside for the day!")
