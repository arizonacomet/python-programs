#check for vowels
def check_vowels(ch):
    if(ch=="a" or ch=="A" or ch=="E" or ch=="e" or ch=="I" or ch=="i" or ch=="O" or ch=="o" or ch=="U" or ch=="u"):
        return True
    else:
        return False
ch=input("Enter a vowel : ")
while(not ch.isalpha()):
    ch=input("Enter a valid character : ")
if(check_vowels(ch)):
        print("YAY!!! Good Job you have entered a vowel correctly")
else:
        print("SORRY!! you have entered a consonant")


