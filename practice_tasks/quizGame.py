from colorama import Fore, Style


def quizGame(question, firstOption, secOption, thOption, fourthOption, correctAnswer):    

    print("\n" + question)
    print(f"\n{firstOption}\n{secOption}\n{thOption}\n{fourthOption}")
    userAnswer = input("Your answer: ").lower().strip()
    for i in range(len(correctAnswer)):
        correctAnswer[i] = correctAnswer[i].lower()

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
    QUESTION = "question"
    OPTIONS = "options"
    CORRECT_ANSWER = "correctAnswer"

    quiz = [
        {
            QUESTION: "What is the capital of France?",
            OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            CORRECT_ANSWER: ["C", "Paris"]
        },
    
        {
            QUESTION: "What planet is known as the Red Planet?",
            OPTIONS: ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            CORRECT_ANSWER: ["C", "Mars"]
        },
    
        {
            QUESTION: "What is the largest ocean in the world?",
            OPTIONS: ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Northern Ocean"],
            CORRECT_ANSWER: ["C", "Pacific Ocean"]
        }
    ]

    rightAnswers = 0
    for index, question in enumerate(quiz,1):
        quizQuestion = "Question " + str(index) + ". " + question[QUESTION]
        option1 = question["options"][0]
        option2 = question["options"][1]
        option3 = question["options"][2]
        option4 = question["options"][3]
        correctAnswer = question["correctAnswer"]

        rightAnswers += quizGame(quizQuestion, option1, option2, option3, option4, correctAnswer)

    print(f"\nQuiz over! You got {rightAnswers} out of 3 questions right.")

if __name__ == "__main__":
    main()