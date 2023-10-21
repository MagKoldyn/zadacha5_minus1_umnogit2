target_sequence = [1]
counter = 0
while target_sequence[len(target_sequence) - 1] < 100000:
    # print(target_sequence)
    next_element = target_sequence[len(target_sequence) - 1] * 2
    while '5' in str(next_element):
        last_element = target_sequence[len(target_sequence) - 1]
        target_sequence.pop(len(target_sequence) - 1)
        next_element = last_element - 1
        if next_element == 2:
            print(target_sequence)
            exit()
    target_sequence.append(next_element)
    counter += 1
    if counter == 10000:
        print(target_sequence)
        counter = 0
