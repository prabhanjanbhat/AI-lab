from sympy.logic.boolalg import Or, And, Not
from sympy.abc import A, B, C, D, E, F
from sympy import simplify_logic

def is_entailment(kb, query):
    # Negate the query
    negated_query = Not(query)
    # Add negated query to the knowledge base
    kb_with_negated_query = And(*kb, negated_query)
   
    # Simplify the combined KB to CNF
    simplified_kb = simplify_logic(kb_with_negated_query, form="cnf")
   
    # If the simplified KB evaluates to False, the query is entailed
    return simplified_kb == False




# Define a larger Knowledge Base
kb = [
    Or(A, B),         # A ∨ B
    Or(Not(A), C),    # ¬A ∨ C
    Or(Not(B), D),    # ¬B ∨ D
    Or(Not(D), E),    # ¬D ∨ E
    Or(Not(E), F),    # ¬E ∨ F
    F                 # F
]
# Query to check
query = Or(C, F)  # C ∨ F


# Check entailment
result = is_entailment(kb, query)
print(f"Is the query '{query}' entailed by the knowledge base? {'Yes' if result else 'No'}")
