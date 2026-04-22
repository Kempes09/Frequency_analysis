# task_2_1_freq_analysis.py

def frequency_analysis(filename):
    
    #Create dictionary with all letters set to 0
    counts = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        counts[letter] =0 

    #Read file and count letters
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().upper()  

    for char in text:
        if char.isalpha():  # check if character is a letter
            counts[char] += 1

    #Calculate total for percentage
    total = sum(counts. values())

    # Sort - descending frequency, alphabetical for ties
    sorted_letters = sorted(counts.items(), 
                           key=lambda x: (-x[ 1], x[ 0]))

    #Print header
    print(f"{'Letter':<10}{'Count':<10}{'Percentage'}")
    print("-" * 35)
    
    #Print each row
    for letter, count in sorted_letters:
        percentage = (count / total *  100) if total > 0 else 0
        print(f"{letter:<10}{count:<10}{percentage:.2f}%")

if __name__ == "__main__":
    frequency_analysis("ciphertext.txt")