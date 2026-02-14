import random

def generate_ticket():
    numbers = random.sample(range(1, 26), 5)
    numbers.sort()
    return numbers

def generate_tickets(players):
    tickets = []
    for i in range(players):
        tickets.append(generate_ticket())
    return tickets

def mark_number(ticket, number):
    for i in range(len(ticket)):
        if ticket[i] == number:
            ticket[i] = "X"

def check_winner(ticket):
    count = 0
    for num in ticket:
        if num == "X":
            count += 1
    return count == 5

def play_game(tickets, players):
    called_numbers = []
    turn = 0

    while True:
        current_player = turn % players
        print("\nPlayer", current_player + 1, "turn")

        # 🟢 Player 1 → Manual
        if current_player == 0:
            number = int(input("Enter number (1-25): "))

            if number < 1 or number > 25:
                print("❌ Invalid number! Enter between 1-25.")
                continue

            if number in called_numbers:
                print("❌ Number already called!")
                continue

        # 🔵 Other Players → Random
        else:
            number = random.randint(1, 25)

            while number in called_numbers:
                number = random.randint(1, 25)

            print("Computer Player", current_player + 1, "called:", number)

        called_numbers.append(number)

        for i in range(players):
            mark_number(tickets[i], number)

            if check_winner(tickets[i]):
                print("\n🎉 Player", i + 1, "wins the game!")
                return

        turn += 1

        if len(called_numbers) == 25:
            print("\nGame Over! No winner.")
            return

def main():
    players = int(input("Enter total players (including you): "))

    if players > 0:
        tickets = generate_tickets(players)

        print("\nGenerated Tickets:")
        for i in range(players):
            print("Player", i + 1, "Ticket:", tickets[i])

        print("\nYou are Player 1 🎮")
        play_game(tickets, players)
    else:
        print("Please enter valid number.")

main()
