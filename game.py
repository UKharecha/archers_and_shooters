import random
user = {
    "Archer": 
 {
        "Name": "",
        "Age": 0,
        "Sex": "",
        "Health": 100,
        "KD_Ratio": 0,
        "Weapon": "arrows",
        "Ammunition": 100

 },

    "Shooter": 
{
        "Name": "",
        "Age" :0,
        "Sex": "",
        "Player_Type": "",
        "Health": 100,
        "KD_Ratio": 0,
        "Weapon": "bullets",
        "Ammunition": 50
 } 
}


game_img = """
        ------------------------------------------------------
        |    ^        ^                                      |
        |   ^|^      ^|^                                     |
        |    |        |             __________]______|____   |
        |    |        |             |i|||||}=============/   |
        |    |        |             |i| > )                  |
        |    |        |             |i|}                     |
        |   /|\      /|\                                     |
        |                                                    |
        |       Welcome to Archers and Shooters!             |
        ------------------------------------------------------
      """

class Player:

    def __init__(self, archer=user["Archer"], shooter=user["Shooter"]):
        self.archer = archer
        self.shooter = shooter
        player_type = [archer, shooter]

        player1_name = input(f"Who is Player 1?\n")
        player1_age = int(input(f"Hi {player1_name}. How old are you?\n"))
        player1_sex = input("Enter your gender in M/F\n")

        player2_name = input(f"Who is Player 2?\n")
        player2_age = int(input(f"Hi {player2_name}. How old are you?\n"))
        player2_sex = input("Enter your gender in M/F\n")
        
        randomize = random.choice(player_type)

        if randomize == archer:
            archer["Name"].update(player1_name)
            archer["Age"].update(player1_age)
            archer["Sex"].update(player1_sex)
            print(
                f"""
                Hi {archer["Name"]} you are the Archer.
                You will start with {archer['Ammunition']} {archer['Weapon']}.
                You have {archer['Health']}% health. Play carefully!
                """)
            shooter["Name"].update(player2_name)
            shooter["Age"].update(player2_age)
            shooter["Sex"].update(player2_sex)
            print(
                f"""
                Hi {shooter["Name"]} you are the Shooter.
                You will start with {shooter['Ammunition']} {shooter['Weapon']}.
                You have {shooter['Health']}% health. Play carefully!
                """)

        if randomize == shooter:
            shooter["Name"].update(player1_name)
            shooter["Age"].update(player1_age)
            shooter["Sex"].update(player1_sex)
            print(
                f"""
                Hi {shooter["Name"]} you are the Shooter.
                You will start with {shooter['Ammunition']} {shooter['Weapon']}.
                You have {shooter['Health']}% health. Play carefully!
                """)
            archer["Name"].update(player2_name)
            archer["Age"].update(player2_age)
            archer["Sex"].update(player2_sex)
            print(
                f"""
                Hi {archer["Name"]} you are the Archer.
                You will start with {archer['Ammunition']} {archer['Weapon']}.
                You have {archer['Health']}% health. Play carefully!
                """)


class Fight(Player):

    def __init__(self):
        pass
            



# print(team1.health())

# team1.accuracy(90), team1.health()

# team2 = Shooter(name="Umang", age=21, sex="M")
# team2.ammunition(bullets=50)
# team2.accuracy(95), team2.health()
