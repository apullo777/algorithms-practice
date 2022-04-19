from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

def personIsSeller(name):
    return name[-1] == 'm'

def search(name):
    searchQueue = deque()
    searchQueue += graph[name]
    searched = []
    while searchQueue:
        person = searchQueue.popleft()
        if not person in searched:
            if personIsSeller(person):
                print(person + " is a mango seller!")
                return True
            else:
                searchQueue += graph[person]
                searched.append(person)
    return False

search("you")


