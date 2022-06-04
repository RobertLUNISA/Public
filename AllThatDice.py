import random


class Player():
    '''
    Player class 
    return name
    return chips
    return won games
    return games played
    '''

    def __init__(self, name):
        self.name = name
        self.chips = 100
        self.won_games = 0
        self.games = 0

    def get_name(self):
        '''retun player name'''
        return self.name

    def change_chips(self, chips):
        '''return player current chips'''
        self.chips += chips

    def get_chips(self):
        '''return player 100 chips'''
        return self.chips

    def reset_chips(self):
        '''return player chips to 0'''
        self.chips = 0

    def add_games_won(self):
        '''counts player wins'''
        self.won_games += 1

    def get_victories(self):
        '''return total games won'''
        return self.won_games

    def add_games(self):
        '''counts games played'''
        self.games += 1

    def get_num_games(self):
        ''' return total number of games '''
        return self.games

    def __str__(self):
        return self.name


class Game():
    name = ""
    num_dice = None
    min_players = None

    def roll_dice(self, step):
        ''' return dice value '''
        # Empty vairable to count dice value
        dice_values = []
        for die in range(self.num_dice):
            # Validate dice roll
            dice_val = self.get_rand()
            dice_val += step
            if dice_val > 6:
                dice_val = dice_val % 6
                if dice_val == 0:
                    dice_val = 6
            dice_values.append(dice_val)
        return dice_values

    def get_rand(self):
        ''' return random dice roll (n) '''
        # random between 1 to 6
        n = random.randint(1, 6)
        return n


class OddEven(Game):
    ''' return game name, number of dice & min player '''

    def __init__(self):
        self.name = "Odd-or-Even"
        self.num_dice = 1
        self.min_players = 1


class Maxi(Game):
    ''' return game name, number of dice & min player '''

    def __init__(self):
        self.name = "Maxi"
        self.num_dice = 2
        self.min_players = 3


class Bunco(Game):
    ''' return game name, number of dice & min player '''

    def __init__(self):
        self.name = "Bunco"
        self.num_dice = 3
        self.min_players = 2


class Interface():
    '''
    print display menu
    print display game
    '''

    def display_menu(self):
        ''' return user choice from menu '''
        # menu interface
        print("What would you like to do?")
        print(" (r) register a new player")
        print(" (s) show the leader board")
        print(" (p) play a game")
        print(" (q) quit")
        choice = input("> ")
        return choice

    def display_games(self):
        ''' return user choice from game '''
        # game menu interface
        print("Which game would you like to play?")
        print(" (o) Odd-or-Even")
        print(" (m) Maxi")
        print(" (b) Bunco")
        choice = input("> ")
        return choice


