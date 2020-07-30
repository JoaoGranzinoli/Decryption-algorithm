# Decryption-algorithm
This project was made so it could decrypt files that wore encrypted by a very similar encoding method as Caesar-Cipher, for that, a chart was provided containing values for all alphabetic letters and the last 5 values for punctuation, starting at 0 and going all the way till 30, also it was provided a text file containing a sentence and a unknow key value added to each letter, so to resolve this challenge, the algorithm used on the project was created to operate without receiving the key. It does that by analyzing the  file and getting the most repeated letter or punctuation and comparing with the most common letter on our alphabet, and if the result isn’t the expected one, the program runs with others common letters until the message is decrypt.

## Installing
It doesn’t require any previous installation to run the project, just clone the project and make sure you have python previously installed.

## Running the tests
It was provided a file with a encrypt text known as SecretMessage.txt, the following example is the result.

```
VOCE DECIFROU A MENSAGEM SECRETA. ESSE DESAFIO FAZ PARTE DA PRIMEIRA DO PROCESSO SELETIVO. DOCUMENTE SUA SOLUCAO, E NAO ESQUECA DE NOS ENTREGAR DENTRO DO PRAZO ESTABELECIDO. 

```
## Usage
To use Project after you install it,  open the project  with your preferable Editor or IDEs that`s compatible with python. Run the program.You will see that the test file is already being initialized. If you want to change the file that is being tested inside the program go to:  

    #Openning the file
    reading_encrypted_text = open('SecretMessage.txt', 'r')
    
 Main.py and change .text for any equivalent file compatible with the program.     
