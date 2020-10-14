import random
from playsound import playsound

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


class ArchersAndShooters:

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
            archer.update(a)
            print(
                f"""
                Hi {archer["Name"]} you are the Archer.
                You will start with {archer['Ammunition']} {archer['Weapon']}.
                You have {archer['Health']}% health. Good luck!
                """)
            s = {"Name": player2_name}
            shooter.update(s)
            print(
                f"""
                Hi {shooter["Name"]} you are the Shooter.
                You will start with {shooter['Ammunition']} {shooter['Weapon']}.
                You have {shooter['Health']}% health. Good luck!
                """)

        if randomize == "shooter":
            s = {"Name": player1_name}
            shooter.update(s)
            print(
                f"""
                            Hi {shooter["Name"]} you are the Shooter.
                            You will start with {shooter['Ammunition']} {shooter['Weapon']}.
                            You have {shooter['Health']}% health. Good luck!
                            """)

            a = {"Name": player2_name}
            archer.update(a)
            print(
                f"""
                            Hi {archer["Name"]} you are the Archer.
                            You will start with {archer['Ammunition']} {archer['Weapon']}.
                            You have {archer['Health']}% health. Good luck!
                            """)

    def fight(self):
        archer = self.archer
        shooter = self.shooter

        while True:
            if archer["Health"] <= 0:
                print(
                    f"""
                    Sorry {archer['Name']} you are out of health:( Better luck next time.
                    {shooter['Name']} won with {shooter['Health']}% health and {shooter["Ammunition"]} bullets!

                    """)
                break
            elif archer["Ammunition"] <= 0:
                print(
                    f"""
                    Sorry {archer['Name']} you are out of ammo:( Better luck next time.
                    {shooter['Name']} won with {shooter['Health']}% health and {shooter["Ammunition"]} bullets!

                     """)
                break

            elif shooter["Health"] <= 0:
                print(
                    f"""
                    Sorry {shooter['Name']} you are out of health:( Better luck next time.
                    {archer['Name']} won with {archer['Health']}% health and {archer["Ammunition"]} arrows!

                    """)
                break

            elif shooter["Ammunition"] <= 0:
                print(
                    f"""
                    Sorry {shooter['Name']} you are out of ammo:( Better luck next time.
                    {archer['Name']} won with {archer['Health']}% health and {archer["Ammunition"]} arrows!

                    """)
                break

            else:

                num_arrows_fire = random.randint(1, 10)
                if archer["Ammunition"] < num_arrows_fire:
                    num_arrows_fire = archer["Ammunition"]
                    last_arms_archer = input(str(
                        f"""
                        {archer['Name']} you have {num_arrows_fire} arrows left. Do want to shoot at {shooter['Name']}

                        """))
                    if last_arms_archer in ("y", "Y"):
                        update_ammo_archer = {"Ammunition": archer["Ammunition"] - num_arrows_fire}
                        archer.update(update_ammo_archer)
                        if shooter["Health"] > 0:
                            update_health_shooter = {"Health": shooter["Health"] - num_arrows_fire * 2}
                            shooter.update(update_health_shooter)
                        if shooter["Health"] <= 0:
                            update_health_shooter = {"Health": 0}
                            shooter.update(update_health_shooter)

                if archer["Ammunition"] > num_arrows_fire and archer["Health"] > 0:
                    archer_turn = str(input(
                        f"""
                        {archer['Name']}, The Computer chose to attack with {num_arrows_fire} {archer['Weapon']} at {shooter['Name']}.
                        Do you want to shoot? Type Y/N.\n

                        """))
                    if archer_turn in ("y", "Y"):
                        for i in range(num_arrows_fire):
                            playsound("Arrow.mp3")
                        update_ammo_archer = {"Ammunition": archer["Ammunition"] - num_arrows_fire}
                        archer.update(update_ammo_archer)
                        if shooter["Health"] > 0:
                            update_health_shooter = {"Health": shooter["Health"] - num_arrows_fire * 2}
                            shooter.update(update_health_shooter)
                        if shooter["Health"] <= 0:
                            update_health_shooter = {"Health": 0}
                            shooter.update(update_health_shooter)

                        print(
                            f"""
                            Shot {num_arrows_fire} {archer['Weapon']} at {shooter['Name']}
                            You have {archer["Ammunition"]} arrows left with {archer["Health"]}% health.
                            {shooter['Name']} has {shooter['Health']}% health left.

                            """)
                    else:
                        break

                num_bullets_fire = random.randint(1, 10)
                if shooter["Ammunition"] < num_bullets_fire:
                    num_bullets_fire = shooter["Ammunition"]
                    last_arms_shooter = input(str(
                        f"""
                        {shooter['Name']} you have {num_bullets_fire} bullets left. Do want to shoot at {archer['Name']}

                        """))
                    if last_arms_shooter in ("y", "Y"):
                        update_ammo_shooter = {"Ammunition": shooter["Ammunition"] - num_bullets_fire}
                        shooter.update(update_ammo_shooter)
                        if archer["Health"] > 0:
                            update_health_archer = {"Health": archer["Health"] - num_bullets_fire}
                            archer.update(update_health_archer)
                        if archer["Health"] <= 0:
                            update_health_archer = {"Health": 0}
                            archer.update(update_health_archer)

                if shooter["Ammunition"] > num_bullets_fire and shooter["Health"] > 0:
                    shooter_turn = str(input(
                        f"""
                        {shooter['Name']}, The Computer chose to attack with {num_bullets_fire} {shooter['Weapon']} at {archer['Name']}.
                        Do you want to shoot? Type Y/N.\n

                        """))
                    if shooter_turn in ("y", "Y"):
                        for i in range(num_bullets_fire):
                            playsound("Bullet.mp3")
                        update_ammo_shooter = {"Ammunition": shooter["Ammunition"] - num_bullets_fire}
                        shooter.update(update_ammo_shooter)
                        if archer["Health"] > 0:
                            update_health_archer = {"Health": archer["Health"] - num_bullets_fire}
                            archer.update(update_health_archer)
                        if archer["Health"] <= 0:
                            update_health_archer = {"Health": 0}
                            archer.update(update_health_archer)
                        print(
                            f"""
                            Shot {num_bullets_fire} {shooter['Weapon']} at {archer['Name']}
                            You have {shooter["Ammunition"]} bullets left with {shooter["Health"]}% health.
                            {archer['Name']} has {archer['Health']}% health left.

                            """)
                    else:
                        break


ArchersAndShooters(archer=Archer, shooter=Shooter).fight()
