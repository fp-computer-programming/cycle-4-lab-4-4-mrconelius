word = "flibbertigibbet"
index_of_t = word.find("t")
if index_of_t != -1 and index_of_t < len(word) - 1:
    letter_after_t = word[index_of_t + 1]
    print("Letter immediately following the first 't':")
first_name_lowercase = "matt"
first_name_uppercase = first_name_lowercase.upper()
print("Uppercase first name:", first_name_uppercase)
sentence = "I wish, I wish, I was a fish."
split_sentence = sentence.split(", ")
print("Split sentence:", split_sentence)