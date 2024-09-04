from board import PlayDesk
from player import Player

players_count = int(input("Zadej počet hráčů: "))
players = [
    Player(chr(ord('A') + i)) for i in range(players_count)
]
# hraci = [Hrac(f"{i + 1}") for i in range(pocet_hracu)]
play_desk = PlayDesk()

while True:
    for player in players:
        roll = player.roll()
        player.move(roll)
        player.position = play_desk.rules(player.position)
        print(f"Hráč {player.name} hodil {roll} a posunul se na pole {player.position}")

        same_position_player = play_desk.check_positions(players, player)
        if same_position_player:
            print(f"Hráč {player.name} stojí na místě {player.position} jako hráč {same_position_player.name}")
            same_position_player.move(-1)
            same_position_player.position = play_desk.rules(same_position_player.position)
            print(f"Hráč {same_position_player.name} se posunul na pole {same_position_player.position}")

        if player.position >= 100:
            print(f"Hráč {player.name} vyhrál!")
            exit()
