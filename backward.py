knowledge_base = {
    "vertebrate(A)": ["mammal(A)", "flying(A)"],
    "animal(A)": ["vertebrate(A)"],
    "bird(A)": ["vertebrate(A)", "flying(A)"]
}

facts = {"vertebrate('duck')", "flying('duck')", "mammal('cat')"}

def backward_chaining(goal):
    if goal in facts:
        return True
    for rule, premises in knowledge_base.items():
        head = rule.split('(')[0]
        if goal.startswith(head):
            for premise in premises:
                variable = goal[goal.find("(")+1:goal.find(")")]
                sub_goal = premise.replace("A", variable)
                if not backward_chaining(sub_goal):
                    return False
            return True
    return False

query = "bird('duck')"
if backward_chaining(query):
    print(query, "is True")
else:
    print(query, "is False")
