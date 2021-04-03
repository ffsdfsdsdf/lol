from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from DezineF import Ui_Dialog
import requests
from bs4 import BeautifulSoup
from pydactyl import PterodactylClient 

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


ui.lineEdit_2.setStyleSheet("color: white;  background-color: gray")
ui.lineEdit_2.setText("Сервер: MagicCore")

#Logic
def MagicCoreInfoAboutMemory():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	Info = client.client.get_server_utilization("857d735e", detail=False)
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText(str(Info))

ui.Memory.clicked.connect( MagicCoreInfoAboutMemory )
#########################################################################
def MagicCoreInfoAbout():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	Info = client.client.get_server("857d735e", detail=False)
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText(str(Info))

ui.Info.clicked.connect( MagicCoreInfoAbout )
#########################################################################
def MagicCore():
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: gray")
	ui.lineEdit_2.setText("Сервер: MagicCore")
	
ui.Server.clicked.connect( MagicCore )
#########################################################################
def MagicCoreStop():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	client.client.send_power_action("857d735e", "stop")
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText("Комманда выполнена, сервер остановлен.")

ui.Stop.clicked.connect( MagicCoreStop )
#########################################################################
def MagicCoreStart():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	client.client.send_power_action("857d735e", "start")
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText("Комманда выполнена, сервер запущен.")

ui.Start.clicked.connect( MagicCoreStart )
#########################################################################
def MagicCoreKill():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	client.client.send_power_action("857d735e", "kill")
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText("Комманда выполнена, сервер убит.")

ui.Kill.clicked.connect( MagicCoreKill )
#########################################################################
def MagicCoreSaveAll():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	client.client.send_console_command("857d735e", "save-all")
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText("Комманда выполнена, мир сохранён.")

ui.pushButton.clicked.connect( MagicCoreSaveAll )
#########################################################################
def MagicCoreRestart():
	client = PterodactylClient('https://game.majorcore.com/', 'uPPtBxS2Ujd5dRff8shoVtSYjKVJc9oLdnnH8iBjGiJg1r5A')
	
	client.client.send_power_action("857d735e", "restart")
	
	
	ui.lineEdit_2.setStyleSheet("color: white;  background-color: green")
	ui.lineEdit_2.setText("Команда была отправленна на сервер.")
	ui.Logi.setText("Комманда выполнена, сервер перезагружен")

ui.Restart.clicked.connect( MagicCoreRestart )
sys.exit(app.exec_())
