from CustomModel import CustomModel
from PySide6.QtWidgets import QTreeView
from PySide6.QtCore import Signal, QObject

class Signals(QObject):
    currentNode = Signal(object)

class ConfigTree:
    def __init__(self, t_view:QTreeView) -> None:
        self.t_view = t_view
        self.model = CustomModel()
        self.t_view.setModel(self.model)

        self.t_view.clicked.connect(self.itemClicked)
        
        self.signal = Signals()

    def itemClicked(self, index):
        item = index.internalPointer()
        if not item.isfile:
            self.signal.currentNode.emit(item)
        
    def getRootNode(self):
        return self.model.rootItem
    
    def searchNode(self, keyword, shared = False):
        searchedNode = self.model.search( keyword, shared = shared)
        return searchedNode