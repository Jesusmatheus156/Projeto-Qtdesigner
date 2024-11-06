# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_cadastrar_paciente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class tela_cadastrar_paciente(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(899, 785)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 901, 151))
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
        self.img_logo.setGeometry(QtCore.QRect(80, 0, 131, 141))
        self.img_logo.setText("")
        self.img_logo.setPixmap(QtGui.QPixmap("img/LOGO.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setObjectName("img_logo")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 150, 901, 631))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(227, 227, 227);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox_viuvo = QtWidgets.QCheckBox(self.frame)
        self.checkBox_viuvo.setGeometry(QtCore.QRect(270, 531, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_viuvo.setFont(font)
        self.checkBox_viuvo.setObjectName("checkBox_viuvo")
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(650, 221, 201, 22))
        self.lineEdit_cpf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.text_nome = QtWidgets.QLabel(self.frame)
        self.text_nome.setGeometry(QtCore.QRect(180, 121, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_nome.setFont(font)
        self.text_nome.setObjectName("text_nome")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(690, 531, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.text_nacionalidade = QtWidgets.QLabel(self.frame)
        self.text_nacionalidade.setGeometry(QtCore.QRect(430, 271, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_nacionalidade.setFont(font)
        self.text_nacionalidade.setObjectName("text_nacionalidade")
        self.text_tipo_san = QtWidgets.QLabel(self.frame)
        self.text_tipo_san.setGeometry(QtCore.QRect(50, 271, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_tipo_san.setFont(font)
        self.text_tipo_san.setObjectName("text_tipo_san")
        self.text_rg = QtWidgets.QLabel(self.frame)
        self.text_rg.setGeometry(QtCore.QRect(380, 221, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_rg.setFont(font)
        self.text_rg.setObjectName("text_rg")
        self.lineEdit_n_conju = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_n_conju.setGeometry(QtCore.QRect(200, 411, 651, 22))
        self.lineEdit_n_conju.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_n_conju.setObjectName("lineEdit_n_conju")
        self.text_cpf = QtWidgets.QLabel(self.frame)
        self.text_cpf.setGeometry(QtCore.QRect(600, 221, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_cpf.setFont(font)
        self.text_cpf.setObjectName("text_cpf")
        self.lineEdit_nacionalidade = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nacionalidade.setGeometry(QtCore.QRect(570, 271, 281, 22))
        self.lineEdit_nacionalidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nacionalidade.setObjectName("lineEdit_nacionalidade")
        self.text_cadaspaci = QtWidgets.QLabel(self.frame)
        self.text_cadaspaci.setGeometry(QtCore.QRect(370, 51, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_cadaspaci.setFont(font)
        self.text_cadaspaci.setObjectName("text_cadaspaci")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 531, 131, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.text_estadocivil = QtWidgets.QLabel(self.frame)
        self.text_estadocivil.setGeometry(QtCore.QRect(60, 451, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_estadocivil.setFont(font)
        self.text_estadocivil.setObjectName("text_estadocivil")
        self.text_datanasc = QtWidgets.QLabel(self.frame)
        self.text_datanasc.setGeometry(QtCore.QRect(60, 221, 141, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_datanasc.setFont(font)
        self.text_datanasc.setObjectName("text_datanasc")
        self.dateEdit_data = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_data.setGeometry(QtCore.QRect(200, 221, 161, 22))
        self.dateEdit_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_data.setObjectName("dateEdit_data")
        self.text_endereco = QtWidgets.QLabel(self.frame)
        self.text_endereco.setGeometry(QtCore.QRect(180, 171, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_endereco.setFont(font)
        self.text_endereco.setObjectName("text_endereco")
        self.lineEdit_n_pai = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_n_pai.setGeometry(QtCore.QRect(170, 361, 681, 22))
        self.lineEdit_n_pai.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_n_pai.setObjectName("lineEdit_n_pai")
        self.lineEdit_tipo_sang = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_tipo_sang.setGeometry(QtCore.QRect(220, 271, 181, 22))
        self.lineEdit_tipo_sang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tipo_sang.setObjectName("lineEdit_tipo_sang")
        self.lineEdit_rg = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_rg.setGeometry(QtCore.QRect(420, 221, 171, 22))
        self.lineEdit_rg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_rg.setObjectName("lineEdit_rg")
        self.checkBox_casado = QtWidgets.QCheckBox(self.frame)
        self.checkBox_casado.setGeometry(QtCore.QRect(270, 491, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_casado.setFont(font)
        self.checkBox_casado.setObjectName("checkBox_casado")
        self.checkBox_solteiro = QtWidgets.QCheckBox(self.frame)
        self.checkBox_solteiro.setGeometry(QtCore.QRect(130, 491, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_solteiro.setFont(font)
        self.checkBox_solteiro.setObjectName("checkBox_solteiro")
        self.lineEdit_endereco = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_endereco.setGeometry(QtCore.QRect(290, 171, 561, 22))
        self.lineEdit_endereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_endereco.setObjectName("lineEdit_endereco")
        self.lineEdit_n_mae = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_n_mae.setGeometry(QtCore.QRect(170, 321, 681, 22))
        self.lineEdit_n_mae.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_n_mae.setObjectName("lineEdit_n_mae")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nome.setGeometry(QtCore.QRect(250, 121, 601, 22))
        self.lineEdit_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.text_n_conju = QtWidgets.QLabel(self.frame)
        self.text_n_conju.setGeometry(QtCore.QRect(50, 411, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_n_conju.setFont(font)
        self.text_n_conju.setObjectName("text_n_conju")
        self.checkBox_divorciado = QtWidgets.QCheckBox(self.frame)
        self.checkBox_divorciado.setGeometry(QtCore.QRect(130, 531, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_divorciado.setFont(font)
        self.checkBox_divorciado.setObjectName("checkBox_divorciado")
        self.text_n_pai = QtWidgets.QLabel(self.frame)
        self.text_n_pai.setGeometry(QtCore.QRect(60, 361, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_n_pai.setFont(font)
        self.text_n_pai.setObjectName("text_n_pai")
        self.text_n_mae = QtWidgets.QLabel(self.frame)
        self.text_n_mae.setGeometry(QtCore.QRect(60, 320, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_n_mae.setFont(font)
        self.text_n_mae.setObjectName("text_n_mae")
        self.img_paciente = QtWidgets.QLabel(self.frame)
        self.img_paciente.setGeometry(QtCore.QRect(10, 60, 191, 161))
        self.img_paciente.setText("")
        self.img_paciente.setPixmap(QtGui.QPixmap("img/paciente.png"))
        self.img_paciente.setScaledContents(True)
        self.img_paciente.setObjectName("img_paciente")
        self.checkBox_viuvo.raise_()
        self.lineEdit_cpf.raise_()
        self.pushButton.raise_()
        self.text_nacionalidade.raise_()
        self.text_tipo_san.raise_()
        self.text_rg.raise_()
        self.lineEdit_n_conju.raise_()
        self.text_cpf.raise_()
        self.lineEdit_nacionalidade.raise_()
        self.text_cadaspaci.raise_()
        self.pushButton_2.raise_()
        self.text_estadocivil.raise_()
        self.text_datanasc.raise_()
        self.dateEdit_data.raise_()
        self.lineEdit_n_pai.raise_()
        self.lineEdit_tipo_sang.raise_()
        self.lineEdit_rg.raise_()
        self.checkBox_casado.raise_()
        self.checkBox_solteiro.raise_()
        self.lineEdit_endereco.raise_()
        self.lineEdit_n_mae.raise_()
        self.lineEdit_nome.raise_()
        self.text_n_conju.raise_()
        self.checkBox_divorciado.raise_()
        self.text_n_pai.raise_()
        self.text_n_mae.raise_()
        self.img_paciente.raise_()
        self.text_nome.raise_()
        self.text_endereco.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Pacientes"))
        self.text_hospital.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">HOSPITAL JOÃO AMOÊDO</span></p></body></html>"))
        self.text_segun.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">SALVANDO VIDAS À 20 ANOS</span></p></body></html>"))
        self.checkBox_viuvo.setText(_translate("Form", "Viúvo(a)"))
        self.text_nome.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#000000;\">Nome:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Fechar"))
        self.text_nacionalidade.setText(_translate("Form", "Nacionalidade"))
        self.text_tipo_san.setText(_translate("Form", "Tipo Sanguíneo:"))
        self.text_rg.setText(_translate("Form", "RG:"))
        self.text_cpf.setText(_translate("Form", "CPF:"))
        self.text_cadaspaci.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">CADASTRAR PACIENTE</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Cadastrar"))
        self.text_estadocivil.setText(_translate("Form", "Estado Civil:"))
        self.text_datanasc.setText(_translate("Form", "Data de Nasc.:"))
        self.text_endereco.setText(_translate("Form", "Endereço:"))
        self.checkBox_casado.setText(_translate("Form", "Casado(a)"))
        self.checkBox_solteiro.setText(_translate("Form", "Solteiro(a)"))
        self.text_n_conju.setText(_translate("Form", "N. do Cônjuge:"))
        self.checkBox_divorciado.setText(_translate("Form", "Divorciado(a)"))
        self.text_n_pai.setText(_translate("Form", "N. do Pai:"))
        self.text_n_mae.setText(_translate("Form", "N. da Mãe:"))
        self.pushButton_2.clicked.connect(self.banco_pacientes)
        self.pushButton.clicked.connect(Form.close)

    def banco_pacientes(self):
        nome_paciente = self.lineEdit_nome.text()
        data_nascimento = self.dateEdit_data.text()
        endereco = self.lineEdit_endereco.text()
        rg = self.lineEdit_rg.text()
        cpf = self.lineEdit_cpf.text()
        tipo_san = self.lineEdit_tipo_sang.text()
        nacionalidade = self.lineEdit_nacionalidade.text()
        nome_mae = self.lineEdit_n_mae.text()
        nome_pai = self.lineEdit_n_pai.text()
        nome_conjugu = self.lineEdit_n_conju.text()

        if self.checkBox_solteiro.isChecked():
            estado_civil = "Solteiro(a)"
        elif self.checkBox_casado.isChecked():
            estado_civil = "Casado(a)"
        elif self.checkBox_divorciado.isChecked():
            estado_civil = "Divorciado(a)"
        elif self.checkBox_viuvo.isChecked():
            estado_civil = "Viúvo(a)"
        else:
            estado_civil = "Não especificado"

        banco_de_dados = sqlite3.connect("Banco_de_dados.db")
        cursor = banco_de_dados.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS pacientes(nome_paciente TEXT, cpf INTEGER, rg INTEGER, data_nascimento DATE, estado_civil TEXT, nome_mae TEXT, nome_pai TEXT, tipo_san TEXT, nacionalidade TEXT, nome_conjugu TEXT, endereco TEXT)")
        cursor.execute(
            "INSERT INTO pacientes VALUES('" + nome_paciente + "', '" + cpf + "', '" + rg + "','" + data_nascimento + "','" + estado_civil + "','" + nome_mae + "','" + nome_pai + "','" + tipo_san + "','" + nacionalidade + "','" + nome_conjugu + "','" + endereco + "')")
        banco_de_dados.commit()
        banco_de_dados.close()
        QtWidgets.QMessageBox.information(None, "Cadastro", "cadastro realizado com sucesso!")
        print("DADOS INSERIDDOS COM SUCESSO NO BANCO DE DADDOS!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tela_cadastrar_paciente()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
