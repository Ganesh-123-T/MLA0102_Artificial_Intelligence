import random

def negotiation(agent1_discount, agent2_discount, max_rounds=10):
    total_resource = 100
    round_num = 1
    offer = None

    while round_num <= max_rounds:
        if round_num % 2 == 1:  # Agent 1 makes offer
            offer = random.randint(40, 60)
            print(f"Round {round_num}: Agent 1 offers {offer}% to Agent 1 and {100-offer}% to Agent 2")
            accept = offer <= 50 + random.randint(-5, 5)
        else:  # Agent 2 makes offer
            offer = random.randint(40, 60)
            print(f"Round {round_num}: Agent 2 offers {100-offer}% to Agent 1 and {offer}% to Agent 2")
            accept = offer >= 50 - random.randint(-5, 5)
        
        if accept:
            agent1_utility = (offer if round_num % 2 == 1 else 100 - offer) * (agent1_discount ** round_num)
            agent2_utility = (100 - offer if round_num % 2 == 1 else offer) * (agent2_discount ** round_num)
            print(f"Agreement reached in round {round_num}!")
            print(f"Agent 1 Utility: {agent1_utility:.2f}")
            print(f"Agent 2 Utility: {agent2_utility:.2f}")
            return
        
        round_num += 1

    print("No agreement reached after maximum rounds.")

negotiation(agent1_discount=0.9, agent2_discount=0.85)