class Model():
    '''
    return game condition
    return set number of players
    return add new player
    '''

    def __init__(self):
        self.players = dict()
        self.dice = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

    def change_game(self, game):
        self.game = game

    def check_game_condition(self):
        '''
        return Boolean
        True if game parametres are met
        False if game parametres are not met
        '''
        # Current Player list
        player_list = []
        for player in self.players:
            player_list.append(player)
        if self.game.name == "Odd-or-Even":
            '''
            if TRUE == Odd-or-Even
            return current player
            return bid
            return game result
            '''
            curr_player = player_list[0]
            player_name = curr_player.get_name()
            bid = self.players[curr_player]
            print(f"Hey {player_name},", end=" ")
            while True:
                choice = input("Odd (o) or Even (e)?\n> ")
                if choice != "o" and choice != "e":
                    print("Invalid choice.")
                else:
                    break
            while True:
                try:
                    throw = int(input("How strong will you throw (0-5)?\n> "))
                    if throw < 0 or throw > 5:
                        raise TypeError
                    else:
                        break
                except:
                    print("Invalid choice.")
            dice_val = self.game.roll_dice(throw)[0]
            print(self.dice[dice_val])
            if ((dice_val % 2) == 0 and choice == "e") or ((dice_val % 2) != 0 and choice == "o"):
                print(f"Congratulations, {player_name}! You win!")
                player_list[0].change_chips(bid)
                player_list[0].add_games_won()
            else:
                print(f"Sorry, {player_name}! You lose!")
                player_list[0].change_chips(-bid)
            player_list[0].add_games()
            for player in self.players:
                print(player.chips)

        elif self.game.name == "Maxi":
            '''
            if TRUE == Maxi
            return current player
            return bid
            return game result
            '''
            # Maxi game
            print("Let the game begin!")
            while True:
                round_tracker = dict()
                for curr_player in player_list:
                    print(f"It's {curr_player.get_name()}'s turn.")
                    while True:
                        try:
                            throw = int(
                                input("How strong will you throw (0-5)?\n> "))
                            if throw < 0 or throw > 5:
                                raise TypeError
                            else:
                                break
                        except:
                            print("Invalid choice.")
                    dice_values = self.game.roll_dice(throw)
                    print(self.dice[dice_values[0]], self.dice[dice_values[1]])
                    round_tracker[curr_player] = sum(dice_values)
                key_max = max(round_tracker, key=round_tracker.get)
                max_sum = round_tracker[key_max]
                player_list = []
                player_list.append(key_max)
                for key, val in round_tracker.items():
                    if val == max_sum:
                        if key != key_max:
                            player_list.append(key)
                    else:
                        key.change_chips(-self.players[key])
                        key.add_games()
                if len(player_list) == 1:
                    print(f"Congratulations, {player_list[0]}! You win!")
                    player_list[0].change_chips(self.players[player_list[0]])
                    player_list[0].add_games()
                    player_list[0].add_games_won()
                    break
                else:
                    print("Players remaining: ", end="")
                    for player in player_list:
                        print(f"{player.get_name()} ", end="")
                    print()

        elif self.game.name == "Bunco":
            '''
            if TRUE == Bunco
            return current player
            return bid
            return game result
            '''
            # Bunco game
            curr_round = 1
            overall_tracker = dict()
            while curr_round <= 6:
                print(f"<Round {curr_round}>")
                round_tracker = dict()
                again = False
                player_num = 0
                for curr_player in player_list:
                    round_tracker[curr_player] = [0, 0, 0]
                while True:
                    curr_player = player_list[player_num]
                    if again == False:
                        print(f"It's {curr_player.get_name()}'s turn.")
                    else:
                        print(f"Keep playing {curr_player.get_name()}.")
                    while True:
                        try:
                            throw = int(
                                input("How strong will you throw (0-5)?\n> "))
                            if throw < 0 or throw > 5:
                                raise TypeError
                            else:
                                break
                        except:
                            print("Invalid choice.")
                    dice_values = self.game.roll_dice(throw)
                    print(
                        self.dice[dice_values[0]], self.dice[dice_values[1]], self.dice[dice_values[2]])
                    if curr_round in dice_values:
                        total_same = 0
                        for val in dice_values:
                            if curr_round == val:
                                total_same += 1
                        if total_same == 3:
                            round_tracker[curr_player][0] += 21
                            round_tracker[curr_player][1] += 1
                            round_tracker[curr_player][2] += 1
                            print("Bunco!")
                            print(
                                f"You earned 21 points, {round_tracker[curr_player][0]} points in total.")
                            print(
                                f"{curr_player.get_name()} is the winner in round {curr_round}!")
                            break
                        else:
                            round_tracker[curr_player][0] += total_same
                            print(
                                f"You earned {total_same} points, {round_tracker[curr_player][0]} points in total.")
                            again = True
                    else:
                        if len(set(dice_values)) == 1:
                            round_tracker[curr_player][0] += 5
                            print(
                                f"You earned 5 points, {round_tracker[curr_player][0]} points in total.")
                            again = True
                        else:
                            print(
                                f"You earned no points, {round_tracker[curr_player][0]} points in total.")
                            player_num += 1
                            if player_num == len(player_list):
                                player_num = 0
                            again = False
                    if round_tracker[curr_player][0] >= 21:
                        round_tracker[curr_player][1] += 1
                        print(
                            f"{curr_player.get_name()} is the winner in round {curr_round}!")
                        break
                overall_tracker[curr_round] = round_tracker
                if player_num == len(player_list)-1:
                    player_list = player_list[:player_num] + \
                        player_list[player_num:]
                else:
                    player_list = player_list[player_num +
                                              1:] + player_list[:player_num+1]
                curr_round += 1

            '''return result and accumulates rounds and wins for user'''
            total_points = dict()
            print("====="+"==========="*len(player_list))
            print("{:>5}".format("Round"), end="")
            for player in player_list:
                print("{:>11}".format(player.get_name()), end="")
            print("\n====="+"==========="*len(player_list))
            for round in overall_tracker:
                print("{:>5}".format(round), end="")
                for player in player_list:
                    point = overall_tracker[round][player][0]
                    wins = overall_tracker[round][player][1]
                    bunco = overall_tracker[round][player][2]
                    print("{:>11}".format(
                        overall_tracker[round][player][0]), end="")
                    if player in total_points:
                        total_points[player][0] += point
                        total_points[player][1] += wins
                        total_points[player][2] += bunco
                    else:
                        total_points[player] = [point, wins, bunco]
                print()
            print("====="+"==========="*len(player_list))
            print("{:>5}".format("Total"), end="")
            for player in player_list:
                print("{:>11}".format(total_points[player][0]), end="")
            print("\n====="+"==========="*len(player_list))
            print("{:>5}".format("Bunco"), end="")
            for player in player_list:
                print("{:>11}".format(total_points[player][2]), end="")
            print("\n====="+"==========="*len(player_list))
            winner = max(total_points, key=lambda k: (
                total_points[k][1], total_points[k][0], total_points[k][2]))
            winner_points = total_points[winner][0]
            winner_wins = total_points[winner][1]
            winner_bunco = total_points[winner][2]
            print(
                f"{winner.get_name()} won {winner_wins} rounds, scoring {winner_points}, with {winner_bunco} Buncos")
            print(f"Congratulations, {winner.get_name()}! You win!")

            for player in player_list:
                player.add_games()
                if player == winner:
                    player.change_chips(self.players[player])
                    player.add_games_won()
                else:
                    player.change_chips(-self.players[player])

    def set_num_players(self, roster):
        '''return set number of players'''
        player_min = 1
        player_max = 1
        if self.game.name == "Odd-or-Even":
            self.player_num = 1
        else:
            if self.game.name == "Maxi":
                player_min = 3
                player_max = 5
            elif self.game.name == "Bunco":
                player_min = 2
                player_max = 4

            while True:
                try:
                    self.player_num = int(
                        input(f"How many players ({player_min}-{player_max})?\n> "))
                    if self.player_num >= player_min and self.player_num <= player_max and self.player_num <= len(roster):
                        break
                    else:
                        print("Invalid choice or not enough players available.")
                except:
                    print("Invalid input")

    def add_players(self, roster):
        '''return new player string'''
        self.players = dict()
        curr_num = 1
        while curr_num <= self.player_num:
            player_exist = False
            player_name = input(f"What is the name of player #{curr_num}?\n> ")
            for player in roster:
                if player_name == player.get_name() and player not in self.players:
                    player_exist = True
                    curr_player = player
                    break
            if player_exist:
                if curr_player.get_chips() == 0:
                    print(
                        f"{player_name} cannot play because of having no chips left.")
                    continue
                available_chips = curr_player.get_chips()
                while True:
                    try:
                        bid = int(
                            input(f"How many chips would you bid {player_name} (1-{available_chips})?\n> "))
                        if bid >= 1 and bid <= available_chips:
                            self.players[curr_player] = bid
                            break
                        else:
                            print("Invalid number of chips.")
                    except:
                        print("Invalid input.")
            else:
                print(
                    f"There is no player named {player_name} or player already in the game.")
                continue
            curr_num += 1


