import re

filename = input("Enter text file name (e.g. sample.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = re.findall(r"\b[\w'-]+\b", text)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]

    def syllable_count(word):
        word = re.sub(r"[^a-z]", "", word.lower())
        if not word: return 1
        count = len(re.findall(r"[aeiouy]+", word))
        if word.endswith("e") and count > 1: count -= 1
        return max(1, count)

    word_count, sentence_count = len(words), max(1, len(sentences))
    syllables = sum(syllable_count(w) for w in words)

    if word_count == 0:
        print("The file is empty.")
    else:
        ease = 206.835 - 1.015 * word_count / sentence_count - 84.6 * syllables / word_count
        grade = 0.39 * word_count / sentence_count + 11.8 * syllables / word_count - 15.59

        print("\n----- READABILITY REPORT -----")
        print("Words:", word_count)
        print("Sentences:", sentence_count)
        print("Estimated syllables:", syllables)
        print(f"Flesch Reading Ease: {ease:.2f}")
        print(f"Estimated grade level: {grade:.2f}")

except FileNotFoundError:
    print("File not found. Create the text file and try again.")
