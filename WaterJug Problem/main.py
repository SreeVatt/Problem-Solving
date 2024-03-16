class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def water_jug_problem(jug1_cap, jug2_cap, target_amount):
    queue = [State(0, 0)]
    visited = set()

    while queue:
        state = queue.pop(0)

        if state.jug2 == target_amount:
            return state

        if state not in visited:
            visited.add(state)

            # Fill jug1
            queue.append(State(jug1_cap, state.jug2))

            # Fill jug2
            queue.append(State(state.jug1, jug2_cap))

            # Empty jug1
            queue.append(State(0, state.jug2))

            # Empty jug2
            queue.append(State(state.jug1, 0))

            # Pour from jug1 to jug2
            if state.jug1 > 0 and state.jug2 < jug2_cap:
                queue.append(State(state.jug1 - min(state.jug1, jug2_cap - state.jug2), state.jug2 + min(state.jug1, jug2_cap - state.jug2)))

            # Pour from jug2 to jug1
            if state.jug2 > 0 and state.jug1 < jug1_cap:
                queue.append(State(state.jug1 + min(state.jug2, jug1_cap - state.jug1), state.jug2 - min(state.jug2, jug1_cap - state.jug1)))

    return None

if __name__ == "__main__":
    jug1_cap = int(input("Enter Capacity of Jug 1"))
    jug2_cap = int(input("Enter Capacity of Jug 2"))
    target_amount = int(input("Enter Target Capacity"))

    state = water_jug_problem(jug1_cap, jug2_cap, target_amount)

    if state is None:
        print("No solution found")
    else:
        print("Solution found:")
        print(state.jug1, state.jug2)