class AllThatDice():
    '''
    return user choice from display_menu
    return user choice of game mode
    '''

    def __init__(self):
        self.interface = Interface()
        self.all_players = []

    def run(self):
        game = Model()
        while True:
            choice = self.interface.display_menu()
            if choice == "r":
                player_exists = False
                name = input("What is the name of the new player?\n> ")
                for player in self.all_players:
                    if name == player.get_name():
                        player_exists = True
                if player_exists:
                    print("Sorry, the name is already taken.")
                else:
                    new_player = Player(name)
                    self.all_players.append(new_player)
                    print(f"Welcome, {name}!\n")
                continue
            # Player choice scoreboard
            elif choice == "s":
                player_stats = []
                for player in self.all_players:
                    name = player.get_name()
                    chips = player.get_chips()
                    wins = player.get_victories()
                    games = player.get_num_games()
                    try:
                        percentage = (wins/games)*100
                    except:
                        percentage = 0
                    player_stats.append([name, chips, wins, games, percentage])
                player_stats.sort(key=lambda x: (x[1], x[4]), reverse=True)

                print("=============================")
                print("{:<11}{:>6}{:>5}{:>7}".format(
                    "Name", "Played", "Won", "Chips"))
                print("=============================")
                for player_stat in player_stats:
                    print("{:<11}{:>6}{:>5}{:>7}".format(
                        f"{player_stat[0]}", f"{player_stat[3]}", f"{player_stat[2]}", f"{player_stat[1]}"))
                print("=============================")
            # Player choice play
            elif choice == "p":
                while True:
                    choice = self.interface.display_games()
                    # Player choice OddEven
                    if choice == "o":
                        new_game = OddEven()
                        break
                    # Player choice Maxi
                    elif choice == "m":
                        new_game = Maxi()
                        break
                    # Player choice Bunco
                    elif choice == "b":
                        new_game = Bunco()
                        break
                    else:
                        print("Invalid choice.")
                game.change_game(new_game)
                if len(self.all_players) < game.game.min_players:
                    print(f"Not enough players to play {game.game.name}")
                    continue
                print(f"Let's play the game of {game.game.name}!")
                game.set_num_players(self.all_players)
                game.add_players(self.all_players)
                game.check_game_condition()

            # Player choice quit
            elif choice == "q":
                print("Thank you for playing All-That-Dice")
                exit()
            else:
                print("Invalid choice.")


'''initiate program'''
my_all_that_dice = AllThatDice()
my_all_that_dice.run()
