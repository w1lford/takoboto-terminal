import requests
from bs4 import BeautifulSoup


while True:
    word = input("")
    response = requests.get(f"https://takoboto.jp/?ajax=1&ajaxq={word}").content
    soup = BeautifulSoup(response,'html.parser')
    defns = []

    #Each ResultDiv is a definition
    for defn in soup.find_all(class_="ResultDiv"):
        lines = []
        for line in defn.find_all('div'):
            if not(line.a) and line.get_text() != "":
                lines.append(line.get_text())
        defns.append(lines)
    #Print definitions in reverse order
    while (len(defns) > 0):
        d = defns.pop()
        for i in range(len(d)):    
            print(d[i])
        if(len(defns) > 0):
            print("")