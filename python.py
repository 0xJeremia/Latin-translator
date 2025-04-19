# main.py

def pig_latin(word):
    vowels = "aeiou"
    word = word.lower()
    
    if word[0] in vowels:
        return word + "way"
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  # for words with no vowels

def translate_sentence(sentence):
    words = sentence.strip().split()
    translated = [pig_latin(word) for word in words]
    return " ".join(translated)

if __name__ == "__main__":
    print("🐷 Pig Latin Translator 🐷")
    user_input = input("Enter a sentence: ")
    output = translate_sentence(user_input)
    print("Pig Latin:", output)
