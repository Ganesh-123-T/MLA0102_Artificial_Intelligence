states = [
    ('floor', 'A', 'B', False),
    ('floor', 'B', 'B', True)
]

for s in states:
    monkey, box, bananas, hasBananas = s
    if monkey != box:
        action = 'Move to box'
    elif not hasBananas:
        action = 'Climb box and get bananas'
    else:
        action = 'Monkey eats bananas'
    print(f"Monkey:{monkey}, Box:{box}, Bananas:{bananas}, Action:{action}")
