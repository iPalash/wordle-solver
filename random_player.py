from wordle_player import WordlePlayer
import re, random


class RandomPlayer(WordlePlayer):
    def __init__(self, words) -> None:
        self.words = words 
        self.guess_history = []
        self.resp_history = []
        self.patterns = set()

    def match(self, word):
        for pattern in self.patterns:
            if not re.search(pattern, word):
                return False
        return True


    def guess(self) -> str:
        matches = [word for word in self.words if self.match(word)]
        l = len(matches)
        # print("Matches: ", self.patterns, matches[:4])
        guess = random.choice(matches)
        self.guess_history.append(guess)
        print(f"RandomPlayer Guess: {guess}")
        return guess
    def cb(self, resp):
        self.resp_history.append(resp)
        # 10000
        patterns = []
        matched = set()
        for i,(r,ch) in enumerate(zip(resp,self.guess_history[-1])):
            if r=='2': # Right place
                patterns.append(f'{"."*i}[{ch}]{"."*(5-i-1)}')
                matched.add(ch)
        for i,(r,ch) in enumerate(zip(resp,self.guess_history[-1])):
            if r=='1': # Wrong place
                patterns.append(f'[{ch}]')
                matched.add(ch)
        for i,(r,ch) in enumerate(zip(resp,self.guess_history[-1])):
            if r=='0' and ch not in matched:
                patterns.append(f'[^{ch}]{{5}}')
            elif r=='1': # Wrong place
                patterns.append(f'[{ch}]')
                matched.add(ch)
            elif r=='2': # Right place
                patterns.append(f'{"."*i}[{ch}]{"."*(5-i-1)}')
                matched.add(ch)
        self.patterns.update(patterns)
        # print("Adding patterns: ", patterns, self.patterns)
        
        