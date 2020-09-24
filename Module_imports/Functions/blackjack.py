import tkinter
import random
from typing import List


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    location = r'Module_imports\Functions\blackjack_cards\cards_'
    for suit in suits:
        for card in range(1, 11):
            name = location + \
                f"{extension}\\cards\\{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = location + \
                f"{extension}\\cards\\{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    ace = False
    score = 0
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def create_new_game():
    global deck
    global player_hand
    global dealer_hand
    global dealer_cards_frame
    global player_cards_frame

    dealer_cards_frame.destroy()
    dealer_cards_frame = tkinter.Frame(card_frame, background="green")
    dealer_cards_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_cards_frame.destroy()
    player_cards_frame = tkinter.Frame(card_frame, background="green")
    player_cards_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    deck = list(cards)
    random.shuffle(deck)
    # print(deck)

    dealer_hand = []
    player_hand = []
    deal_player()
    deal_player()
    dealer_hand.append(deal_card(dealer_cards_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    result_text.set("")


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_cards_frame))
        dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)

    # print(player_score, dealer_score)
    # print(dealer_score > 21 or dealer_score < player_score)

    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_cards_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        # Simple code
        # global player_hand_score
        # global player_ace
        # card_dealt = deal_card(player_cards_frame)
        # player_hand.append(card_dealt)
        # card_value = card_dealt[0]
        # print(card_value)
        # if card_value == 1 and not player_ace:  # pylint: disable=used-before-assignment
        #     card_value = 11
        #     player_ace = True
        # player_hand_score += card_value  # pylint: disable=undefined-variable
        # if player_hand_score > 21 and player_ace:
        #     player_hand_score -= 10
        #     player_ace = False
        # player_score_label.set(player_hand_score)
        # if(player_hand_score > 21):
        #     result_text.set("Dealer wins")
        # print(locals())  # usefull to check local variables


def create_game():
    deal_player()
    deal_player()
    dealer_hand.append(deal_card(dealer_cards_frame))
    dealer_score_label.set(score_hand(dealer_hand))

    mainWindow.mainloop()


mainWindow = tkinter.Tk()
mainWindow.title("BlackJack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(
    mainWindow, textvariable=result_text, background='green', fg='white')
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken",
                           borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
dealer = tkinter.Label(
    card_frame, text="Dealer", background="green", fg="white")
dealer.grid(row=0, column=0)
dealer_score = tkinter.Label(
    card_frame, textvariable=dealer_score_label, background="green", fg="white")
dealer_score.grid(row=1, column=0)

# Embedded frame to hold cards images
dealer_cards_frame = tkinter.Frame(card_frame, background="green")
dealer_cards_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
player = tkinter.Label(card_frame, text="Player",
                       background="green", fg="white")
player.grid(row=2, column=0)
player_score = tkinter.Label(
    card_frame, textvariable=player_score_label, background="green", fg="white")
player_score.grid(row=3, column=0)
player_hand_score = 0
player_ace = False

# Embedded frame to hold cards images
player_cards_frame = tkinter.Frame(card_frame, background="green")
player_cards_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(
    button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(
    button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

new_game = tkinter.Button(
    button_frame, text='New Game', command=create_new_game)
new_game.grid(row=0, column=2)

cards: List[tkinter.PhotoImage] = []
load_images(cards)

deck = list(cards)
random.shuffle(deck)
# print(deck)

dealer_hand: List[tkinter.PhotoImage] = []
player_hand: List[tkinter.PhotoImage] = []

if __name__ == "__main__":
    create_game()
