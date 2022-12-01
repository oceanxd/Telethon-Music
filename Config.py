import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16051908"))
    API_HASH = os.environ.get("API_HASH", "abf9b83f9ca40cf9f5ba9bf6e6afaa8b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5704393118:AAGuUyVNJ8ZpyhuAy_H8SvpC7oclJMhxaqo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLkBu7Um62VDHVD-dLFyqzTFKl8hD28v1Qpb7Z6tM3mphIXcBlsbIhu8kuymkAT2NwhuPuhF1ztpFm_xk6v2yjsQcAimRNN81V1cuoLb0LadSz1lDQ5_e5IylV7jvrmXzi2kFbFMIk1H4Bl-rBCDAu_5M8oGIoIk06tQm6ebgT8X474xiJMrmP5ujAJ-UX2Kc0qsIpoXq3iOcfe2bdXWuOOYew9q5BKw9l61SWgPGcvE_ay47X33C55P0VnNeivkc_GJbpE63ydWiHJct__-6SCWKCFZev77mjT1uhzZfYhAMZnB9GB8GSNANVDg639LE22JS5ijny1FlBlc9W7K_2XI0Mk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TDNMUSICBOT")
    SUPPORT = os.environ.get("SUPPORT", "TDN_CHAT") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "THE_DRAGON_NETWORK_OFFICIAL") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5486649568")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
