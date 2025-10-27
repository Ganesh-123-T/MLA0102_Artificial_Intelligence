states = [
    ('floor', 'A', 'B', False),
    ('floor', 'B', 'B', True)
]

for s in states:
    monkey, box, bananas, hasBananas = s
    if hasBananas:
        action = 'Monkey eats bananas'
    elif monkey == box:
        action = 'Climb box and get bananas'
    else:
        action = 'Move to box'
    print(f"Monkey:{monkey}, Box:{box}, Bananas:{bananas}, Action:{action}")
