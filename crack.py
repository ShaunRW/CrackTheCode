
def correct_and_well_placed(subject, test, required_match_count):
    count = 0
    for index, num in enumerate(subject):
        if num == test[index]:
            count += 1
    return count == required_match_count

def contains_but_wrong_position(subject, test, required_match_count):
    count = 0
    for index in range(0, 3):
        if subject[index] == test[index]:
            return False
        if subject[index] in test:
            count += 1
    return count == required_match_count

def excludes(subject, test):
    for num in subject:
        if num in test:
            return False
    return True

def create_subjects():
    for number in range(0, 1000):
        subject = str(number)
        if len(subject) != 3:
            subject = "0"*(3-len(subject)) + subject
        yield subject


if __name__ == "__main__":
    subjects = create_subjects()
    possible_numbers = []
    for subject in subjects:
        possible = correct_and_well_placed(subject, "682", 1)
        possible = possible and contains_but_wrong_position(subject, "614", 1)
        possible = possible and contains_but_wrong_position(subject, "206", 2)
        possible = possible and excludes(subject, "738")
        possible = possible and contains_but_wrong_position(subject, "870", 1)
        if possible:
            possible_numbers.append(subject)

    print(possible_numbers)
