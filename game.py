import random

Archer = {
            "Name": "",
            "Health": 100,
            "KD_Ratio": 0,
            "Weapon": "arrows",
            "Ammunition": 100
        }

Shooter = {
            "Name": "",
            "Player_Type": "",
            "Health": 100,
            "KD_Ratio": 0,
            "Weapon": "bullets",
            "Ammunition": 50
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

    def __init__(self, archer, shooter):
        print(game_img)
        self.archer = archer
        self.shooter = shooter
        player_type = ["archer", "shooter"]

        player1_name = input(f"Who is Player 1?\n")

        player2_name = input(f"Who is Player 2?\n")

        randomize = random.choice(player_type)

        if randomize == "archer":
            a = {"Name": player1_name}
            self.archer.update(a)
            print(
                f"""
                Hi {self.archer["Name"]} you are the Archer.
                You will start with {self.archer['Ammunition']} {self.archer['Weapon']}.
                You have {self.archer['Health']}% health. Good luck!
                """)
            s = {"Name": player2_name}
            self.shooter.update(s)
            print(
                f"""
                Hi {self.shooter["Name"]} you are the Shooter.
                You will start with {self.shooter['Ammunition']} {self.shooter['Weapon']}.
                You have {self.shooter['Health']}% health. Good luck!
                """)

        if randomize == "shooter":
            s = {"Name": player1_name}
            self.shooter.update(s)
            print(
                f"""
                            Hi {self.shooter["Name"]} you are the Shooter.
                            You will start with {self.shooter['Ammunition']} {self.shooter['Weapon']}.
                            You have {self.shooter['Health']}% health. Good luck!
                            """)

            a = {"Name": player2_name}
            self.archer.update(a)
            print(
                f"""
                            Hi {self.archer["Name"]} you are the Archer.
                            You will start with {self.archer['Ammunition']} {self.archer['Weapon']}.
                            You have {self.archer['Health']}% health. Good luck!
                            """)


def fight(archer, shooter):
    while True:
        if archer["Health"] <= 0 or archer["Ammunition"] <= 0:
            print(
                f"""
                {archer['Name']} unfortunately you loose with {archer["Health"]}% health and {archer["Ammunition"]} arrows.
                {shooter['Name']} won with {shooter['Health']}% health and {shooter["Ammunition"]} bullets!

                """)
            break
        elif shooter["Health"] <= 0 or shooter["Ammunition"] <= 0:
            print(
                f"""
                {shooter['Name']} unfortunately you loose with {shooter["Health"]}% health and {shooter["Ammunition"]} bullets.
                {archer['Name']} won with {archer['Health']}% health and {archer["Ammunition"]} arrows!
                
                """)
            break

        else:

            num_arrows_fire = random.randint(1, 10)
            if archer["Ammunition"] < num_arrows_fire:
                num_arrows_fire = archer["Ammunition"]
                last_arms_archer = input(str(
                    f"""
                    You have {num_arrows_fire} arrows left. Do want to shoot at {shooter['Name']}
                    \n"""))
                if last_arms_archer in ("y", "Y"):
                    damage_by_archer = num_arrows_fire * 2
                    update_ammo_archer = {"Ammunition": archer["Ammunition"] - num_arrows_fire}
                    update_health_shooter = {"Health": shooter["Health"] - damage_by_archer}
                    archer.update(update_ammo_archer)
                    shooter.update(update_health_shooter)

            if archer["Ammunition"] > num_arrows_fire and archer["Health"] > 0:
                archer_turn = str(input(
                    f"""
                    {archer['Name']}, The Computer chose to attack with {num_arrows_fire} {archer['Weapon']} at {shooter['Name']}. 
                    Do you want to shoot? Type Y/N.\n
    
                    """))
                if archer_turn in ("y", "Y"):
                    damage_by_archer = num_arrows_fire * 2
                    update_ammo_archer = {"Ammunition": archer["Ammunition"] - num_arrows_fire}
                    update_health_shooter = {"Health": shooter["Health"] - damage_by_archer}
                    archer.update(update_ammo_archer)
                    shooter.update(update_health_shooter)
                    print(
                        f"""
                        Shot {num_arrows_fire} {archer['Weapon']} at {shooter['Name']}
                        You have {archer["Ammunition"]} arrows left with {archer["Health"]}% health.
                        {shooter['Name']} has {shooter['Health']}% health left.
    
                        """)

            num_bullets_fire = random.randint(1, 10)
            if shooter["Ammunition"] < num_bullets_fire:
                num_bullets_fire = shooter["Ammunition"]
                last_arms_shooter = input(str(
                    f"""
                    You have {num_bullets_fire} bullets left. Do want to shoot at {archer['Name']}
                    \n"""))
                if last_arms_shooter in ("y", "Y"):
                    damage_by_shooter = num_bullets_fire
                    update_ammo_shooter = {"Ammunition": shooter["Ammunition"] - num_bullets_fire}
                    update_health_archer = {"Health": archer["Health"] - damage_by_shooter}
                    shooter.update(update_ammo_shooter)
                    archer.update(update_health_archer)

            if shooter["Ammunition"] > num_bullets_fire and shooter["Health"] > 0:
                shooter_turn = str(input(
                    f"""
                    {archer['Name']}, The Computer chose to attack with {num_bullets_fire} {shooter['Weapon']} at {archer['Name']}. 
                    Do you want to shoot? Type Y/N.\n
    
                    """))
                if shooter_turn in ("y", "Y"):
                    damage_by_shooter = num_bullets_fire
                    update_ammo_shooter = {"Ammunition": shooter["Ammunition"] - num_bullets_fire}
                    update_health_archer = {"Health": archer["Health"] - damage_by_shooter}
                    shooter.update(update_ammo_shooter)
                    archer.update(update_health_archer)
                    print(
                        f"""
                        Shot {num_bullets_fire} {shooter['Weapon']} at {archer['Name']}
                        You have {shooter["Ammunition"]} bullets left with {shooter["Health"]}% health.
                        {archer['Name']} has {archer['Health']}% health left.
    
                        """)


play = Player(archer=Archer, shooter=Shooter)
fight(archer=play.archer, shooter=play.shooter)
