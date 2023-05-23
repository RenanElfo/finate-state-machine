from automata import FinateStateMachine

def main():
    states = {0, 1, 2, 3, 4, 5}
    initial_state = 0
    final_states = {0, 1, 2, 3, 4}
    transitions = {
        (0, 'C'): 0,
        (0, 'P'): 1,
        (0, 'E'): 2,
        (0, 'D'): 3,
        (1, 'C'): 4,
        (1, 'P'): 1,
        (1, 'E'): 2,
        (1, 'D'): 3,
        (2, 'C'): 4,
        (2, 'P'): 4,
        (2, 'E'): 2,
        (2, 'D'): 3,
        (3, 'C'): 4,
        (3, 'P'): 4,
        (3, 'E'): 4,
        (3, 'D'): 3,
        (4, 'C'): 4,
        (4, 'P'): 4,
        (4, 'E'): 4,
        (4, 'D'): 4,
    }
    symbols = {'C','P', 'E', 'D'}
    automata = FinateStateMachine(
        states, initial_state, final_states, transitions, symbols
        )
    sequence = 'CCCCPPEED'
    print(automata.run(sequence))


if __name__ == '__main__':
    main()
