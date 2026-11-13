def unify(p1, a1, p2, a2):

    print("Expression 1:", p1, a1)
    print("Expression 2:", p2, a2)

    # Step 1: Check if expressions are equal
    if p1 == p2 and a1 == a2:
        print("Already equal")
        return

    # Step 2: Check predicate names
    if p1 != p2:
        print("Unification Failed - Predicate Names are different")
        return

    # Step 3: Check number of arguments
    if len(a1) != len(a2):
        print("Unification Failed - Number of arguments are different")
        return

    substitution = {}

    # Step 4: Compare arguments
    for x, y in zip(a1, a2):

        # Apply existing substitutions
        while x in substitution:
            x = substitution[x]

        while y in substitution:
            y = substitution[y]

        if x == y:
            continue

        elif x.islower():
            substitution[x] = y

        elif y.islower():
            substitution[y] = x

        else:
            print("Unification Failed - Conflicting variables")
            return

    # Step 5: Apply substitutions
    print("\nSubstitutions:")
    for x, y in substitution.items():
        print(x, "=", y)

    result = a1[:]

    for i in range(len(result)):
        while result[i] in substitution:
            result[i] = substitution[result[i]]

    print("\nUnified Expression:")
    print(p1 + "(" + ", ".join(result) + ")")
    print("Unification Successful!")


# Example
unify("Eats", ["x", "Apple"],
      "Eats", ["Riya", "y"])
print("-------------------\n")

unify("Eats", ["x", "Apple"],
      "Eats", ["Riya", "x"])
print("-------------------\n")

unify("Likes", ["x", "Apple"],
      "Eats", ["Riya", "y"])
print("-------------------\n")

unify("Eats", ["x", "Apple"],
      "Eats", ["Riya"])
print("-------------------\n")

unify("Eats", ["Riya", "Apple"],
      "Eats", ["Riya", "Apple"])
