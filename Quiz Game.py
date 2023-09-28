print("Welcome to the NFL Teams Quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Let's get started!")
score = 0

question1 = input("""What 2003-04 N.Y.Giant had been with the team the longest?
a. Lawrence Taylor
b. Kerry Collins
c. Michael Barrow
d. Keith Hamilton 
""")
if question1.lower == "Kerry Collins" or "b" or "b.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

question2 = input("""Who was the first Giant quarterback to throw for over 4000 yards in a season?
a. Phil Simms
b. Fran Tarkenton
c. Jeff Hostetler
d. Y.A. Tittle 
""")
if question2.lower == "Phil Simms" or "a" or "a.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

question3 = input("""The 2004 NFL Draft saw Eli Manning drafted first overall. Which team drafted him?
a.  San Diego Chargers
b.  Tampa Bay Buccaneers
c. San Francisco 49ers
d. Atlanta Falcons
""")
if question3.lower == "San Diego Chargers" or "Chargers" or "a" or "a.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
question4 = input("""In February 2008, fans at Phoenix Stadium watched the Giants ruin the perfect-season hopes of the New England Patriots by defeating them 17-14. Which Giants player was the first to put points on the scoreboard?
a. Lawrence Tynes
b.  Heath Evans
c.  Stephen Gostkowski
 d. Laurence Maroney
 """)
if question4.lower == "Lawrence Tynes" or "a" or "a.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

question5= input("""Which receiver made one of the most iconic catches of all time, dubbed 'The Catch', as a rookie Giants receiver against the Cowboys?
a. David Tyree
b. Victor Cruz
c. Mario Manningham
d. Odell Beckham Jr
""")
if question5.lower == "Odell" or "d" or "d." or "Odell Beckham" or "Odell Beckham Jr":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


print("Your final score was " + str(score) + " out of 5!" )
print("Thanks for playing!")

