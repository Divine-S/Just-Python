import random


def run_game():
    level_dif = input('Welcome To Math Trivia (Addition Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    def addition_edition(num_quests, one, two):
        score = 0
        for attempts in range(0, num_quests):
            a = random.randint(one, two)
            b = random.randint(one, two)
            try:
                quest = int(input('{}. {:>4s}\n  +{:>4s}\n{:>4s}'.format(attempts + 1, str(a), str(b), '')))
                if quest == (a + b):
                    print('\nYour Answer Is Correct\n')
                    score += 1
                else:
                    print(f'\nYour Answer Is Wrong\nThe Correct Answer Is {a + b}\n')
            except SyntaxError:
                print('Invalid Input ---: Please Enter A Number\n')
            except ValueError:
                print('Invalid Input ---: Please Enter A Number\n')

        print(f'\nYou Got {score}/{num_quests}')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        addition_edition(10, 10, 50)
    elif level_dif == 'm':
        addition_edition(20, 80, 250)
    elif level_dif == 'h':
        addition_edition(25, 300, 499)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_game()
