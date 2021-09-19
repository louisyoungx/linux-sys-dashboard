# head.next.next.value

class LinkNode ():
    def __init__(self, next, value=None):
        self.next = LinkNode
        self.value = value

class LinkList ():

     def __init__(self, Array):
         self.linkList = []
         for i in range(len(Array)):
             thisLink = LinkNode(i+1, Array[i])
             self.linkList.append(thisLink)
         self.head = self.linkList[0]


def createLinkList(Array):
    linkList = []
    head = {}
    for i in range(len(Array)):
        linkNode = {}
        linkNode['next'] = i + 1
        linkNode['value'] = Array[i]
        linkList.append(linkNode)
    return linkList
    # [{'next': 1, 'value': 1}, {'next': 2, 'value': 2}, {'next': 3, 'value': 3}]

if __name__ == '__main__':
    Array = [1,2,3]
    link = LinkList(Array)
    link.head.next.next.value
