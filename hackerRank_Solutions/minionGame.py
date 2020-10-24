# The question proposes a game in which one player maximizes the number of "sub-words" they can make out of the input word. Points are awarded based on the number of times each subword appears in the original word.
def minion_game(string):
    vowels = 'AEIOU'
    scoreStuart, scoreKevin = 0,0
    for i in range(len(string)):
        if string[i] in vowels:
            scoreKevin += (len(string) - i)
        else:
            scoreStuart += (len(string) -i)
    Winner = 'Stuart '+str(scoreStuart) if (scoreStuart>scoreKevin) else 'Kevin '+str(scoreKevin)
    print(Winner)