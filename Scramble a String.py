print("💬String Scrambler💬")

def single_string():
    string = input("Enter a single word: ")
    scrambled = string[::2] + string[1::2]
    return scrambled


print(single_string())