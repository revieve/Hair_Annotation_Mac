import os

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtWidgets import QFileDialog


class Ui_Hair_Analysis(object):

    def __init__(self):
        super().__init__()
        self.imagenumber = 0

    def setupUi(self, Hair_Analysis):
        Hair_Analysis.setObjectName("Hair_Analysis")
        Hair_Analysis.resize(1134, 793)
        self.centralwidget = QtWidgets.QWidget(Hair_Analysis)
        self.centralwidget.setObjectName("centralwidget")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(0, 0, 1131, 551))
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("Image/R.png"))
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/Logo.png"),
                       QtGui.QIcon.Selected, QtGui.QIcon.On)
        Hair_Analysis.setWindowIcon(icon)



        #self.Previous = QtWidgets.QPushButton(self.centralwidget)
        #self.Previous.setGeometry(QtCore.QRect(20, 560, 75, 23))
        #self.Previous.setObjectName("Previous")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(1050, 560, 75, 23))
        self.Next.setObjectName("Next")
        self.Hair_Color = QtWidgets.QLabel(self.centralwidget)
        self.Hair_Color.setGeometry(QtCore.QRect(460, 590, 61, 21))
        self.Hair_Color.setObjectName("Hair_Color")
        self.Hair_Type = QtWidgets.QLabel(self.centralwidget)
        self.Hair_Type.setGeometry(QtCore.QRect(460, 620, 61, 21))
        self.Hair_Type.setObjectName("Hair_Type")
        self.Hair_Volume = QtWidgets.QLabel(self.centralwidget)
        self.Hair_Volume.setGeometry(QtCore.QRect(460, 650, 61, 21))
        self.Hair_Volume.setObjectName("Hair_Volume")
        self.Hair_Frizziness = QtWidgets.QLabel(self.centralwidget)
        self.Hair_Frizziness.setGeometry(QtCore.QRect(460, 680, 81, 21))
        self.Hair_Frizziness.setObjectName("Hair_Frizziness")
        self.Hair_Lusterness = QtWidgets.QLabel(self.centralwidget)
        self.Hair_Lusterness.setGeometry(QtCore.QRect(460, 710, 81, 21))
        self.Hair_Lusterness.setObjectName("Hair_Lusterness")
        self.Finish = QtWidgets.QPushButton(self.centralwidget)
        self.Finish.setGeometry(QtCore.QRect(900, 680, 221, 71))
        self.Finish.setObjectName("Finish")
        self.Filename = QtWidgets.QLabel(self.centralwidget)
        self.Filename.setGeometry(QtCore.QRect(240, 560, 611, 21))
        self.Filename.setObjectName("Filename")
        self.Hair_Color_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Hair_Color_comboBox.setGeometry(QtCore.QRect(560, 590, 121, 22))
        self.Hair_Color_comboBox.setObjectName("Hair_Color_comboBox")
        self.Hair_Color_comboBox.addItem("")
        self.Hair_Color_comboBox.addItem("")
        self.Hair_Color_comboBox.addItem("")
        self.Hair_Color_comboBox.addItem("")
        self.Hair_Color_comboBox.addItem("")
        self.Hair_Color_comboBox.addItem("")
        self.Hair_Type_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Hair_Type_comboBox.setGeometry(QtCore.QRect(560, 620, 121, 22))
        self.Hair_Type_comboBox.setObjectName("Hair_Type_comboBox")
        self.Hair_Type_comboBox.addItem("")
        self.Hair_Type_comboBox.addItem("")
        self.Hair_Type_comboBox.addItem("")
        self.Hair_Type_comboBox.addItem("")
        self.Hair_Type_comboBox.addItem("")
        self.Hair_Volume_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Hair_Volume_comboBox.setGeometry(QtCore.QRect(560, 650, 121, 22))
        self.Hair_Volume_comboBox.setObjectName("Hair_Volume_comboBox")
        self.Hair_Volume_comboBox.addItem("")
        self.Hair_Volume_comboBox.addItem("")
        self.Hair_Volume_comboBox.addItem("")
        self.Hair_Frizziness_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Hair_Frizziness_comboBox.setGeometry(QtCore.QRect(560, 680, 121, 22))
        self.Hair_Frizziness_comboBox.setObjectName("Hair_Frizziness_comboBox")
        self.Hair_Frizziness_comboBox.addItem("")
        self.Hair_Frizziness_comboBox.addItem("")
        self.Hair_Frizziness_comboBox.addItem("")
        self.Hair_Lusterness_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Hair_Lusterness_comboBox.setGeometry(QtCore.QRect(560, 710, 121, 22))
        self.Hair_Lusterness_comboBox.setObjectName("Hair_Lusterness_comboBox")
        self.Hair_Lusterness_comboBox.addItem("")
        self.Hair_Lusterness_comboBox.addItem("")
        self.Hair_Lusterness_comboBox.addItem("")
        self.Number_Text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Number_Text.setGeometry(QtCore.QRect(870, 590, 141, 31))
        self.Number_Text.setObjectName("Number_Text")
        self.Number_Text.setPlaceholderText("NULL")

        self.Number = QtWidgets.QLabel(self.centralwidget)
        self.Number.setGeometry(QtCore.QRect(800, 600, 47, 13))
        self.Number.setObjectName("Number")
        Hair_Analysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hair_Analysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Hair_Analysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hair_Analysis)
        self.statusbar.setObjectName("statusbar")
        Hair_Analysis.setStatusBar(self.statusbar)

        self.Source = QtWidgets.QAction(Hair_Analysis)
        self.Source.setObjectName("Source")
        self.Source.triggered.connect(self.openDir)

        self.Exit = QtWidgets.QAction(Hair_Analysis)
        self.Exit.setObjectName("Exit")
        self.Exit.triggered.connect(app.quit)

        self.Destination = QtWidgets.QAction(Hair_Analysis)
        self.Destination.setObjectName("Destination")
        self.Destination.triggered.connect(self.storeDir)

        self.menuFile.addAction(self.Source)
        self.menuFile.addAction(self.Destination)
        self.menuFile.addAction(self.Exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Hair_Analysis)
        QtCore.QMetaObject.connectSlotsByName(Hair_Analysis)
        self.Finish.clicked.connect(self.handle_first_input_text)
        self.Finish.clicked.connect(self.result)
        self.Next.clicked.connect(self.show_Next)
        self.Next.clicked.connect(self.clicked)
        # self.Previous.clicked.connect(self.show_Previous)
        # self.Previous.clicked.connect(self.clicked)

    def retranslateUi(self, Hair_Analysis):
        _translate = QtCore.QCoreApplication.translate
        Hair_Analysis.setWindowTitle(_translate("Hair_Analysis", "Hair Annotation Application"))
        #self.Previous.setText(_translate("Hair_Analysis", "Previous"))
        self.Next.setText(_translate("Hair_Analysis", "Next"))
        self.Hair_Color.setText(_translate("Hair_Analysis", "Hair_Color"))
        self.Hair_Type.setText(_translate("Hair_Analysis", "Hair_Type"))
        self.Hair_Volume.setText(_translate("Hair_Analysis", "Hair_Volume"))
        self.Hair_Frizziness.setText(_translate("Hair_Analysis", "Hair_Frizziness"))
        self.Hair_Lusterness.setText(_translate("Hair_Analysis", "Hair_Lusterness"))
        self.Finish.setText(_translate("Hair_Analysis", "Finish"))
        self.Filename.setText(_translate("Hair_Analysis", "Filename"))
        self.Hair_Color_comboBox.setItemText(0, _translate("Hair_Analysis", "Black"))
        self.Hair_Color_comboBox.setItemText(1, _translate("Hair_Analysis", "Brown"))
        self.Hair_Color_comboBox.setItemText(2, _translate("Hair_Analysis", "Blond"))
        self.Hair_Color_comboBox.setItemText(3, _translate("Hair_Analysis", "Gray"))
        self.Hair_Color_comboBox.setItemText(4, _translate("Hair_Analysis", "Red"))
        self.Hair_Color_comboBox.setItemText(5, _translate("Hair_Analysis", "Others"))
        self.Hair_Type_comboBox.setItemText(0, _translate("Hair_Analysis", "Straight"))
        self.Hair_Type_comboBox.setItemText(1, _translate("Hair_Analysis", "Wavy"))
        self.Hair_Type_comboBox.setItemText(2, _translate("Hair_Analysis", "Curly"))
        self.Hair_Type_comboBox.setItemText(3, _translate("Hair_Analysis", "Coily"))
        self.Hair_Type_comboBox.setItemText(4, _translate("Hair_Analysis", "Others"))
        self.Hair_Volume_comboBox.setItemText(0, _translate("Hair_Analysis", "Low_Volume"))
        self.Hair_Volume_comboBox.setItemText(1, _translate("Hair_Analysis", "Average_Volume"))
        self.Hair_Volume_comboBox.setItemText(2, _translate("Hair_Analysis", "High_Volume"))
        self.Hair_Frizziness_comboBox.setItemText(0, _translate("Hair_Analysis", "Low_Frizziness"))
        self.Hair_Frizziness_comboBox.setItemText(1, _translate("Hair_Analysis", "Average_Frizziness"))
        self.Hair_Frizziness_comboBox.setItemText(2, _translate("Hair_Analysis", "High_Frizziness"))
        self.Hair_Lusterness_comboBox.setItemText(0, _translate("Hair_Analysis", "Low_Lusterness"))
        self.Hair_Lusterness_comboBox.setItemText(1, _translate("Hair_Analysis", "Average_Lusterness"))
        self.Hair_Lusterness_comboBox.setItemText(2, _translate("Hair_Analysis", "High_Lusterness"))
        self.Number.setText(_translate("Hair_Analysis", "Number"))
        self.menuFile.setTitle(_translate("Hair_Analysis", "File"))
        self.Source.setText(_translate("Hair_Analysis", "Source"))
        self.Exit.setText(_translate("Hair_Analysis", "Exit"))
        self.Destination.setText(_translate("Hair_Analysis", "Destination"))


    def handle_first_input_text(self):
        self.textEdit = self.Number_Text.toPlainText()
        #print( "textEdit", textEdit )

    def result(self):
        #print("Hair_Color :", self.Hair_Color_comboBox.currentText())
        #print("Hair_Type :", self.Hair_Type_comboBox.currentText())
        #print("Hair_Volume :", self.Hair_Volume_comboBox.currentText())
        #print("Hair_Frizziness :", self.Hair_Frizziness_comboBox.currentText())
        #print("Hair_Lusterness:", self.Hair_Lusterness_comboBox.currentText())
        self.Fname = str(self.Hair_Color_comboBox.currentText()) + "_" + str(self.Hair_Type_comboBox.currentText()) + "_" +  str(self.Hair_Volume_comboBox.currentText()) + "_" + str(self.Hair_Frizziness_comboBox.currentText()) + "_" + str(self.Hair_Lusterness_comboBox.currentText())
        if(self.imagenumber < 0):
            print("Cannot Save the Image")
        else:
            #self.FPname = str(self.imagenumber)+ "_" + str(self.Fname) + ".png"
            self.FPname = self.textEdit + "_" + str(self.Fname) + ".png"
            #print("Final Name :", self.FPname)
            img = cv2.imread(self.input_path)
            #img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            name = self.OPath + "/" + self.FPname
            cv2.imwrite(name, img)

    def show_Next(self):
        path = self.Path
        image_path = os.listdir(path)
        #print(image_path)
        # create the full input path and read the file
        self.input_path = path + "/" + image_path[self.imagenumber]
        #image_to_rotate = ndimage.imread(input_path)
        self.Image.setPixmap(QtGui.QPixmap(self.input_path))
        #self.Image.adjustSize()
        self.imagenumber = self.imagenumber + 1
        #print("self.imagenumber:", self.imagenumber)
        #print(self.input_path)


    def show_Previous(self):
        #self.Image.setPixmap(QtGui.QPixmap("D:/Revieve_Dataset/Dataset/Batch 1/00003[M1BrBr].png"))
        path = self.Path
        image_path = os.listdir(path)
        # print(image_path)
        # create the full input path and read the file
        self.input_path = path + "/" + image_path[self.imagenumber]
        # image_to_rotate = ndimage.imread(input_path)
        self.Image.setPixmap(QtGui.QPixmap(self.input_path))
        self.imagenumber = self.imagenumber - 1
        #print("self.imagenumber:", self.imagenumber)
        #print(self.input_path)

    def clicked(self):
        self.Filename.setText(str(self.input_path))
        self.update()

    def update(self):
        self.Filename.adjustSize()

    def openDir(self):
        #imagePath, _ = QFileDialog.getOpenFileUrl()
        self.Path = QFileDialog.getExistingDirectory()#(self, "Select Directory"))
        #print("imagePath :", self.Path)

    def storeDir(self):
        #imagePath, _ = QFileDialog.getOpenFileUrl()
        self.OPath = QFileDialog.getExistingDirectory()#(self, "Select Directory"))
        #print("imagePath :", self.OPath)




if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    Hair_Analysis = QtWidgets.QMainWindow()
    ui = Ui_Hair_Analysis()
    ui.setupUi(Hair_Analysis)
    Hair_Analysis.show()
    #Hair_Analysis.start()
    sys.exit(app.exec_())