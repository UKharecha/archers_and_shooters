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
            "Age": 0,
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
            a = {archer["Name"]: player1_name, archer["Age"]: player1_age, archer["Sex"]: player1_sex}
            user.update(a)
            print(
                f"""
                Hi {archer["Name"]} you are the Archer.
                You will start with {archer['Ammunition']} {archer['Weapon']}.
                You have {archer['Health']}% health. Play carefully!
                """)
            s = {shooter["Name"]: player2_name, shooter["Age"]: player2_age, shooter["Sex"]: player2_sex}
            user.update(s)
            print(
                f"""
                Hi {shooter["Name"]} you are the Shooter.
                You will start with {shooter['Ammunition']} {shooter['Weapon']}.
                You have {shooter['Health']}% health. Play carefully!
                """)

        if randomize == shooter:
            s = {shooter["Name"]: player1_name, shooter["Age"]: player1_age, shooter["Sex"]: player1_sex}
            user.update(s)
            print(
                f"""
                            Hi {shooter["Name"]} you are the Shooter.
                            You will start with {shooter['Ammunition']} {shooter['Weapon']}.
                            You have {shooter['Health']}% health. Play carefully!
                            """)

            a = {archer["Name"]: player2_name, archer["Age"]: player2_age, archer["Sex"]: player2_sex}
            user.update(a)
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
