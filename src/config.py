import os

TOKEN = os.getenv("TOKEN")
NICKNAME = os.getenv("NICKNAME")
CHANNELS = os.getenv("CHANNELS").split(",")
BOTS = os.getenv("BOTS").split(",")
BOTS.append(NICKNAME)
