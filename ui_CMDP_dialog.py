# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CMDP_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CMDPDialogBase(object):
    def setupUi(self, CMDPDialogBase):
        CMDPDialogBase.setObjectName("CMDPDialogBase")
        CMDPDialogBase.resize(870, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(CMDPDialogBase.sizePolicy().hasHeightForWidth())
        CMDPDialogBase.setSizePolicy(sizePolicy)
        CMDPDialogBase.setMinimumSize(QtCore.QSize(870, 580))
        CMDPDialogBase.setMaximumSize(QtCore.QSize(950, 620))
        self.gridLayoutWidget = QtWidgets.QWidget(CMDPDialogBase)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 872, 582))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(870, 580))
        self.tabWidget.setMaximumSize(QtCore.QSize(950, 620))
        self.tabWidget.setObjectName("tabWidget")
        self.tLogin = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tLogin.sizePolicy().hasHeightForWidth())
        self.tLogin.setSizePolicy(sizePolicy)
        self.tLogin.setMinimumSize(QtCore.QSize(350, 260))
        self.tLogin.setMaximumSize(QtCore.QSize(950, 620))
        self.tLogin.setObjectName("tLogin")
        self.lLoginandconnect = QtWidgets.QLabel(self.tLogin)
        self.lLoginandconnect.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.lLoginandconnect.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lLoginandconnect.setObjectName("lLoginandconnect")
        self.lUserId = QtWidgets.QLabel(self.tLogin)
        self.lUserId.setGeometry(QtCore.QRect(10, 50, 55, 21))
        self.lUserId.setObjectName("lUserId")
        self.lApiKey = QtWidgets.QLabel(self.tLogin)
        self.lApiKey.setGeometry(QtCore.QRect(10, 100, 55, 21))
        self.lApiKey.setObjectName("lApiKey")
        self.lEUserId = QtWidgets.QLineEdit(self.tLogin)
        self.lEUserId.setGeometry(QtCore.QRect(80, 50, 741, 22))
        self.lEUserId.setObjectName("lEUserId")
        self.lEApiKey = QtWidgets.QLineEdit(self.tLogin)
        self.lEApiKey.setGeometry(QtCore.QRect(80, 100, 741, 22))
        self.lEApiKey.setObjectName("lEApiKey")
        self.cBSaveUserAndApi = QtWidgets.QCheckBox(self.tLogin)
        self.cBSaveUserAndApi.setGeometry(QtCore.QRect(10, 150, 181, 20))
        self.cBSaveUserAndApi.setObjectName("cBSaveUserAndApi")
        self.tabWidget.addTab(self.tLogin, "")
        self.tAOI = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tAOI.sizePolicy().hasHeightForWidth())
        self.tAOI.setSizePolicy(sizePolicy)
        self.tAOI.setMinimumSize(QtCore.QSize(350, 260))
        self.tAOI.setMaximumSize(QtCore.QSize(950, 620))
        self.tAOI.setObjectName("tAOI")
        self.lDefineAOI = QtWidgets.QLabel(self.tAOI)
        self.lDefineAOI.setGeometry(QtCore.QRect(14, 20, 201, 20))
        self.lDefineAOI.setObjectName("lDefineAOI")
        self.rBFullModelArea = QtWidgets.QRadioButton(self.tAOI)
        self.rBFullModelArea.setGeometry(QtCore.QRect(10, 50, 151, 20))
        self.rBFullModelArea.setObjectName("rBFullModelArea")
        self.rBRestrictedArea = QtWidgets.QRadioButton(self.tAOI)
        self.rBRestrictedArea.setGeometry(QtCore.QRect(10, 90, 151, 20))
        self.rBRestrictedArea.setObjectName("rBRestrictedArea")
        self.lNorth = QtWidgets.QLabel(self.tAOI)
        self.lNorth.setGeometry(QtCore.QRect(20, 140, 55, 21))
        self.lNorth.setObjectName("lNorth")
        self.lWest = QtWidgets.QLabel(self.tAOI)
        self.lWest.setGeometry(QtCore.QRect(20, 190, 55, 21))
        self.lWest.setObjectName("lWest")
        self.lSouth = QtWidgets.QLabel(self.tAOI)
        self.lSouth.setGeometry(QtCore.QRect(20, 240, 55, 21))
        self.lSouth.setObjectName("lSouth")
        self.lEast = QtWidgets.QLabel(self.tAOI)
        self.lEast.setGeometry(QtCore.QRect(20, 290, 55, 21))
        self.lEast.setObjectName("lEast")
        self.lENorth = QtWidgets.QLineEdit(self.tAOI)
        self.lENorth.setGeometry(QtCore.QRect(90, 140, 721, 22))
        self.lENorth.setObjectName("lENorth")
        self.lEWest = QtWidgets.QLineEdit(self.tAOI)
        self.lEWest.setGeometry(QtCore.QRect(90, 190, 721, 22))
        self.lEWest.setObjectName("lEWest")
        self.lESouth = QtWidgets.QLineEdit(self.tAOI)
        self.lESouth.setGeometry(QtCore.QRect(90, 240, 721, 22))
        self.lESouth.setObjectName("lESouth")
        self.lEEast = QtWidgets.QLineEdit(self.tAOI)
        self.lEEast.setGeometry(QtCore.QRect(90, 290, 721, 22))
        self.lEEast.setObjectName("lEEast")
        self.rBAddShapeFile = QtWidgets.QRadioButton(self.tAOI)
        self.rBAddShapeFile.setGeometry(QtCore.QRect(10, 340, 121, 20))
        self.rBAddShapeFile.setObjectName("rBAddShapeFile")
        self.lShapeFile = QtWidgets.QLabel(self.tAOI)
        self.lShapeFile.setGeometry(QtCore.QRect(20, 390, 71, 21))
        self.lShapeFile.setObjectName("lShapeFile")
        self.cBShapeFile = QtWidgets.QComboBox(self.tAOI)
        self.cBShapeFile.setGeometry(QtCore.QRect(100, 390, 711, 22))
        self.cBShapeFile.setObjectName("cBShapeFile")
        self.tabWidget.addTab(self.tAOI, "")
        self.tDownloadData = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tDownloadData.sizePolicy().hasHeightForWidth())
        self.tDownloadData.setSizePolicy(sizePolicy)
        self.tDownloadData.setMinimumSize(QtCore.QSize(350, 260))
        self.tDownloadData.setMaximumSize(QtCore.QSize(950, 620))
        self.tDownloadData.setObjectName("tDownloadData")
        self.lDownloadedDataOptions = QtWidgets.QLabel(self.tDownloadData)
        self.lDownloadedDataOptions.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.lDownloadedDataOptions.setObjectName("lDownloadedDataOptions")
        self.lVariable = QtWidgets.QLabel(self.tDownloadData)
        self.lVariable.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.lVariable.setObjectName("lVariable")
        self.lModel = QtWidgets.QLabel(self.tDownloadData)
        self.lModel.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.lModel.setObjectName("lModel")
        self.lLevel = QtWidgets.QLabel(self.tDownloadData)
        self.lLevel.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.lLevel.setObjectName("lLevel")
        self.lDate = QtWidgets.QLabel(self.tDownloadData)
        self.lDate.setGeometry(QtCore.QRect(10, 180, 71, 21))
        self.lDate.setObjectName("lDate")
        self.lType = QtWidgets.QLabel(self.tDownloadData)
        self.lType.setGeometry(QtCore.QRect(10, 220, 71, 21))
        self.lType.setObjectName("lType")
        self.lTime = QtWidgets.QLabel(self.tDownloadData)
        self.lTime.setGeometry(QtCore.QRect(10, 260, 71, 21))
        self.lTime.setObjectName("lTime")
        self.lFormat = QtWidgets.QLabel(self.tDownloadData)
        self.lFormat.setGeometry(QtCore.QRect(10, 420, 71, 21))
        self.lFormat.setObjectName("lFormat")
        self.lLeadTime = QtWidgets.QLabel(self.tDownloadData)
        self.lLeadTime.setGeometry(QtCore.QRect(420, 260, 71, 21))
        self.lLeadTime.setObjectName("lLeadTime")
        self.cBTermsAndConditions = QtWidgets.QCheckBox(self.tDownloadData)
        self.cBTermsAndConditions.setGeometry(QtCore.QRect(10, 460, 251, 20))
        self.cBTermsAndConditions.setObjectName("cBTermsAndConditions")
        self.pBDownloadData = QtWidgets.QPushButton(self.tDownloadData)
        self.pBDownloadData.setGeometry(QtCore.QRect(630, 460, 93, 28))
        self.pBDownloadData.setObjectName("pBDownloadData")
        self.pBDownloadDataProgress = QtWidgets.QProgressBar(self.tDownloadData)
        self.pBDownloadDataProgress.setGeometry(QtCore.QRect(10, 500, 811, 23))
        self.pBDownloadDataProgress.setProperty("value", 0)
        self.pBDownloadDataProgress.setObjectName("pBDownloadDataProgress")
        self.dTEStartDate = QtWidgets.QDateTimeEdit(self.tDownloadData)
        self.dTEStartDate.setGeometry(QtCore.QRect(120, 180, 131, 22))
        self.dTEStartDate.setDate(QtCore.QDate(2020, 8, 26))
        self.dTEStartDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 8, 26), QtCore.QTime(0, 0, 0)))
        self.dTEStartDate.setMinimumDate(QtCore.QDate(2020, 8, 26))
        self.dTEStartDate.setTimeSpec(QtCore.Qt.LocalTime)
        self.dTEStartDate.setObjectName("dTEStartDate")
        self.cBVariable = QtWidgets.QComboBox(self.tDownloadData)
        self.cBVariable.setGeometry(QtCore.QRect(80, 60, 741, 22))
        self.cBVariable.setObjectName("cBVariable")
        self.cBModel = QtWidgets.QComboBox(self.tDownloadData)
        self.cBModel.setGeometry(QtCore.QRect(80, 100, 741, 22))
        self.cBModel.setObjectName("cBModel")
        self.cBLevel = QtWidgets.QComboBox(self.tDownloadData)
        self.cBLevel.setGeometry(QtCore.QRect(80, 140, 741, 22))
        self.cBLevel.setObjectName("cBLevel")
        self.cBType = QtWidgets.QComboBox(self.tDownloadData)
        self.cBType.setGeometry(QtCore.QRect(80, 220, 741, 22))
        self.cBType.setObjectName("cBType")
        self.cBFormat = QtWidgets.QComboBox(self.tDownloadData)
        self.cBFormat.setGeometry(QtCore.QRect(80, 420, 331, 22))
        self.cBFormat.setObjectName("cBFormat")
        self.dTEEndDate = QtWidgets.QDateTimeEdit(self.tDownloadData)
        self.dTEEndDate.setGeometry(QtCore.QRect(690, 180, 131, 22))
        self.dTEEndDate.setDate(QtCore.QDate(2024, 1, 1))
        self.dTEEndDate.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dTEEndDate.setTimeSpec(QtCore.Qt.LocalTime)
        self.dTEEndDate.setObjectName("dTEEndDate")
        self.lStartDate = QtWidgets.QLabel(self.tDownloadData)
        self.lStartDate.setGeometry(QtCore.QRect(80, 180, 31, 21))
        self.lStartDate.setObjectName("lStartDate")
        self.lEndDate = QtWidgets.QLabel(self.tDownloadData)
        self.lEndDate.setGeometry(QtCore.QRect(650, 180, 31, 21))
        self.lEndDate.setObjectName("lEndDate")
        self.lWTime = QtWidgets.QListWidget(self.tDownloadData)
        self.lWTime.setGeometry(QtCore.QRect(80, 260, 331, 151))
        self.lWTime.setFrameShape(QtWidgets.QFrame.Box)
        self.lWTime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lWTime.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lWTime.setObjectName("lWTime")
        self.lWLeadTime = QtWidgets.QListWidget(self.tDownloadData)
        self.lWLeadTime.setGeometry(QtCore.QRect(490, 260, 331, 151))
        self.lWLeadTime.setFrameShape(QtWidgets.QFrame.Box)
        self.lWLeadTime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lWLeadTime.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lWLeadTime.setObjectName("lWLeadTime")
        self.pBCancel = QtWidgets.QPushButton(self.tDownloadData)
        self.pBCancel.setGeometry(QtCore.QRect(730, 460, 93, 28))
        self.pBCancel.setObjectName("pBCancel")
        self.tBChooseFolder = QtWidgets.QToolButton(self.tDownloadData)
        self.tBChooseFolder.setGeometry(QtCore.QRect(790, 420, 27, 21))
        self.tBChooseFolder.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tBChooseFolder.setArrowType(QtCore.Qt.NoArrow)
        self.tBChooseFolder.setObjectName("tBChooseFolder")
        self.lChooseFolder = QtWidgets.QLabel(self.tDownloadData)
        self.lChooseFolder.setGeometry(QtCore.QRect(620, 420, 151, 21))
        self.lChooseFolder.setObjectName("lChooseFolder")
        self.pBVariableInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBVariableInfo.setGeometry(QtCore.QRect(830, 60, 31, 21))
        self.pBVariableInfo.setObjectName("pBVariableInfo")
        self.pBModelInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBModelInfo.setGeometry(QtCore.QRect(830, 100, 31, 21))
        self.pBModelInfo.setObjectName("pBModelInfo")
        self.pBLevelInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBLevelInfo.setGeometry(QtCore.QRect(830, 140, 31, 21))
        self.pBLevelInfo.setObjectName("pBLevelInfo")
        self.pBTimeInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBTimeInfo.setGeometry(QtCore.QRect(10, 290, 31, 21))
        self.pBTimeInfo.setObjectName("pBTimeInfo")
        self.pBLeadTimeInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBLeadTimeInfo.setGeometry(QtCore.QRect(430, 290, 31, 21))
        self.pBLeadTimeInfo.setObjectName("pBLeadTimeInfo")
        self.pBFormatInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBFormatInfo.setGeometry(QtCore.QRect(430, 420, 31, 21))
        self.pBFormatInfo.setObjectName("pBFormatInfo")
        self.pBCAMSInfo = QtWidgets.QPushButton(self.tDownloadData)
        self.pBCAMSInfo.setGeometry(QtCore.QRect(830, 20, 31, 21))
        self.pBCAMSInfo.setObjectName("pBCAMSInfo")
        self.lCAMSInfo = QtWidgets.QLabel(self.tDownloadData)
        self.lCAMSInfo.setGeometry(QtCore.QRect(690, 20, 131, 21))
        self.lCAMSInfo.setObjectName("lCAMSInfo")
        self.tabWidget.addTab(self.tDownloadData, "")
        self.tHelp = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tHelp.sizePolicy().hasHeightForWidth())
        self.tHelp.setSizePolicy(sizePolicy)
        self.tHelp.setMaximumSize(QtCore.QSize(950, 620))
        self.tHelp.setObjectName("tHelp")
        self.sAHelp = QtWidgets.QScrollArea(self.tHelp)
        self.sAHelp.setGeometry(QtCore.QRect(20, 20, 821, 501))
        self.sAHelp.setWidgetResizable(True)
        self.sAHelp.setObjectName("sAHelp")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tEHelp = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.tEHelp.setGeometry(QtCore.QRect(0, 0, 821, 501))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tEHelp.setFont(font)
        self.tEHelp.setObjectName("tEHelp")
        self.sAHelp.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tHelp, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(CMDPDialogBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CMDPDialogBase)

    def retranslateUi(self, CMDPDialogBase):
        _translate = QtCore.QCoreApplication.translate
        CMDPDialogBase.setWindowTitle(_translate("CMDPDialogBase", "CMDP"))
        self.lLoginandconnect.setText(_translate("CMDPDialogBase", "Login & Connect to CAMS:"))
        self.lUserId.setText(_translate("CMDPDialogBase", "User-ID:"))
        self.lApiKey.setText(_translate("CMDPDialogBase", "API Key:"))
        self.cBSaveUserAndApi.setText(_translate("CMDPDialogBase", "Save User-ID and API Key"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tLogin), _translate("CMDPDialogBase", "Login"))
        self.lDefineAOI.setText(_translate("CMDPDialogBase", "Define the area of interest (AOI):"))
        self.rBFullModelArea.setText(_translate("CMDPDialogBase", "Full Model Area"))
        self.rBRestrictedArea.setText(_translate("CMDPDialogBase", "Restricted Area"))
        self.lNorth.setText(_translate("CMDPDialogBase", "North:"))
        self.lWest.setText(_translate("CMDPDialogBase", "West:"))
        self.lSouth.setText(_translate("CMDPDialogBase", "South:"))
        self.lEast.setText(_translate("CMDPDialogBase", "East:"))
        self.rBAddShapeFile.setText(_translate("CMDPDialogBase", "Add Shape File"))
        self.lShapeFile.setText(_translate("CMDPDialogBase", "Shape File:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tAOI), _translate("CMDPDialogBase", "Area Of Interest"))
        self.lDownloadedDataOptions.setText(_translate("CMDPDialogBase", "Downloaded Data Parameters:"))
        self.lVariable.setText(_translate("CMDPDialogBase", "Variable:"))
        self.lModel.setText(_translate("CMDPDialogBase", "Model:"))
        self.lLevel.setText(_translate("CMDPDialogBase", "Level:"))
        self.lDate.setText(_translate("CMDPDialogBase", "Date:"))
        self.lType.setText(_translate("CMDPDialogBase", "Type:"))
        self.lTime.setText(_translate("CMDPDialogBase", "Time:"))
        self.lFormat.setText(_translate("CMDPDialogBase", "Format:"))
        self.lLeadTime.setText(_translate("CMDPDialogBase", "Lead Time:"))
        self.cBTermsAndConditions.setText(_translate("CMDPDialogBase", "I Agree To The Terms And Conditions"))
        self.pBDownloadData.setText(_translate("CMDPDialogBase", "Download Data"))
        self.dTEStartDate.setDisplayFormat(_translate("CMDPDialogBase", "dd/MM/yyyy"))
        self.dTEEndDate.setDisplayFormat(_translate("CMDPDialogBase", "dd/MM/yyyy"))
        self.lStartDate.setText(_translate("CMDPDialogBase", "Start:"))
        self.lEndDate.setText(_translate("CMDPDialogBase", "End:"))
        self.pBCancel.setText(_translate("CMDPDialogBase", "Cancel"))
        self.tBChooseFolder.setText(_translate("CMDPDialogBase", "..."))
        self.lChooseFolder.setText(_translate("CMDPDialogBase", "Choose Download Folder:"))
        self.pBVariableInfo.setText(_translate("CMDPDialogBase", "i"))
        self.pBModelInfo.setText(_translate("CMDPDialogBase", "i"))
        self.pBLevelInfo.setText(_translate("CMDPDialogBase", "i"))
        self.pBTimeInfo.setText(_translate("CMDPDialogBase", "i"))
        self.pBLeadTimeInfo.setText(_translate("CMDPDialogBase", "i"))
        self.pBFormatInfo.setText(_translate("CMDPDialogBase", "i"))
        self.pBCAMSInfo.setText(_translate("CMDPDialogBase", "i"))
        self.lCAMSInfo.setText(_translate("CMDPDialogBase", "CAMS Documentation:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tDownloadData), _translate("CMDPDialogBase", "Download Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tHelp), _translate("CMDPDialogBase", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CMDPDialogBase = QtWidgets.QDialog()
    ui = Ui_CMDPDialogBase()
    ui.setupUi(CMDPDialogBase)
    CMDPDialogBase.show()
    sys.exit(app.exec_())