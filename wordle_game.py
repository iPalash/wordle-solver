from wordlists import ANSWERS, WORDS
import random, sys
from random_player import RandomPlayer
MAX_TRY = 6
class Wordle:
    def __init__(self, words = WORDS, answers = ANSWERS):
        self.words = set(words+answers)
        self.answers = answers
        self.answer = answers[random.randint(0,len(answers))]
        self.tries = 0
        print(self.answer)
    
    def guess(self , word):
        if word==self.answer:
            print(f'You guessed it - {word}')
            raise Exception("GAMEOVER - WON")
        elif word in self.words:
            resp = list("00000")
            ans = list(self.answer)
            match_idx = set()
            # Match the exact first
            for i in range(5):
                if word[i]==self.answer[i]:
                    # Correct pos
                    resp[i]="2"
                    match_idx.add(i)
                    ans[i]='-'
                    
            # Match the letters right but place wrong next
            for i in range(5):
                if i in match_idx:
                    continue
                if word[i] in ans:
                    # Right letter but wrong place
                    resp[i]="1"
                    ans.remove(word[i])
        else:
            print("Invalid guess - Try again")
            return
        self.tries+=1
        if self.tries==6:
            print(f"You lost - the word was {self.answer}")
            raise Exception("GAMEOVER - LOSS")
        resp = f"{''.join(resp)}"
        print(resp)
        return resp


if __name__=='__main__':
    g = Wordle()
    player = RandomPlayer(WORDS+ANSWERS)
    interactive = sys.argv[1] =='1'
    while 1:
        if interactive:
            guess = input()
        else:
            guess = player.guess()
        resp = g.guess(guess)
        if not interactive:
            player.cb(resp)
    
