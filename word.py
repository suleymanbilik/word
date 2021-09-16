import random

words = ['alper', 'mucahit', 'harun', 'bahri',
'emir', 'suleyman']

random_word = random.choice(words)
print('*********** ISIM TAHMINI ***********')
print('Konu : Hunililer Grubu Üyelerinden Biri')
user_guesses = ''
chances = 3

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"Dogru harf: {character}")
        else:
            wrong_guesses += 1
            print('_')

    if wrong_guesses == 0:
        print("Dogru.")
        print(f"Kelime : {random_word}")
        break
    guess = input('Bil bakalim ben kimim: ')
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f"Yanlis. Senin {chances} sansin daha var")

        if chances == 0:
            print('oyun bitti')