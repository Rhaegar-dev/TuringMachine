import termcolor
from termcolor import colored, cprint

class TuringMachine:
    def __init__(self, alphabet, states, start_pos = 0, initial_state = 'q0'):
        self.alphabet = alphabet
        self.states = states
        self.pos = start_pos
        self.state = initial_state
    
    def move(self, side):
        if side == 'R':
            self.pos += 1
        if side == 'L':
            self.pos -= 1
        if side == 'N':
            pass
    

    def run(self, sentence):
        #sentence = sentence + ' '
        while(self.state != 'q9'):

            print(self.state, end=' ')
            print(sentence[:self.pos], end ='')
            cprint(sentence[self.pos], 'red', end='')
            print(sentence[self.pos + 1:])

            a = sentence[self.pos]
            q = self.state

            qn, s, side = self.parse(states[q][a])
            #print(qn, s, side)

            self.state = qn
            sentence = self.write(sentence, s)
            self.move(side)

            if self.pos == len(sentence):
                sentence = sentence + ' '
            



    def write(self, sentence, sym):
        sentence = sentence[:self.pos] + sym + sentence[self.pos + 1:]
        return sentence

    def parse(self, rule):
        res = rule.split(' ')
        return res[0], res[1], res[2]

   


if __name__ == "__main__":
    alphabet = ['1', 'x', '=', 'a', '*', ' ']
    states = {'q0': {'1': 'q0 1 R', 'x':'q1 x R', '*':'q0 * R'}, 
              'q1': {'1':'q2 a R'}, 
              'q2': {'1':'q2 1 L', 'x':'q3 x L', '=':'q2 = L', 'a':'q2 a L'},
              'q3': {'1':'q4 a R', 'a':'q3 a L', '*':'q6 * R'},
              'q4': {'1': 'q4 1 R', 'x':'q4 x R', '=':'q4 = R', 'a':'q4 a R', '*':'q5 1 R'},
              'q5': {' ':'q2 * L'},
              'q6': {'x':'q7 x R', 'a':'q6 1 R'},
              'q7': {'1':'q2 a R', '=':'q8 = L', 'a':'q7 a R'},
              'q8': {'x':'q9 x N', 'a':'q8 1 L'},
              'q9': 'END'}

    text = '*11x11=*'
    TM = TuringMachine(alphabet, states)
    TM.run(text)