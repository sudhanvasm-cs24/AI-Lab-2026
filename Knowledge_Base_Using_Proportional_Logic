import itertools
import pandas as pd

# Define the basic logical connectives
def implication(p, q):
    return not p or q

# Generate all possible truth assignments for P, Q, R
symbols = ['P', 'Q', 'R']
truth_values = [0, 1]
combinations = list(itertools.product(truth_values, repeat=3))

rows = []
for p, q, r in combinations:
    s1 = implication(q, p)
    s2 = implication(p, not q)
    s3 = q or r
    kb_val = s1 and s2 and s3

    # Convert True/False to 1/0
    rows.append({
        'P': 1 if p else 0,
        'Q': 1 if q else 0,
        'R': 1 if r else 0,
        'Q -> P': 1 if s1 else 0,
        'P -> ~Q': 1 if s2 else 0,
        'Q v R': 1 if s3 else 0,
        'KB (AND of sentences)': 1 if kb_val else 0
    })

df = pd.DataFrame(rows)
display(df)

print("Models where KB is True:")
display(df[df['KB (AND of sentences)'] == 1])

kb_models = df[df['KB (AND of sentences)'] == 1]
# ii) Does KB entail R?
entails_R = True if all(kb_models['R'] == 1) else False
print(f"\nii) Does KB entail R? {entails_R}")

# iii) Does KB entail R -> P?
# R -> P is True (1) if R is 0 or P is 1
r_imp_p = kb_models.apply(lambda row: 1 if (row['R'] == 0 or row['P'] == 1) else 0, axis=1)
entails_R_imp_P = True if all(r_imp_p == 1) else False
print(f"iii) Does KB entail R -> P? {entails_R_imp_P}")

# iv) Does KB entail Q -> R?
# Q -> R is True (1) if Q is 0 or R is 1
q_imp_r = kb_models.apply(lambda row: 1 if (row['Q'] == 0 or row['R'] == 1) else 0, axis=1)
entails_Q_imp_R = True if all(q_imp_r == 1) else False
print(f"iv) Does KB entail Q -> R? {entails_Q_imp_R}")
