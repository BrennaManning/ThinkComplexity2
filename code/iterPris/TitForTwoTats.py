class TitForTwoTats():
    ''' TitForTwoTats will cooperate unless the oppponent defects twice. '''
    def step(self, history, round):
        if round == 0:
            action = 1
        else:
            action = history[self.order^1][round - 1] and  history[self.order^1][round - 2]
            # ^ is the bitwise XOR operator, for easy switching from 0 to 1.
        return action

