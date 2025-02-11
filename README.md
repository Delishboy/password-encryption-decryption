# password-encryption-decryption
this is a simple text encryption/decryption process that uses seeds to encrypt and then come back to the encryption and be able to decrypt it.
how it works:
  encyption:
      there are 2 lists who hold all the characaters available(numbers, letters and special characaters), while the first list is in order(1234...abcd...!@#$), and the other list is shuffled (the shuffle is randomized based on the passowrd[seed] that the                    users inputs)
      so after the user inputs the password or in other words the set seed, and then inputs the massage he wants to encypt, the code replaces each letter in the in the message with the letters that are in the shuffled list.
      how it does it? so first, lets say the message is "hello", the code checks what place in the unshuffled list the characater "h" is in, so lets say its in the 7th position of that list, after it does that, the code goes to the shuffled list
      and checks which letter is in the 7th place too, after its done checking (lets say that the 7th letter is q), it replces the letter in the message with the shuffled letter, so for now the message will be "qello", and the code continues to do that
      for each letter untill its fully replaced.
  
  decryption:
      if the user wants to decrypt the massage (he enters d for decryption), the user needs to put the passowrd that he set for the encypted message, after that the code gets the seed that the encryption was done in and the shuffled list is saved
      in the same exact order that the message was encrypted in, because of that, the only thing left to do it to reverse the exact same process that was done with encryption, (look up what's the letters potions in both lists and then just replace them)
      after that process is done the message is fully decrypted.

conclusion: 
    this code is quite simple yet effective for message encytpion and decryption.
    allthough there are some flaws to the code such as the password could be brute forced as for the use of importing the random funcion in python and also the no checking for if the password is secured.
