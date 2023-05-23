from automata import FinateStateMachine

def main():
    states = {0, 1, 2, 3, 4, 5}
    initial_state = 0
    final_states = {4}
    transitions = {
        (0, 'C'): 1,
        (0, 'P'): 5,
        (0, 'E'): 5,
        (0, 'D'): 5,
        (1, 'C'): 1,
        (1, 'P'): 2,
        (1, 'E'): 5,
        (1, 'D'): 5,
        (2, 'C'): 5,
        (2, 'P'): 2,
        (2, 'E'): 3,
        (2, 'D'): 5,
        (3, 'C'): 5,
        (3, 'P'): 5,
        (3, 'E'): 3,
        (3, 'D'): 4,
        (4, 'C'): 5,
        (4, 'P'): 5,
        (4, 'E'): 5,
        (4, 'D'): 4,
        (5, 'C'): 5,
        (5, 'P'): 5,
        (5, 'E'): 5,
        (5, 'D'): 5,
    }
    symbols = {'C','P', 'E', 'D'}
    automata = FinateStateMachine(
        states, initial_state, final_states, transitions, symbols
        )
    sequence = 'CCCPPEEED'
    print(automata.run(sequence))


if __name__ == '__main__':
    main()
