from random import choice

class Say:
    '''
    A cow helper function to say something

    Parameters:
    -----------
    something:  A string to say in console
    '''
    def __init__(self, something:str):
        self.something = something
        
    
    def cow_says_good(self) -> str:
        """
        A method to say something good/positive in console
        """
        emoji_list = ['😉','🛐','🙈','🐶','🥇','🤖']
        """

        """
        lenght = len(self.something)
        print(" _" + lenght * "_" + "_ ")
        print("< " + self.something + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print(f"            (__)\ good{choice(emoji_list)} )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")

    def cow_says_error(self) -> str:
        '''
        A method to say something error/negative in console
        '''
        emoji_list = ['😭','❌','😬','🌑','💔','🙈']
        lenght = len(self.something)
        print(" _" + lenght * "_" + "_ ")
        print("< " + self.something + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print(f"            (__)\ good{choice(emoji_list)} )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")