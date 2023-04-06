from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        
        #BACKGROUND 
        bg_label = QLabel(self)
        bg_pixmap = QPixmap("./src/images/hud_.png")
        self.resize(1366,697)
        bg_label.setPixmap(bg_pixmap)
        bg_label.setGeometry(0, 0, bg_pixmap.width(), bg_pixmap.height())
        
        #FONT SETTING AND TITTLES 
        
        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
        font1 = QtGui.QFont(fontstr)
        font_ = QtGui.QFont(fontstr)
        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/neuropolitical rg.ttf")
        fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]

        font_.setPointSize(15)
        font_.setBold(False)
        font_.setItalic(False)
        font_.setWeight(5)
        self.contact = QtWidgets.QLabel(self)
        self.contact.setText("STAFF LOGIN")
        self.contact.setObjectName("text_contact")
        self.contact.setGeometry(QtCore.QRect(900,80,600,100))
        self.contact.setStyleSheet("#text_contact{background:transparent;color:rgb(99, 255, 255);}")
        self.contact.setFont(font_)
        self.shadow_con = QtWidgets.QGraphicsDropShadowEffect(self.contact,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.contact.setGraphicsEffect(self.shadow_con)
        self.gen = QtWidgets.QLabel(self)
        self.gen.setText("ADMIN lOGIN")  
        self.gen.setObjectName("text_contact")
        self.gen.setGeometry(QtCore.QRect(290,80,600,100))
        self.gen.setStyleSheet("#text_contact{background:transparent;color:rgb(99, 255, 255);}")
        self.gen.setFont(font_)
        self.shadow_con = QtWidgets.QGraphicsDropShadowEffect(self.gen,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.gen.setGraphicsEffect(self.shadow_con)
        
        #TEXTBOXES , IMAGE AND BUTTONS FOR ADMIN 

        
        #staff logo
        self.id_upload = QtWidgets.QPushButton(self)
        self.id_upload.setEnabled(True)
        self.id_upload.setGeometry(QtCore.QRect(800, 130, 200, 200))
        self.shadow_ = QtWidgets.QGraphicsDropShadowEffect(self.id_upload,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.id_upload.setObjectName("id_upload")
        self.id_upload.setStyleSheet("#id_upload{background:transparent;border-image:url('./src/images/image-1.png');}")
        self.id_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.id_upload.setMouseTracking(True)
        self.id_upload.setGraphicsEffect(self.shadow_)

        #admin logo
        self.id_upload = QtWidgets.QPushButton(self)
        self.id_upload.setEnabled(True)
        self.id_upload.setGeometry(QtCore.QRect(200, 130, 200, 200))
        self.shadow_ = QtWidgets.QGraphicsDropShadowEffect(self.id_upload,blurRadius=40,xOffset=1,yOffset=1,color=QtGui.QColor(7, 179, 150))
        self.id_upload.setObjectName("id_upload")
        self.id_upload.setStyleSheet("#id_upload{background:transparent;border-image:url('./src/images/image-1.png');}")
        self.id_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.id_upload.setMouseTracking(True)
        self.id_upload.setGraphicsEffect(self.shadow_)
        
        #username for admin 
        self.usradmin = QtWidgets.QLineEdit(self)
        self.usradmin.setGeometry(QtCore.QRect(370, 180, 201, 31))
        self.usradmin.setObjectName("usradmin")
        self.usradmin.setStyleSheet("#usradmin:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#usradmin{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.usradmin.setFont(font1)
        self.usradmin.setPlaceholderText("Username")

        #password for admin
        self.pssadmin = QtWidgets.QLineEdit(self)
        self.pssadmin.setGeometry(QtCore.QRect(370, 250, 201, 31))
        self.pssadmin.setObjectName("pssadmin")
        self.pssadmin.setStyleSheet("#pssadmin:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#pssadmin{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.pssadmin.setFont(font1)
        self.pssadmin.setPlaceholderText("Password")

        #username for staff
        self.usrstaff = QtWidgets.QLineEdit(self)
        self.usrstaff.setGeometry(QtCore.QRect(970, 180, 201, 31))
        self.usrstaff.setObjectName("usrstaff")
        self.usrstaff.setStyleSheet("#usrstaff:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#usrstaff{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.usrstaff.setFont(font1)
        self.usrstaff.setPlaceholderText("Username")

        #password for staff
        self.usrstaff = QtWidgets.QLineEdit(self)
        self.usrstaff.setGeometry(QtCore.QRect(970, 250, 201, 31))
        self.usrstaff.setObjectName("usrstaff")
        self.usrstaff.setStyleSheet("#usrstaff:hover {background: rgba(0, 214, 252, 0.17);border-radius: 5px;}#usrstaff{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-radius:4px;border-color:rgb(20, 182, 216);}")
        self.usrstaff.setFont(font1)
        self.usrstaff.setPlaceholderText("Password")
        
        
        # STAFF LOGIN BUTTON 
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(1000, 300, 100, 35))
        font_.setPointSize(12)
        self.pushButton.setText("Login")

        #self.pushButton.clicked.connect(self.add)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setFont(font_)
        self.pushButton.setStyleSheet("#pushButton:hover {background: rgba(0, 214, 252, 0.17);}#pushButton{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-top-right-radius:10px;border-bottom-left-radius:10px;border-color:rgb(20, 182, 216);}")
        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.pushButton,blurRadius=20,xOffset=1,yOffset=1)
        self.pushButton.setGraphicsEffect(self.shadow1)

        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
                    
                    
        # ADMIN LOGIN BUTTON 
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(400, 300, 100, 35))
        self.pushButton.setText("Login")
        font_.setPointSize(12)
        #self.pushButton.clicked.connect(self.add)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setFont(font_)
        self.pushButton.setStyleSheet("#pushButton:hover {background: rgba(0, 214, 252, 0.17);}#pushButton{background: rgba(0, 214, 252, 0.1);padding:5px;color:rgb(99, 255, 255);border: 1px solid rgb(20, 182, 216);border-top-right-radius:10px;border-bottom-left-radius:10px;border-color:rgb(20, 182, 216);}")
        self.shadow1 = QtWidgets.QGraphicsDropShadowEffect(self.pushButton,blurRadius=20,xOffset=1,yOffset=1)
        self.pushButton.setGraphicsEffect(self.shadow1)

        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Polaris", "Polaris"))
        


