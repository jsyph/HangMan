import hangman.ascii as ascii


class UI:
    def _press_enter_to_continue(self) -> None:
        input("\x1b[37mPress Enter to Continue: ")

    def clear_screen(self) -> None:
        print("\033c")

    def prompt(self, current: list[str]) -> str:
        print("[ ", end="")

        for x in current:
            print(x, end=" ")

        print("]")

        return input("Guess a Letter: ")

    def print_answer(self, answer: str):
        print(f"\x1b[36mThe correct answer is: \x1b[34m{answer}\x1b[37m")

    def print_intro(self) -> None:
        print(ascii.INTRO_TEXT)

    def print_win(self) -> None:
        print("\x1b[32m" + ascii.YOU_WIN_TEXT)

    def print_lose(self) -> None:
        print("\x1b[31m" + ascii.YOU_LOOSE_TEXT)

    def print_wrong_answer(self) -> None:
        print("\x1b[31mWrong Answer.\x1b[37m")
        self._press_enter_to_continue()

    def print_right_answer(self) -> None:
        print("\x1b[32mCorrect.\x1b[37m")

    def print_already_answered(self) -> None:
        print("\x1b[33mPreviously Answered.\x1b[37m")
        self._press_enter_to_continue()

    def print_hangman(self, stage: int) -> None:
        """
        stage: int. Number from 1 -> 7
        """
        print(ascii.HANGMAN_STAGES[stage])
