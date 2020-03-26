# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 345)
        Dialog.setStyleSheet("background-color: rgb(203, 255, 211);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.c1 = QtWidgets.QComboBox(Dialog)
        self.c1.setObjectName("c1")
        import sqlite3
        conn = sqlite3.connect('cricket.db')
        self.horizontalLayout.addWidget(self.c1)
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.c1.addItem(row[0])        
        conn.close()
        
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.c2 = QtWidgets.QComboBox(Dialog)
        self.c2.setObjectName("c2")
        self.c2.addItem("")
        self.c2.addItem("")
        self.c2.addItem("")
        self.c2.addItem("")
        self.horizontalLayout.addWidget(self.c2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.l1 = QtWidgets.QListWidget(Dialog)
        self.l1.setObjectName("l1")
        self.horizontalLayout_3.addWidget(self.l1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.l2 = QtWidgets.QListWidget(Dialog)
        self.l2.setObjectName("l2")
        self.horizontalLayout_3.addWidget(self.l2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.b = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.b.setFont(font)
        self.b.setStyleSheet("background-color: rgb(108, 255, 145);")
        self.b.setObjectName("b")
        self.horizontalLayout_4.addWidget(self.b)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.b.clicked.connect(self.press)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def press(self):
        
        import sqlite3
        con= sqlite3.connect('cricket.db')
        cur=con.cursor()
        team=self.c1.currentText()
        self.l1.clear()
        
        s="SELECT players from teams WHERE name='"+team+"';"
        cur=con.execute(s)
        row=cur.fetchone()
        player=row[0].split(',')
        self.l1.addItems(player)
        
        te=0
        
        self.l2.clear()
        
       
        for i in range(self.l1.count()-1):
            n=self.l1.item(i).text()
            cursor=con.execute("SELECT *from match WHERE player=='"+n+"'")
            row=cursor.fetchone()
           
            tt=0
            batscore=0
            bowlscore=0
            fieldscore=0
            batscore=int(row[1]/2)
            if batscore>=50:
                batscore+=5
            if batscore>=100:
                batscore+=10
            if row[1]>0:
                sr=(row[1]*100)/row[2]
                if sr>=80 and sr<100:
                    batscore+=2
                if sr>=100:
                    batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            
            
            bowlscore=row[8]*10
            if row[8]>=3:
                bowlscore=bowlscore+5
            if row[8]>=5:
                bowlscore=bowlscore+10
            if row[5]>0:
                er=row[7]/row[5]
                
                if er<=2: bowlscore=bowlscore+10
                if er>2 and er<=3.5:
                    bowlscore=bowlscore+7
                if er>3.5 and er<=4.5:
                    bowlscore=bowlscore+4
            
            fieldscore=(row[9]+row[10]+row[11])*10
            
            tt=batscore+bowlscore+fieldscore
            
            self.l2.addItem(str(tt))
            te=te+tt
       
        self.lineEdit.setText(str(te))
           
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "CHOOSE TEAM"))
        self.label.setText(_translate("Dialog", "CHOOSE MATCH"))
        self.c2.setItemText(0, _translate("Dialog", "Match1"))
        self.c2.setItemText(1, _translate("Dialog", "Match2"))
        self.c2.setItemText(2, _translate("Dialog", "Match3"))
        self.c2.setItemText(3, _translate("Dialog", "Match4"))
        self.label_4.setText(_translate("Dialog", "PLAYERS"))
        self.label_3.setText(_translate("Dialog", "SCORE"))
        self.b.setText(_translate("Dialog", "CALCULATE SCORE"))


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

