from PySide6.QtWidgets import QListView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from CustomModel import Node

class ConfigList:
    def __init__(self, l_view:QListView) -> None:
        self.l_view = l_view
        self.model = QStandardItemModel()
        self.l_view.setModel(self.model)

    def setCurrentNode(self, current_node):
        self.model.clear()

        if isinstance(current_node, Node):
            for i in current_node.children:
                listItem = QStandardItem(i.icon(), i.name)
                self.model.appendRow(listItem)

        if isinstance(current_node, list):
            for i in current_node:
                listItem = QStandardItem(i.icon(), i.name)
                self.model.appendRow(listItem)
        