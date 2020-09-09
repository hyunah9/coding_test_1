import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import PyQt5

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

RegUI = 'fast.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(RegUI, self)
        self.analysis_pushButton.clicked.connect(self.AnalysisClicked)

    def AnalysisClicked(self):
        try :
            fast_data_name = self.import_lineEdit.text()
            fast_data = pd.read_csv(fast_data_name)
            self.error_lineEdit_1.clear()
            fast_y_name = self.select_y_lineEdit.text()
            fast_y_names = fast_y_name.split(',')
            fast_y_name = fast_y_name.replace(',', '')
            fast_y_name = fast_y_name.strip()
            fast_y_name_length = len(fast_y_name)
            fast_x_name = self.select_x_lineEdit.text()
            fast_x_name_length = len(fast_x_name)
            fast_x_name = fast_x_name.split(',')
            while ('' in fast_x_name) == True:
                fast_x_name.remove('')
            for i in range(len(fast_x_name)):
                fast_x_name[i] = fast_x_name[i].strip()
            try :
                y = fast_data[fast_y_name]
                self.error_lineEdit_2.clear()
            except :
                if len(fast_y_names) !=1 or fast_y_name_length==0:
                    self.error_lineEdit_2.setText("종속변수는 하나만 선택해야 합니다.")
                elif (fast_y_name in fast_data.columns) == False:
                    self.error_lineEdit_2.setText("%s라는 변수는 존재하지 않습니다. 대소문자 구분 필수" % fast_y_name)
            try:
                if fast_x_name ==[]:
                    raise Exception()
                X = fast_data[fast_x_name]
                self.error_lineEdit_3.clear()
            except :
                if fast_x_name_length == 0 :
                    self.error_lineEdit_3.setText("변수를 하나 이상 설정하세요")
                else:
                    for i in fast_x_name:
                        if (i in fast_data.columns) == False:
                            self.error_lineEdit_3.setText("%s라는 변수는 존재하지 않습니다. 대소문자 구분 필수" % i)
            Xc = sm.add_constant(X)
            linear_regression = sm.OLS(y, Xc)
            fitted_model = linear_regression.fit()
            summary = fitted_model.summary().as_text()
            self.textEdit_1.setText(summary)
        except Exception as e:
            if type(e) == FileNotFoundError:
                self.error_lineEdit_1.setText("파일을 잘 못 불러왔습니다. 확장자가 .csv인지 확인하세요")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
