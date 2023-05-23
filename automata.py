class FinateStateMachine:
    states: set[int]
    initial_state: int
    final_states: set[int]
    transitions: dict[tuple[int, str], int]
    symbols: set[str]

    def __init__(self, states, initial_state,
                 final_states, transitions, symbols):
        self.states = states
        self.initial_state = initial_state
        self. final_states = final_states
        self.transitions = transitions
        self.symbols = symbols

    def run(self, sequence):
        state = self.initial_state
        while sequence:
            state = self.transitions[(state, sequence[0])]
            sequence = sequence[1:]
        return state in self.final_states
