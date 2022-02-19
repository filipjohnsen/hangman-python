import random


def main():
    f = open("word.txt", "r")
    word_array = f.read().split("\n")
    number_of_guesses = 6
    current_guess = ""
    random_word = word_array[random.randint(0, len(word_array)) - 1]
    total_word = ["_"] * len(random_word)
    total_correct = 0

    print("Ordet består av " + str(len(random_word)) + " bokstaver")

    def correct_quess(letter):
        for idx, l in enumerate(random_word):
            if l == letter:
                total_word[idx] = letter

    while number_of_guesses >= -1:
        if "".join(total_word) == random_word:
            print("RIKTIG, DU VANT! ORDET VAR " + random_word)
            break

        current_guess = input("Skriv en bokstav \n").split(" ")[0]

        if current_guess not in random_word:
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print("Du er tom for forsøk")
                break
            print("Det var feil, du har " +
                  str(number_of_guesses) + " igjen \n\n")
        elif current_guess in random_word:
            total_correct += 1
            correct_quess(current_guess)
            print("Riktig bokstav, men du mangler fortsatt " +
                  str(len(random_word) - total_correct) + " bokstaver")
            print("".join(total_word))
        else:
            break


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
