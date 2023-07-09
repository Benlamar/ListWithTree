import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainUI import Ui_MainWindow as MainWindowUI

from ConfigList import ConfigList
from ConfigTree import ConfigTree

class MainWindow(QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.ui = MainWindowUI()
        self.ui.setupUi(self)

        self.l_view = self.ui.listView
        self.t_view = self.ui.treeView
        self.ui.homeButton.clicked.connect(self.goToHome)
        self.ui.searchButton.clicked.connect(self.searchItem)
        self.ui.allButton.clicked.connect(self.goToHome)
        self.ui.shareButton.clicked.connect(self.showShare)

        # config listview here
        self.l_conf = ConfigList(self.l_view)

        # cofig treeView here
        self.t_conf = ConfigTree(self.t_view)
        self.t_conf.signal.currentNode.connect(self.currentNode)
        self.goToHome()
        
    def currentNode(self, current_node):
        self.ui.pathInput.setText(current_node.href)
        self.l_conf.setCurrentNode(current_node)

    def goToHome(self):
        root = self.t_conf.getRootNode()
        self.ui.pathInput.setText(root.href)
        self.l_conf.setCurrentNode(root)

    def searchItem(self):
        text = self.ui.searchInput.text()
        if text:
            search_item = self.t_conf.searchNode(text)
            
            self.l_conf.setCurrentNode(search_item)

    def showShare(self):
        share_item = self.t_conf.shareItems()
        print(share_item)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit()