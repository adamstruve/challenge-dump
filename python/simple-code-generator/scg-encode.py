letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", ",", "!", "?", ":", ";", "-", "_", "(", ")", "[", "]", "{", "}", "/", "\\", "\"", "'", "`", "~", "@", "#", "$", "%", "^", "&", "*", "+", "=", "|", "<", ">")
random_letters = ('6', 'H', 'W', '&', '}', 'V', 'U', 'Y', '-', "'", 'S', '+', 'X', 'E', '>', 'M', '?', '<', '%', 'O', '#', '{', 'K', 'L', '/', ')', 'I', '*', '@', ':', 'B', '$', '3', '1', 'T', '0', '~', '`', 'F', 'A', '!', ',', 'Z', '"', ']', '4', 'R', 'D', '\\', '|', '=', '^', 'G', '9', '5', '7', 'Q', 'C', '8', ';', '[', '2', ' ', 'N', '.', 'P', '(', '_', 'J')

original = input("Enter the message you want to code: ")
original = original.upper()
original = [*original]
coded_message = ""

for i in range(len(original)):
    coded_message += random_letters[letters.index(original[i])]
print(f"Coded message: {coded_message}")