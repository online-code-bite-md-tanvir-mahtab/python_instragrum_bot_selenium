# edge_path = "G:\edgedriver_win64\msedgedriver.exe"
from Insertragrambot import Instragram

if __name__ == '__main__':
    edge_path = "G:\edgedriver_win64\msedgedriver.exe"
    bot = Instragram(edge_path=edge_path)
    # calling the methods
    bot.login()
    bot.find_flower()
    bot.follower()