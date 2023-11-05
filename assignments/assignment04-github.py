# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name
# The program should then commit those changes and push the file back to the repository.
# I do not need to see your keys (see lab2, to follow)
# Handup: Save the program as assignment04-github.py to the same repository you uploaded the xml to
# Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.

import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]

# use your own key
g = Github(apikey)
# token generated from gitbuh and stored in config.py which is added to a .gitignore file

repo = g.get_repo("mhmdmahdi/aprivateone")
# print(repo.clone_url)
# check

fileInfo = repo.get_contents("assignment04private.txt")
urlOfFile = fileInfo.download_url
# print (urlOfFile)
# check

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)
# prints the contents of the txt file

contentOfFile = contentOfFile.replace("Andrew", "Mohammed")
print(contentOfFile)
# Replace "Andrew" with "Mohammed" in the content
