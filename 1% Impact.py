import random
import pandas as pd
import requests
from io import BytesIO

# URL of the Excel file in your GitHub repository
QUIZ_DATA = 'https://github.com/Shimmyou/CIP/raw/main/Environmental_Impact_Quiz_Questions.xlsx'

def get_quiz_data():
    response = requests.get(QUIZ_DATA)
    response.raise_for_status()  # Ensure the request was successful
    data = response.content
    df = pd.read_excel(BytesIO(data))
    return df

# Load the Quiz data from GitHub repository
df = get_quiz_data()
MAX = len(df)
ROUNDS = 20


    #spliting the dataframe into columns

def question_and_answers(df, index):
    categorys = df.loc[index, 'Category']
    questions = df.loc[index, 'Question']
    options = {
        '1': df.loc[index, 'Option1'],
        '2': df.loc[index, 'Option2'],
        '3': df.loc[index, 'Option3'],
        '4': df.loc[index, 'Option4']
        }
    correct_answer = df.loc[index, 'Correct Answer']
    summary = df.loc[index, 'Summary']

    return categorys, questions, options, correct_answer, summary

question_number_gen = set()

def question_drawing():
    # Function to generate random question numbers but without risk of repetition
    while len(question_number_gen) < ROUNDS:
        number = random.randint(0, 21)
        if number not in question_number_gen:
            question_number_gen.add(number)
            return number
    return None  # Explicitly return None if all 10 unique numbers are already generated

def quizlet(df):
    player_score =int(0)
    for _ in range(ROUNDS):
        unique_number = question_drawing()
        categorys, questions, options, correct_answer, summary = question_and_answers(df, unique_number)
        #Number of Question in game
        game_round = int(_)+1
        print(game_round, questions)
        for option, answer in options.items():
            print(f"{option}: {answer}")
        user_answer = input("What is your answer? (1/2/3/4): ")

                # Validate user input
        while user_answer not in options:
            user_answer = input("Please choose a valid answer (1/2/3/4): ")

        # #zabezpieczenie odpowiedzi 1-4
        # argument_invalid = user_answer !=1 or user_answer !=2 or user_answer !=3 or user_answer !=4
        # while(argument_invalid):
        #     user_answer = input("Please choose answer 1,2,3 or 4: ")
        #     argument_invalid = user_answer !=1 or user_answer !=2 or user_answer !=3 or user_answer !=4
        user_answer_text = options[user_answer]  
        if user_answer_text == correct_answer:
            print("Correct!")
            print(summary)
            player_score = player_score +1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
            print(summary)
        print()
    if player_score == 0 :
        print("You didn't score, try again!")
        print()
    else:        
        print(f"You have scored ",player_score," out of ",ROUNDS," points!")
        print()

quizlet(df)


#Komentarz Szymon: Zrobione zabezpieczenie wyboru pytania 1-4, losowanie, i sprawdzanie odpowiedzi
#Do zrobienia tylko trackowanie wyniku rozgrywkii ew. dopracowanie wyglądu etc.

    #Lista pytań i odpowiedzi, z oznaczneiem jednej poprawnej odpowiedzi
    #do każdego pytania przypisać 4 warianty, z czego tylko 1 prawidłowy
    #po uzyskaniu odpowiedzi informacja zwrotna o tym czy prawidłowa czy nie, podsumowanie, informacja o zdobytych punktach
    #losowe przypisanie odpowiedzi do różnych liter (a/b/c/d)

    # Give a "Hint" option to have more info about topic