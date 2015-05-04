# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Okno4.ui'
#
# Created: Wed Apr 29 11:58:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_PrzypominaczI(object):

    def __init__(self):
        self.listaWatki = []


    def setupUi(self, PrzypominaczI):

        PrzypominaczI.setObjectName(_fromUtf8("PrzypominaczI"))
        PrzypominaczI.resize(1081, 510)
        self.listaPrzyp = QListWidget(PrzypominaczI)
        self.listaPrzyp.setGeometry(QRect(170, 50, 211, 391))
        self.listaPrzyp.setObjectName(_fromUtf8("listaPrzyp"))
        self.labelP = QLabel(PrzypominaczI)
        self.labelP.setGeometry(QRect(170, 20, 151, 16))
        self.labelP.setObjectName(_fromUtf8("labelP"))
        self.Edytuj = QPushButton(PrzypominaczI)
        self.Edytuj.setGeometry(QRect(10, 370, 151, 71))
        self.Edytuj.setObjectName(_fromUtf8("Edytuj"))
        self.Usun = QPushButton(PrzypominaczI)
        self.Usun.setGeometry(QRect(10, 280, 151, 71))
        self.Usun.setObjectName(_fromUtf8("Usun"))
        self.kalendarz = QCalendarWidget(PrzypominaczI)
        self.kalendarz.setGeometry(QRect(690, 50, 361, 391))
        self.kalendarz.setObjectName(_fromUtf8("kalendarz"))
        self.label_3 = QLabel(PrzypominaczI)
        self.label_3.setGeometry(QRect(420, 50, 141, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tytul = QLineEdit(PrzypominaczI)
        self.tytul.setGeometry(QRect(420, 80, 251, 20))
        self.tytul.setObjectName(_fromUtf8("tytul"))
        self.label = QLabel(PrzypominaczI)
        self.label.setGeometry(QRect(420, 110, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.trescPrzyp = QTextEdit(PrzypominaczI)
        self.trescPrzyp.setGeometry(QRect(420, 140, 251, 301))
        self.trescPrzyp.setObjectName(_fromUtf8("trescPrzyp"))
        self.startPrzyp = QPushButton(PrzypominaczI)
        self.startPrzyp.setGeometry(QRect(10, 50, 151, 71))
        self.startPrzyp.clicked.connect(self.startWatek)
        self.startPrzyp.setObjectName(_fromUtf8("startPrzyp"))
        self.label_2 = QLabel(PrzypominaczI)
        self.label_2.setGeometry(QRect(850, 460, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.godzina = QTimeEdit(PrzypominaczI)
        self.godzina.setGeometry(QRect(940, 450, 111, 41))
        font = QFont()
        font.setPointSize(14)
        self.godzina.setFont(font)
        self.godzina.setObjectName(_fromUtf8("godzina"))

        self.retranslateUi(PrzypominaczI)
        QMetaObject.connectSlotsByName(PrzypominaczI)




    def retranslateUi(self, PrzypominaczI):
        PrzypominaczI.setWindowTitle(_translate("PrzypominaczI", "Dialog", None))
        self.labelP.setText(_translate("PrzypominaczI", "Lista przypomnień", None))
        self.Edytuj.setText(_translate("PrzypominaczI", " Edytuj przypomnienie", None))
        self.Usun.setText(_translate("PrzypominaczI", "Usuń przypomnienie", None))
        self.label_3.setText(_translate("PrzypominaczI", "Podaj tytuł przypomnienia:", None))
        self.label.setText(_translate("PrzypominaczI", "Wprowadź tekst przypomnienia:", None))
        self.startPrzyp.setText(_translate("PrzypominaczI", "Ustaw Przypomnienie", None))
        self.label_2.setText(_translate("PrzypominaczI", "Podaj godzinę:", None))
    
    
    

    def pozycjaTytul(self):

        #lista = []
        #self.pozycja = self.zebTyt()#tytul.text()
        #lista.append(self.pozycja)
        #licz = len(lista)
        #n = -1
        #for x in range(licz):
        #	n = n + 1
        #print self.pozycja
        QListWidgetItem(self.tytul.text(),self.listaPrzyp)

    #def zebTyt(self):
        #watek.tytul = self.tytul.text()
        #return watek.tytul
    
    def startWatek(self):


        index = len(self.listaWatki)
        watek = Watek(index)

        watek.pobranaData = self.kalendarz.selectedDate().toString("yyyy-MM-dd")
        watek.pobranaGodzina = self.godzina.time().toString("hh:mm")


        watek.start()
        self.listaWatki.append(watek)
        watek.sygnal.connect(ui.okienko)
        #watek.sygnal2.connect(ui.zebTyt)
        #watek.sygnal2.connect(ui.pozycjaTytul)
        #print index

    def okienko(self):
        komunikat = self.trescPrzyp.toPlainText()
        QMessageBox.information(QWidget(),'Przypomnienie',komunikat, QMessageBox.Ok)

class Watek(QThread):
    sygnal2 = pyqtSignal()
    sygnal = pyqtSignal()


    def __init__(self,index):
        super(Watek, self).__init__()
        self.index = index
        self.pobranaData = None
        self.pobranaGodzina = None
        #self.tytul = None


    def run(self):

        #self.sygnal2.emit()
        #while self.tytul is None:

            #continue


        silnik(self.pobranaData,self.pobranaGodzina)
        self.sygnal.emit()

def silnik(pobranaData,pobranaGodzina):

    while True:

        dataKomputera = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")
        dataKalendarza = pobranaData + " " + pobranaGodzina
        print dataKalendarza + " " + dataKomputera

        if dataKomputera == dataKalendarza:

            break

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
   
    
    
    PrzypominaczI = QDialog()
    ui = Ui_PrzypominaczI()
    ui.setupUi(PrzypominaczI)
    PrzypominaczI.show()
    
    sys.exit(app.exec_())

