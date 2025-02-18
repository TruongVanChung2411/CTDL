def character_count(word):
    character_statistic = {}
    
    for char in word:
        character_statistic[char] = character_statistic.get(char, 0) + 1
    
    return character_statistic

# Test case
print(character_count('Happiness'))  # {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
print(character_count('smiles'))  # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
