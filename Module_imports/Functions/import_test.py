import blackjack

print(__name__)

blackjack.create_game()
print(blackjack.cards)

personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details
print(name, country)
print(_)
