from collections import namedtuple
from scipy.optimize import linprog

with open("input10.txt", "r") as f:
    lines = f.readlines()

Machine = namedtuple('Machine', ['goal', 'buttons', 'joltage'])

machines = []
for line in lines:
    words = line.split()
    goal = tuple([c=="#" for c in words[0][1:-1]])
    buttons = [tuple(int(n) for n in word[1:-1].split(",")) for word in words[1:-1]]
    joltage = tuple([int(i) for i in words[-1][1:-1].split(",")])
    machines.append(Machine(goal, buttons, joltage))

total_presses = 0
for machine in machines:
    possible_lights = set()

    initial = tuple([False]*len(machine.goal))
    possible_lights.add(initial)

    while machine.goal not in possible_lights:
        next_states = set()
        for state in possible_lights:
            candidate_buttons = set()
            for i in range(len(state)):
                if state[i] != machine.goal[i]:
                    for button in filter(lambda b: i in b, machine.buttons):
                        candidate_buttons.add(button)
                    break
            for button in candidate_buttons:
                next_states.add(tuple([(not state[s]) if s in button else state[s] for s in range(len(state))]))

        possible_lights = next_states
        total_presses += 1

print(total_presses)  # part 1

total_presses = 0
for machine in machines:
    n = len(machine.joltage)
    c =  [1] * len(machine.buttons)
    b_eq = [-1*j for j in machine.joltage]
    A_eq = [[(-1 if i in b else 0) for b in machine.buttons] for i in range(n)]
    bounds = [(0, None)] * len(machine.buttons)
    result= linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs", integrality=True)
    assert result.success == True
    total_presses += round(result.fun)
print(total_presses)  # part 2