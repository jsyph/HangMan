from dictionary import Dictionary
from ui import UI


def is_complete(current: list[str]) -> bool:
    for i in current:
        if i == "_":
            return False
    return True


def main():
    ui = UI()
    ui.clear_screen()

    dictionary = Dictionary()
    word = dictionary.random_word()

    answer = [i for i in word]
    current = ["_" for _ in word]

    stage: int = 1

    debug_mode: bool = False

    while stage != 7 and not is_complete(current):
        if not debug_mode:
            ui.clear_screen()

        ui.print_intro()
        ui.print_hangman(stage)

        responce = ui.prompt(current)

        if responce == "DEV_DEBUG_MODE":
            debug_mode = True
            ui.print_answer(word)

        valid: bool = False
        for i in range(0, len(answer)):
            if responce == answer[i]:
                if current[i] != "_":
                    ui.print_already_answered()
                else:
                    ui.print_right_answer()

                current[i] = answer[i]
                valid = True

        if not valid:
            stage += 1
            ui.print_wrong_answer()

    ui.print_answer(word)

    for x in current:
        if x == "_":
            ui.print_lose()
            return

    ui.print_win()


if __name__ == "__main__":
    main()
