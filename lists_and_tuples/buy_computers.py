current_choice = -1
computer_parts = []
options = ["computer", "monitor", "keyboard",
           "mouse", "mouse mat", "hdmi cable"]

while current_choice:
    if 0 < current_choice <= len(options):
        print(f"Adding {current_choice}")
        computer_parts.append(options[current_choice - 1])
    else:
        print("Please add options to the list below: ")
        for number, part in enumerate(options):
            print(f"{number}. {part}")
        print("0. exit")
        current_choice = int(input())
print(computer_parts)
