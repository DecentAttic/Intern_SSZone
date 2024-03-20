# This code is interpreitation of an Transposition cypher technique used in cryptography using 
# python


class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        num_columns = len(self.key)
        num_rows = -(-len(plaintext) // num_columns)  # Ceiling division to ensure all characters fit in grid

        # Create an empty grid
        grid = [[''] * num_columns for _ in range(num_rows)]

        # Fill in the grid with the plaintext
        for i, char in enumerate(plaintext):
            row = i // num_columns
            col = i % num_columns
            grid[row][col] = char

        # Create a list of ASCII values of key characters so as to arrange the coloums on basic of letters in keys 
        key_values = [ord(char) for char in self.key]

        # Sort key_values and get the indices of the sorted values 
        sorted_indices = sorted(range(len(key_values)), key=lambda k: key_values[k])

        # Create a string from the columns according to the sorted key indices and returns an encrypted version of the plain text
        encrypted_text = ''
        for col_index in sorted_indices:
            for row_index in range(num_rows):
                encrypted_text += grid[row_index][col_index]

        return encrypted_text

#instance creation and getting the necessary inputs for the program to run
key = input("Key for encryption:")  #Key for encryption
message = input("Message for encryption:")  #Plain text or message used for the encryption process
cipher = TranspositionCipher(key)   #Creating the instance
encrypted_message = cipher.encrypt(message) #calling the method inside the class Transposition cipher
print("Encrypted message:", encrypted_message)
