def count_word(file_path):
    counter = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                counter[word] = counter.get(word, 0) + 1
                
    return counter

# Test case
file_path = r"D:\cau_truc_du_lieu\Kiemtra buoi 5\P1.txt"
print(count_word(file_path))
