from itertools import permutations

def solve_cryptarithmetic(letters,a,b,c):
 
    
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sol[a[0]] == 0 or sol[b[0]] == 0:
            continue

        x = 1000 * sol[a[0]] + 100 * sol[a[1]] + 10 * sol[a[2]] + sol[a[3]]
        y = 1000 * sol[b[0]] + 100 * sol[b[1]] + 10 * sol[b[2]] + sol[b[3]]
        z = 10000 * sol[c[0]] + 1000 * sol[c[1]] + 100 * sol[c[2]] + 10 * sol[c[3]] + sol[c[4]]

        if x + y == z:
            return sol

    return None

a=input("Enter a Three Letter Word")
b=input("Enter a Three Letter Word")
c=input("Enter a Four Letter Word")
f=a.upper()+b.upper()+c.upper()
s=set(f)
y=list(s)
solution = solve_cryptarithmetic(y,a.upper(),b.upper(),c.upper())
if solution is not None:
    print("Solution found: ", solution)
else:
    print("No solution found.")
    
