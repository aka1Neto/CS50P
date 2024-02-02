phrase = input("Input");
vowels = ['a', 'e', 'i', 'o', 'u'];

for letter in phrase:
    if letter.lower() in vowels:
        phrase = phrase.replace(letter, "");

print("Output:", phrase)