class Node:
    def __init__(self, data, nextAdd):
        self.data = data
        self.nextAdd = nextAdd
class linkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        self.head = Node(data, self.head)
        print(self.head)
    def insertValue(self, dataList):
        for i in dataList:
            self.insert(i)
    def printList(self):
        if self.head == None:
            print("Empty List")
        else:
            listData = ""
            while (self.head):
                print(self.head)
                print(self.head.data)
                # print(self.head.nextAdd)
                listData += self.head.data+ "-->"
                self.head = self.head.nextAdd
            print(self.head)
            print(listData)
st1 = linkedList()
st1.insert("Apple")
st1.insert("Apple1")
st1.insert("Apple2")
st1.insertValue(["Apple", "Apple2", "Apple3"])
st1.printList()