from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide6.QtGui import QIcon

class Node:
    def __init__(self, name, href, isfile=None, icon=None, shared=False, parent=None):
        self.name = name
        self.href = href
        self.isfile = isfile
        self._icon = icon
        self.shared = shared
        self.parent = parent
        self.children = []

    def appendChild(self, child):
        child.parent = self
        self.children.append(child)

    def child(self, row):
        return self.children[row]

    def childCount(self):
        return len(self.children)

    def columnCount(self):
        return 1

    def data(self, column):
        if column == 0:
            if self.parent is None:
                return "Title"  # Modify this to set the desired title
            return self.name
        return None
    
    def icon(self):
        return QIcon(self._icon)


    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0
    
    def currentParent(self):
        return self


DATA = [
    {"href":"/", "isfile":False, "icon":"folder.png",  "shared":False},
    {"href":"/Documents", "isfile":False, "icon":"folder.png",  "shared":False},
    {"href":"/Documents/Word files", "isfile":False, "icon":"folder.png",  "shared":False},
    {"href":"/Documents/Word files/sample.docx", "isfile":True, "icon":"file.png",  "shared":False},
    {"href":"/Documents/Word files/dog.other", "isfile":True, "icon":"file.png",  "shared":False},
    {"href":"/Documents/Word files/cat.docx", "isfile":True, "icon":"file.png", "shared":False},
    {"href":"/Documents/Word files/dog.docx", "isfile":True, "icon":"file.png",  "shared":False},
    {"href":"/Documents/Word files/penguine.docx", "isfile":True, "icon":"file.png",  "shared":False},
    {"href":"/Music", "isfile":False, "icon":"folder.png",  "shared":True},
    {"href":"/Music/sample.mp3", "isfile":True, "icon":"file.png",  "shared":True},
    {"href":"/Music/cat.mp3", "isfile":True, "icon":"file.png",  "shared":True},
    {"href":"/Music/dog.mp3", "isfile":True, "icon":"file.png",  "shared":True},
    {"href":"/Music/penguine.mp3", "isfile":True, "icon":"file.png",  "shared":True},
    {"href":"/Video", "isfile":False, "icon":"folder.png",  "shared":False},
    {"href":"/Video/Shorts", "isfile":False, "icon":"folder.png",  "shared":False},
    {"href":"/Video/Medium", "isfile":False, "icon":"folder.png",  "shared":False},
    {"href":"/sample.other", "isfile":True, "icon":"file.png",  "shared":False},
    {"href":"/cat.other", "isfile":True, "icon":"file.png" , "shared":True},
    {"href":"/dog.other", "isfile":True, "icon":"file.png",  "shared":False},
    {"href":"/penguine.other", "isfile":True, "icon":"file.png",  "shared":False}
]

class CustomModel(QAbstractItemModel):
    def __init__(self, data=DATA, parent=None):
        super().__init__(parent)
        self.rootItem = None
        self.buildTree(data, self.rootItem)

    def buildTree(self, data, parent=None):
        file_paths = [item['href'] for item in data]
    
        if not self.rootItem:
            self.rootItem = Node("/", data[0]['href'], data[0]['isfile'], data[0]['icon'], data[0]['shared'])
            parent = self.rootItem

        # the children are here
        for path in range(1,len(file_paths)):
            directories = file_paths[path].split("/")[1:]  # Exclude the root directory
            current_node = parent
            for directory in directories:
                found_child = None
                for child in current_node.children:
                    if child.name == directory:
                        found_child = child
                        break
                if found_child is None:
                    new_node = Node(directory, data[path]['href'], data[path]['isfile'], data[path]['icon'], data[0]['shared'])
                    current_node.appendChild(new_node)
                    current_node = new_node
                else:
                    current_node = found_child

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == Qt.DisplayRole:
            if index.column() == 0:
                return item.data(index.column())
        
        if role == Qt.DecorationRole:
            if index.column() == 0:
                return item.icon()
        return None
    
    def _searchNode(self, node, searched, keyword, shared = False):
        if node.name == keyword:
            searched.append(node)
        else:
            for child in node.children:
                self._searchNode(keyword, child, searched)

    def search(self, keyword, shared = False, node = None):
        if node == None:
            node = self.rootItem

        search_item = []
        if self.rootItem:
            self._searchNode(node, search_item, keyword, shared)
            return search_item