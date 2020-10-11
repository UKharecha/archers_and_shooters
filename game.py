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

    def __init__(self):
        print(game_img)
        self.archer = user["Archer"]
        self.shooter = user["Shooter"]
        player_type = ["archer", "shooter"]

        player1_name = input(f"Who is Player 1?\n")
        player1_age = int(input(f"Hi {player1_name}. How old are you?\n"))
        player1_sex = input("Enter your gender in M/F\n")

        player2_name = input(f"Who is Player 2?\n")
        player2_age = int(input(f"Hi {player2_name}. How old are you?\n"))
        player2_sex = input("Enter your gender in M/F\n")

        randomize = random.choice(player_type)

        if randomize == "archer":
            a = {"Name": player1_name, "Age": player1_age, "Sex": player1_sex}
            self.archer.update(a)
            print(
                f"""
                Hi {self.archer["Name"]} you are the Archer.
                You will start with {self.archer['Ammunition']} {self.archer['Weapon']}.
                You have {self.archer['Health']}% health. Play carefully!
                """)
            s = {"Name": player2_name, "Age": player2_age, "Sex": player2_sex}
            self.shooter.update(s)
            print(
                f"""
                Hi {self.shooter["Name"]} you are the Shooter.
                You will start with {self.shooter['Ammunition']} {self.shooter['Weapon']}.
                You have {self.shooter['Health']}% health. Play carefully!
                """)

        if randomize == "shooter":
            s = {"Name": player1_name, "Age": player1_age, "Sex": player1_sex}
            self.shooter.update(s)
            print(
                f"""
                            Hi {self.shooter["Name"]} you are the Shooter.
                            You will start with {self.shooter['Ammunition']} {self.shooter['Weapon']}.
                            You have {self.shooter['Health']}% health. Play carefully!
                            """)

            a = {"Name": player2_name, "Age": player2_age, "Sex": player2_sex}
            self.archer.update(a)
            print(
                f"""
                            Hi {self.archer["Name"]} you are the Archer.
                            You will start with {self.archer['Ammunition']} {self.archer['Weapon']}.
                            You have {self.archer['Health']}% health. Play carefully!
                            """)


def fight(archer, shooter):
    while True:
        archer_turn = str(input(f"{archer['Name']} do you want to attack with {archer['Weapon']}\n"))
        if archer_turn in ("y", "Y"):
            fire = int(input(f"How many {archer['Weapon']} do you want to fire at {shooter['Name']}\n"))
            if fire > 5:
                print(f"Please use less than 5 {archer['Weapon']} at a time.")
                continue
            if fire <= 5:
                damage = fire * 2
                update_health = {"Health": shooter["Health"] - damage}
                shooter.update(update_health)
                print(f"Shooting {fire} {archer['Weapon']} at {shooter['Name']}")

        shooter_turn = str(input(f"{shooter['Name']} do you want to attack with {shooter['Weapon']}\n"))
        if shooter_turn in ("y", "Y"):
            fire = int(input(f"How many {shooter['Weapon']} do you want to fire at {archer['Name']}\n"))
            if fire > 5:
                print(f"Please use less than 5 {shooter['Weapon']} at a time.")
                continue
            if fire <= 50:
                damage = fire
                update_health = {"Health": archer["Health"] - damage}
                archer.update(update_health)
                print(f"Shooting {fire} {shooter['Weapon']} at {archer['Name']}")

        if archer["Health"] == 0:
            print(f"{archer['Name']} unfortunately you loose.")
            print(f"{shooter['Name']} won with shooter['Health']% health! ")
            break
        if shooter["Health"] == 0:
            print(f"{shooter['Name']} unfortunately you loose.")
            print(f"{archer['Name']} won with shooter['Health']% health! ")
            break


player1 = Player()
fight(archer=user["Archer"], shooter=user["Shooter"])
