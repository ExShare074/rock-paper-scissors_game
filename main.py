#ИГРА КАМЕНЬ\НОЖНИЦЫ\БУМАГА
import random

def determine_winner(user_choice, computer_choice):
      # Определяем победителя
      if user_choice == computer_choice:
          return "Ничья"
      elif (user_choice == 'k' and computer_choice == 'n') or \
           (user_choice == 'n' and computer_choice == 'b') or \
           (user_choice == 'b' and computer_choice == 'k'):
           return "Вы победили!"
      else:
          return "Вы проиграли."

user_score, computer_score = 0, 0

while user_score < 3 and computer_score < 3:
      user_choice = input("Выберите камень (k), ножницы (n) или бумагу (b): ")
      computer_choice = random.choice(['k', 'n', 'b'])

      print(f"Ваш выбор: {user_choice}")
      print(f"Выбор компьютера: {computer_choice}")

      winner = determine_winner(user_choice, computer_choice)
      print(winner)

      if winner == "Вы победили!":
          user_score += 1
      elif winner == "Вы проиграли.":
          computer_score += 1

      print(f"Ваш счет: {user_score}")
      print(f"Счет компьютера: {computer_score}")

if user_score > computer_score:
      print("Вы выиграли игру!")
else:
      print("Вы проиграли игру.")