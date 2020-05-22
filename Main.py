"""
In this algorithm we aim to break the encryption offered by SecretMessage and others encryptions of the same kind
using the provided instructions.

"""


#Here we difine the letters and signs we are going to use to do our comparisons
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.,;!?"
SPACE = "# \n"
SINS = ".,;!?"

#These are the most used letters in the portuguese lenguage in order
most_used_letters =["A","E","O","S","R","I","N","M","U","T","C","L","P","V"]

def decrypt(encrypted_text):
    """
    This function decrypts the encrypted text without the key using a distribution
    analysis and returns it.
    :param encrypted_text:
    :return:
    """
    i = False
    cont = 0
    #This while aims to test the letters of the most_used_letters list tryng to find a fitting key
    while i == False:
        key = find_Key(encrypted_text, ALPHABET.find(most_used_letters[cont]))
        decrypt_text = ""
        for letter in encrypted_text:
            if letter in SPACE:
                decrypt_text+=" "
                continue
            crypted_word = ALPHABET.find(letter)
            decrypted_word = find_word(crypted_word,key)
            decrypt_text += ALPHABET[decrypted_word]

        #If returns false the key is changed and the process restart
        i =test_decrypted_text(decrypt_text)
        if cont < len(most_used_letters):
            cont += 1
        else:
            return "Error"

    return decrypt_text

def find_Key(encrypted_text, index_letter):
    #The value of the letter is passed as index
    most_common_letter_index = index_letter

    #Calculate distribution
    letter_distribution_dict = letter_distribution(encrypted_text)

    #Get the most used letters
    ordened_distribution_dict = sorted(letter_distribution_dict,key=letter_distribution_dict.get,reverse =True)

    #Use most_common_letter with the letter that appeared the most in the text to get the key using the following formula
    key = 31 - ALPHABET.find(ordened_distribution_dict[0]) + (most_common_letter_index+1)
    if key > 31:
        key = key - 31
    return key

def find_word(encrypted_word, key):
    """
    The function find_word is used to decrypt the word using the newly founded key,
    resulting in the real supposed meaning of the word.
    :param encrypted_word:
    :param key:
    :return:
    """
    decrypt_word = encrypted_word + key
    #If the value of the word is higher than the last position it goes back to the beginning
    if(decrypt_word > 30):
        decrypt_word = decrypt_word -31

    #After the sum of the word with the key we need to go back one position, because "A" assumes the value of 0
    return decrypt_word-1

def letter_distribution(encrypted_text):
    """
    Here we do a simple distribution, counting the most used letters, putting inside a dictionary
    and returning the dictionary.
    :param encrypted_text:
    :return:
    """
    letter_distribution_dict = {}
    for letter in encrypted_text:
        if letter in SPACE:
            continue
        if letter not in letter_distribution_dict:
            letter_distribution_dict[letter] = 1
        else:
            letter_distribution_dict[letter] += 1

    return letter_distribution_dict

def test_decrypted_text(decrypt_text):
    """
    In this function we test the newly founded decrypted text seeing if some punctuation
    is bad placed in the text, returning true or false based on the analysis.
    :param decrypt_text:
    :return:
    """
    cont = 0
    for letter in decrypt_text:
        if letter in SINS and cont+1<len(decrypt_text):
            #
            if decrypt_text[cont+1] != " ":
                return False
        cont+=1
    return True

if __name__ == "__main__":
    #Openning the file
    reading_encrypted_text = open('SecretMessage.txt', 'r')

    #Reading the file
    reading_encrypted_text = reading_encrypted_text.readlines()

    #Concatenating the Strings and putting the result inside encrypted_text
    encrypted_text = ""
    for frase in reading_encrypted_text:
        encrypted_text+= frase
    print(decrypt(encrypted_text))



