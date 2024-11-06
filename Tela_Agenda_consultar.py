# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Agenda_consultar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class tela_agenda_consultar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 513)
        MainWindow.setWindowOpacity(5.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-20, -10, 891, 151))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.text_hospital = QtWidgets.QLabel(self.frame_2)
        self.text_hospital.setGeometry(QtCore.QRect(230, 20, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.text_hospital.setFont(font)
        self.text_hospital.setObjectName("text_hospital")
        self.text_segun = QtWidgets.QLabel(self.frame_2)
        self.text_segun.setGeometry(QtCore.QRect(260, 80, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.text_segun.setFont(font)
        self.text_segun.setObjectName("text_segun")
        self.img_logo = QtWidgets.QLabel(self.frame_2)
        self.img_logo.setGeometry(QtCore.QRect(90, 20, 131, 121))
        self.img_logo.setText("")
        self.img_logo.setPixmap(QtGui.QPixmap("img/LOGO.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setObjectName("img_logo")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 140, 871, 571))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border -radius: 50px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.text_agendacon = QtWidgets.QLabel(self.frame)
        self.text_agendacon.setGeometry(QtCore.QRect(320, 20, 231, 31))
        self.text_agendacon.setObjectName("text_agendacon")
        self.text_nome = QtWidgets.QLabel(self.frame)
        self.text_nome.setGeometry(QtCore.QRect(170, 100, 81, 20))
        self.text_nome.setObjectName("text_nome")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nome.setGeometry(QtCore.QRect(240, 100, 571, 22))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.text_n_medico = QtWidgets.QLabel(self.frame)
        self.text_n_medico.setGeometry(QtCore.QRect(170, 149, 181, 21))
        self.text_n_medico.setObjectName("text_n_medico")
        self.lineEdit_n_medico = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_n_medico.setGeometry(QtCore.QRect(350, 150, 461, 22))
        self.lineEdit_n_medico.setObjectName("lineEdit_n_medico")
        self.text_data = QtWidgets.QLabel(self.frame)
        self.text_data.setGeometry(QtCore.QRect(160, 199, 61, 21))
        self.text_data.setObjectName("text_data")
        self.dateEdit_data = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_data.setGeometry(QtCore.QRect(220, 200, 131, 22))
        self.dateEdit_data.setObjectName("dateEdit_data")
        self.text_horario = QtWidgets.QLabel(self.frame)
        self.text_horario.setGeometry(QtCore.QRect(370, 200, 81, 21))
        self.text_horario.setObjectName("text_horario")
        self.timeEdit_horario = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit_horario.setGeometry(QtCore.QRect(460, 200, 161, 22))
        self.timeEdit_horario.setObjectName("timeEdit_horario")
        self.text_cpf = QtWidgets.QLabel(self.frame)
        self.text_cpf.setGeometry(QtCore.QRect(640, 200, 51, 21))
        self.text_cpf.setObjectName("text_cpf")
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(690, 200, 121, 22))
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.botao_marcar = QtWidgets.QPushButton(self.frame)
        self.botao_marcar.setGeometry(QtCore.QRect(370, 290, 131, 41))
        self.botao_marcar.setObjectName("botao_marcar")
        self.botao_fechar = QtWidgets.QPushButton(self.frame)
        self.botao_fechar.setGeometry(QtCore.QRect(550, 290, 131, 41))
        self.botao_fechar.setObjectName("botao_fechar")
        self.img_consulta = QtWidgets.QLabel(self.frame)
        self.img_consulta.setGeometry(QtCore.QRect(20, 80, 141, 151))
        self.img_consulta.setText("")
        self.img_consulta.setPixmap(QtGui.QPixmap("img/paciente (2).png"))
        self.img_consulta.setScaledContents(True)
        self.img_consulta.setObjectName("img_consulta")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda Consulta"))
        self.text_hospital.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">HOSPITAL JOÃO AMOÊDO</span></p></body></html>"))
        self.text_segun.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">SALVANDO VIDAS À 20 ANOS</span></p></body></html>"))
        self.text_agendacon.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">AGENDA CONSULTA</span></p></body></html>"))
        self.text_nome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome:</span></p></body></html>"))
        self.text_n_medico.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome do Médico:</span></p></body></html>"))
        self.text_data.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Data:</span></p></body></html>"))
        self.text_horario.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Horário:</span></p></body></html>"))
        self.text_cpf.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CPF:</span></p></body></html>"))
        self.botao_marcar.setText(_translate("MainWindow", "Marcar"))
        self.botao_fechar.setText(_translate("MainWindow", "Fechar"))
        self.botao_marcar.clicked.connect(self.banco_consultas)
        self.botao_fechar.clicked.connect(MainWindow.close)

    def banco_consultas(self):
        nome_paciente = self.lineEdit_nome.text()
        nome_medico = self.lineEdit_n_medico.text()
        cpf = self.lineEdit_cpf.text()
        data = self.dateEdit_data.text()
        horario = self.timeEdit_horario.text()

        banco_de_dados = sqlite3.connect("Banco_de_dados.db")
        cursor = banco_de_dados.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS consultas(nome_paciente TEXT, cpf INTEGER, data DATE, nome_medico TEXT, horario TEXT)")
        cursor.execute(
            "INSERT INTO consultas VALUES('"+nome_paciente+"','" +cpf+"','"+data+"','"+nome_medico+"','"+horario+"')")
        banco_de_dados.commit()
        banco_de_dados.close()
        QtWidgets.QMessageBox.information(None, "Consulta", "Consulta marcada com sucesso!")
        print("DADOS INSERIDDOS COM SUCESSO NO BANCO DE DADDOS!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = tela_agenda_consultar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())