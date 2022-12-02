# if the letters of both words are the same it prints the text, if not the pass

def animal_crackers(text):
    letters = text.split()
    if letters[0][0] == letters[1][0]:
        print(text)
    else:
        pass


animal_crackers('Crazy Kangaroo')