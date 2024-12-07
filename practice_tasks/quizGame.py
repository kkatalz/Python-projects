from colorama import Fore, Style


def question(question, firstOption, secOption, thOption, fourthOption, correctAnswer):    

    print("\n" + question)
    print(f"\nA. {firstOption} \nB. {secOption} \nC. {thOption} \nD. {fourthOption}")
    userAnswer = input("Your answer: ").lower()
    if userAnswer in correctAnswer:
        print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
        return 1
    else:
        for i in range(len(correctAnswer)):
            if i == 0:
                correctAnswers = correctAnswer[i].upper()
            else:
                correctAnswers += " or " + correctAnswer[i].upper()
                
        print(f"{Fore.RED} Wrong. The correct answers are {correctAnswers} {Style.RESET_ALL}")
        return 0
    

def main():
    firstQuestion = "Question 1: What is the capital of France?"
    firstQuestionOptions = {
        "A": "Berlin",
        "B": "Madrid",
        "C": "Paris",
        "D": "Rome"
    }
    firstQuestionCorrectAnswer = ["c", "paris"]

    secondQuestion = "Question 2: What planet is known as the Red Planet?"
    secondQuestionOptions = {
        "A": "Earth",
        "B": "Jupiter",
        "C": "Mars",
        "D": "Venus"
    }
    secondQuestionCorrectAnswer = ["c", "mars"]

    thirdQuestion = "Question 3: What is the largest ocean in the world?"
    thirdQuestionOptions = {
        "A": "Atlantic Ocean",
        "B": "Indian Ocean",
        "C": "Pacific Ocean",
        "D": "Northern Ocean"
    }
    thirdQuestionCorrectAnswer = ["c", "pacific ocean"]

    rightAnswers = 0
    rightAnswers += question(firstQuestion, firstQuestionOptions["A"], firstQuestionOptions["B"], firstQuestionOptions["C"], firstQuestionOptions["D"], firstQuestionCorrectAnswer)
    rightAnswers += question(secondQuestion, secondQuestionOptions["A"], secondQuestionOptions["B"], secondQuestionOptions["C"], secondQuestionOptions["D"], secondQuestionCorrectAnswer)
    rightAnswers += question(thirdQuestion, thirdQuestionOptions["A"], thirdQuestionOptions["B"], thirdQuestionOptions["C"], thirdQuestionOptions["D"], thirdQuestionCorrectAnswer)

    print(f"\nQuiz over! You got {rightAnswers} out of 3 questions right.")

main()