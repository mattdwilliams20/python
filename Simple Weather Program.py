daily_weather = [["Monday", "Sunny"], ["Tuesday", "Sunny"] , ["Wednesday", "Cloudy"], ["Thursday", "Rainy"], ["Friday", "Sunny"], ["Saturday", "Windy"], ["Sunday", "Sunny"]]


def weather_app(Day):
    if Day.lower() == "monday":
        print("The weather on",daily_weather[0][0], "will be", daily_weather[0][1])
    elif Day.lower() == "tuesday":
        print("The weather on",daily_weather[1][0], "will be", daily_weather[1][1])
    elif Day.lower() == "wednesday":
        print("The weather on",daily_weather[2][0], "will be", daily_weather[2][1])
    elif Day.lower() == "thursday":
        print("The weather on",daily_weather[3][0], "will be", daily_weather[3][1])
    elif Day.lower() == "friday":
        print("The weather on",daily_weather[4][0], "will be", daily_weather[4][1])
    elif Day.lower() == "saturday":
        print("The weather on",daily_weather[5][0], "will be", daily_weather[5][1])
    elif Day.lower() == "sunday":
        print("The weather on",daily_weather[6][0], "will be", daily_weather[6][1])
    else:
        print("Please enter a day of the week.")


weather_daily = weather_app(input("Which day in the following week do you want to know the weather for? "))

question = input("Are you happy with the weather? ")

def answer_question():
    if question.lower() == "yes":
        print("Awesome, enjoy your day!")
    else:
        print("The world ain't all sunshine and rainbows.")

answer_question()


