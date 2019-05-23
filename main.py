import json # this library helps convert between a list and a string (we can only store strings in a text file)
import random
import datetime

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0

player = input("Hello, what's your name?")

score_data = {
    "attempts": attempts,
    "date": datetime.datetime.now(),
    "player": input,
}

# this code helps read the text file
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

# this code helps sort the list from lowest to biggest number, in this case we only print the top 3 scores
for score_dict in score_list:
    print(str(score_dict["attempts"]) + " intentos, en la fecha " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player": player, "secret": secret}) # using .append() we add data to a list

        # with this code we save (write) the score list back into the txt
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))


        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
