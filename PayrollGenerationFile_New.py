# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PayrollGenerationFile_New.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


import config
class Ui_Form(object):
 
    empdata = [[0]*11]*20 
    empcheck = [[0]*1]*20
    empcheckcount = 0

    def loadData(self):
        print("File Name= "+config.filename)
        f=open(config.filename,"r")
        emprows, empcols = (20, 11) 
        global empdata
        empcount=0
        while True:
                line=f.readline()
                if ( line == ''):
                        break;
                self.empdata[empcount]=line.split(",")
                empcount += 1 
       
        f.close()
        self.tableWidget.setRowCount(0)
        for row_number in range (0,empcount):
                self.tableWidget.insertRow(row_number)
                for colum_number in range (0,11): 
                                             
                        self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(self.empdata[row_number][colum_number])))
	

       

    def checkboxclick(self):
        global empcheck
         
        count = 0        
        if self.checkBox.isChecked():
            self.empcheck[count]=0
            count += 1
        if self.checkBox_2.isChecked():
            self.empcheck[count]=1
            count += 1
        if self.checkBox_3.isChecked():
            self.empcheck[count]=2
            count += 1
        if self.checkBox_4.isChecked():
            self.empcheck[count]=3
            count += 1
        if self.checkBox_5.isChecked():
            self.empcheck[count]=4
            count += 1
        if self.checkBox_6.isChecked():
            self.empcheck[count]=5
            count += 1
        if self.checkBox_7.isChecked():
            self.empcheck[count]=6
            count += 1
        if self.checkBox_8.isChecked():
            self.empcheck[count]=7
            count += 1
        if self.checkBox_9.isChecked():
            self.empcheck[count]=8
            count += 1
        if self.checkBox_10.isChecked():
            self.empcheck[count]=9
            count += 1
        if self.checkBox_11.isChecked():
            self.empcheck[count]=10
            count += 1
        if self.checkBox_12.isChecked():
            self.empcheck[count]=11
            count += 1
        if self.checkBox_13.isChecked():
            self.empcheck[count]=12
            count += 1
        if self.checkBox_14.isChecked():
            self.empcheck[count]=13
            count += 1
        if self.checkBox_15.isChecked():
            self.empcheck[count]=14
            count += 1
        if self.checkBox_16.isChecked():
            self.empcheck[count]=15
            count += 1
        if self.checkBox_17.isChecked():
            self.empcheck[count]=16
            count += 1
        if self.checkBox_18.isChecked():
            self.empcheck[count]=17
            count += 1
        if self.checkBox_19.isChecked():
            self.empcheck[count]=18
            count += 1
        if self.checkBox_20.isChecked():
            self.empcheck[count]=19
            count += 1


        for i in range (0,count):
              print(self.empcheck[i])
        empcheckcount = count
        return empcheckcount

    def salarycalculation(self,count,employeedata,isSBI):

        from datetime import date
        today = date.today()
        from datetime import datetime
        now = datetime.now()
        TotalSalary = 0
        TotalTDS = 0

        if isSBI == 1:
            f=open("EmpPay_"+today.strftime("%d-%m-%Y")+"_S_"+now.strftime("%H:%M:%S"+".csv"),"w")
        else:
            f=open("EmpPay_"+today.strftime("%d-%m-%Y")+"_NS_"+now.strftime("%H:%M:%S"+".csv"),"w")
        
        f.write("S.No,Employee Name,Bank Name,Account Number,IFS Code,Salary,TDS\n") 

        for i in range (0, count):

            Gross_salary = int(employeedata[i][7])/int(employeedata[i][6]) * float(employeedata[i][3])
            TDS = (Gross_salary * 10)/100 
            Salary = Gross_salary-TDS
        	
            rowentry = str(i+1) +","+str(employeedata[i][1])+","
            rowentry += str(employeedata[i][8])+","+str(employeedata[i][9])+","
            rowentry += str(employeedata[i][10].replace("\n",""))+","+str(round(Salary,2))+","+str(round(TDS,2))

            TotalSalary += Salary
            TotalTDS += TDS

            f.write(rowentry+"\n")
        
        f.write(",TotalSalary = "+str(round(TotalSalary,2))+"\n")
        f.write(",TotalTDS = "+str(round(TotalTDS,2))+"\n")
        f.close()
       

    def GeneratePayrollFile(self):

        global empcheck
        empcheckcount = self.checkboxclick()
        emprows, empcols = (20, 11) 
        empdatasbi = [[0]*empcols]*emprows 
        empsbicount=0
        empdatanonsbi = [[0]*empcols]*emprows 
        empnonsbicount=0


        for i in range (0,empcheckcount):
            index = self.empcheck[i]
            if self.empdata[index][8] == "SBI":
                empdatasbi[empsbicount] = self.empdata[index]
                empsbicount += 1
            else:
                empdatanonsbi[empnonsbicount] = self.empdata[index]
                empnonsbicount += 1
        print("SBI Accounts")
        for i in range (0,empsbicount):
             print(empdatasbi[i])
        self.salarycalculation(empsbicount,empdatasbi,1)
        print("Non SBI Accounts")    
        for i in range (0,empnonsbicount):
            print(empdatanonsbi[i])
        self.salarycalculation(empnonsbicount,empdatanonsbi,0)
        
    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1071, 891)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 1011, 631))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 790, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 790, 191, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.GeneratePayrollFile)
        
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(1030, 150, 21, 21))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 120, 911, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(1030, 180, 21, 21))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(1030, 210, 21, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(1030, 240, 21, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(1030, 300, 21, 21))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(1030, 330, 21, 21))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setGeometry(QtCore.QRect(1030, 360, 21, 21))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Form)
        self.checkBox_9.setGeometry(QtCore.QRect(1030, 390, 21, 21))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setGeometry(QtCore.QRect(1030, 420, 21, 21))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(Form)
        self.checkBox_11.setGeometry(QtCore.QRect(1030, 450, 21, 21))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(Form)
        self.checkBox_12.setGeometry(QtCore.QRect(1030, 470, 21, 21))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(1030, 270, 21, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_13 = QtWidgets.QCheckBox(Form)
        self.checkBox_13.setGeometry(QtCore.QRect(1030, 500, 21, 21))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(Form)
        self.checkBox_14.setGeometry(QtCore.QRect(1030, 530, 21, 21))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(Form)
        self.checkBox_15.setGeometry(QtCore.QRect(1030, 560, 21, 21))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(Form)
        self.checkBox_16.setGeometry(QtCore.QRect(1030, 590, 21, 21))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(Form)
        self.checkBox_17.setGeometry(QtCore.QRect(1030, 620, 21, 21))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(Form)
        self.checkBox_18.setGeometry(QtCore.QRect(1030, 650, 21, 21))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(Form)
        self.checkBox_19.setGeometry(QtCore.QRect(1030, 670, 21, 21))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(Form)
        self.checkBox_20.setGeometry(QtCore.QRect(1030, 700, 21, 21))
        self.checkBox_20.setObjectName("checkBox_20")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Employee ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Employee Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PT/FT"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Paid Leave"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Unpaid leave"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Total No.Of Days"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Worked days"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Bank Name"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Account Number"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "IFS Code"))
        self.pushButton.setText(_translate("Form", "Upload Employee Details"))
        self.pushButton_2.setText(_translate("Form", "Generate Payroll File"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.label_2.setText(_translate("Form", config.payrolltitle))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.checkBox_3.setText(_translate("Form", "CheckBox"))
        self.checkBox_4.setText(_translate("Form", "CheckBox"))
        self.checkBox_6.setText(_translate("Form", "CheckBox"))
        self.checkBox_7.setText(_translate("Form", "CheckBox"))
        self.checkBox_8.setText(_translate("Form", "CheckBox"))
        self.checkBox_9.setText(_translate("Form", "CheckBox"))
        self.checkBox_10.setText(_translate("Form", "CheckBox"))
        self.checkBox_11.setText(_translate("Form", "CheckBox"))
        self.checkBox_12.setText(_translate("Form", "CheckBox"))
        self.checkBox_5.setText(_translate("Form", "CheckBox"))
        self.checkBox_13.setText(_translate("Form", "CheckBox"))
        self.checkBox_14.setText(_translate("Form", "CheckBox"))
        self.checkBox_15.setText(_translate("Form", "CheckBox"))
        self.checkBox_16.setText(_translate("Form", "CheckBox"))
        self.checkBox_17.setText(_translate("Form", "CheckBox"))
        self.checkBox_18.setText(_translate("Form", "CheckBox"))
        self.checkBox_19.setText(_translate("Form", "CheckBox"))
        self.checkBox_20.setText(_translate("Form", "CheckBox"))
        self.label_3.setText(_translate("Form", "Employee Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
