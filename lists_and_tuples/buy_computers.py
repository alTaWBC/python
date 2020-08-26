from typing import List

current_choice = -1
computer_parts: List[str] = []
options = ["computer", "monitor", "keyboard",
           "mouse", "mouse mat", "hdmi cable"]

while current_choice:
    if 0 < current_choice <= len(options):
        if options[current_choice - 1] in computer_parts:
            print(f"Removing {current_choice}")
            computer_parts.remove(options[current_choice - 1])
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(options[current_choice - 1])
    else:
        print("Please add options to the list below: ")
        for number, part in enumerate(options):
            print(f"{number + 1}. {part}")
        print("0. exit")
    print(computer_parts)
    try:
        current_choice = int(input())
    except Exception:
        current_choice = -1
print(computer_parts)
