letter = '''dear <|NAME|>,
You are selected!
YOU ARE GOOD CODER 
THANK YOU
Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter your DATE\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)

#follow for more @arushsengar495