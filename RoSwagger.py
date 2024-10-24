# Made by RoSwagger Developers at roswagger.com
# Visit our creator program here for unrestricted access for free at
# discord.roswagger.com


import requests

def Swagger(endpoint, username):
return requests.get(f"https://roswagger.com/get/{endpoint}/{username}").json() if requests.get else "RoSwagger may be in Testing Mode, else it may be your Internet."


def all(username): return Swagger('all', username)
def userId(username): return Swagger('userId', username)
def lastOnline(username): return Swagger('lastOnline', username)
def creationDate(username): return Swagger('creationDate', username)
def thumbnail(username): return Swagger('thumbnail', username)
def rap(username): return Swagger('rap', username)
def verified(username): return Swagger('verified', username)
def pastUsernames(username): return Swagger('pastUsernames', username)
