def count_words_in_file(file_path):
  with open(file_path, 'r') as file:
    text = file.read()
    words = text.split()
    return len(words)


#Test Case
def generate_test_function(file_path, expected_word_count):
  assert count_words_in_file(file_path) == expected_word_count


generate_test_function("data.txt", 15)
