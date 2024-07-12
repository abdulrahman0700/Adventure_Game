import time
import random


def print_pause(*setence):
    """
    * Delay between Prints and another *

    Parameters :
      Sentence (String) : our Sentence that we want to print

    Return :
      None

    """
    time.sleep(2)
    print(*setence)


def plat_again():

    while True:
        replay = input("Do you wanna play again ? please answer y/n ")
        replay = replay.lower()

        if replay == 'y':
            Start_Game()
            main()
            break
        elif replay == 'n':
            print_pause("We hope to see you again !")
            break
        else:
            print_pause("Invalid Input")


def defend(score):

    """
    * print win if the player got a score 100 and Facing the monster *

    Parameters :
       Score (int) : store the score of the player in it

    Return :
       None
    """
    print_pause("it Trying to attack you!",
                " you avoid it so hard with little scratch on your face")
    print_pause("then you Casting a spell, abracadabra! you defeated him !")
    if score == 100:
        print_pause("Congratulation!, You Won!")
    plat_again()


def field(score):
    """
    * Back to the start of the game (Field) *

    Parameters :
      Score (int): store the score of the player in it

    Return :
      None
    """
    print_pause("Running back to the field")
    if score == 0:
        print_pause("Hmmm ...... i am sorry you lost ")
    plat_again()


def cave(score):
    """
    * Cave Option and print depend on player Choice *

    Parameters :
       Score (int): store the score of the player in it

    Return :
       None
    """
    score += 30
    monster = random.choice(['bear', 'tiger', 'lion', 'wolf'])
    cave_case = random.choice(['darker', 'Scarer', 'Terrifiying', 'Creepy'])
    while True:
        print_pause("through walking into the cave",
                    " it gets {}".format(cave_case))
        print_pause("then a {} suddenly appear in front of you !",
                    " your Score is {}".format(monster, score))
        print_pause("Enter 1 if you want to face the {}".format(monster))
        print_pause("Enter 2 if you want to go back to the field")
        cave_step = input("Please Enter 1 or 2: ")
        if cave_step == '1':
            score += 60
            print_pause("Your Score {}".format(score))
            defend(score)
            break
        elif cave_step == '2':
            score -= 40
            print_pause("Your Score {}".format(score))
            field(score)
            break
        else:
            print_pause("Invalid Input")


def house(score):
    """
    * house Option and print depend on player Choice *

    Parameters :
       Score (int): store the score of the player in it

    Return :
       None
    """

    house_case = random.choice(["you find it so old and smell so bad",
                                " You find it ancient ",
                                " and it has a dreadful smell",
                                " You notice how old it is",
                                " and the stench is unbearable",
                                " It is aged and gives off a terrible scent",
                                " it was really scary"])
    print_pause("You Enter to the house , {}".format(house_case),
                "and you find two ways of stairs to go up")
    print_pause("you have to choose the right way or the left way")
    print_pause("Enter 1 if you want to choose the right way")
    print_pause("Enter 2 if you want to choose the left way")
    print_pause("Or if you want to go back to the field Enter 3")

    road_choice = input("Please Enter 1 or 2 or 3: ")

    if road_choice == '1':
        score += 30
        while road_choice == '1':
            monsters = random.choice(['Sinister Sprite', 'Malevolent Pixie',
                                      'Dark Sylph', 'Vengeful Imp'])
            print_pause("Now you go up to the right way",
                        "and you heared a noise next to you !")
            print_pause("You turned you face and found ",
                        "a hude ugle Sinister Sprite!",
                        "your Score is {} ".format(score))
            print_pause("Enter 1 if you want to face The{}!".format(monsters))
            print_pause("Enter 2 if you want running to the field")
            house_step = input("Please Enter 1 or 2: ")
            if house_step == '1':
                score += 60
                print_pause("Your Score {}".format(score))
                defend(score)
                break
            elif house_step == '2':
                score -= 40
                print_pause("Your Score {}".format(score))
                field(score)
                break
            else:
                print_pause("Invalid Input")

    elif road_choice == '2':
        score += 30
        monsteres = random.choice(['Cursed Elf', 'Malicious Nymph',
                                   'Fiendish Brownie',
                                   'Evil Dryad', 'wicked fairy'])
        while road_choice == '2':
            print_pause("Now you go up to the left way",
                        "and when you go up the stairs got broke!")
            print_pause("You fall down and suddenly found ",
                        "in front of you the {} !".format(monsteres))
            print_pause("Enter 1 if you want to facing {} !".format(monsteres))
            print_pause("Enter 2 if you want running to the field")
            house_step = input("Please Enter 1 or 2: ")
            if house_step == '1':
                score += 60
                print_pause("Your Score{}".format(score))
                defend(score)
                break
            elif house_step == '2':
                score -= 40
                print_pause("Your Score {}".format(score))
                field(score)
                break
            else:
                print_pause("Invalid Input")

    elif road_choice == '3':
        score = 0
        print_pause("Your Score {}".format(score))
        field(score)

    else:
        score = 10
        print_pause("Invalid Input")
        house(score)


def Choice():
    """
    * First Option and print depend on player Choice *

    Parameters :
       None

    Return :
       None
    """
    print_pause("Enter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave")


def Start_Game():
    """
    * The Start of the Game and print depend on player Choice *

    Parameters :
       None

    Return :
       None
    """

    print_pause("You find yourself standing in an open field",
                "filled with grass and",
                "yellow wildflowers .")

    print_pause("Rumor has it that a wicked fairie ",
                "is somewhere around here and has",
                "been terrifying the nearby village.")

    print_pause("In front of you is house")

    print_pause("To your right is a dark cave")

    print_pause("In your hand you hold your trusty magic wand")


def main():
    """
    *Start of the Game and print depend on player Choice *

    Parameters :
       None

    Return :
       None
    """

    Choice()

    total_score = 10

    while True:

        user_choice = input("Please Enter 1 or 2: ")

        if user_choice == '1':
            house(total_score)
            break

        elif user_choice == '2':
            cave(total_score)
            break


Start_Game()
main()
