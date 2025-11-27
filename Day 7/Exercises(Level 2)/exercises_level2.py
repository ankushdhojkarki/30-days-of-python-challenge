A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1. Join A and B

print(f"Joining A and B: {A.union(B)}")


#2. Find A intersection B
print(f"A intersection B: {A.intersection(B)}")

#3. Is A subset of B
print(f"A subset of B: {A.issubset(B)}")

#4. Are A and B disjoint sets
print(f"A and B are disjoint sets: {A.isdisjoint(B)}")

#5. Join A with B and B with A
print(f"Joining A with B: {A.union(B)}")
print(f"Joining B with A: {B.union(A)}")

#6. What is the symmetric difference between A and B
print(f"Symmetric difference: {A.symmetric_difference(B)}")

#7. Delete the sets completely
del A
del B
print(f"{A}\n{B}")