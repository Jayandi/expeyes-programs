# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputSelector.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 432)
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/control/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(True)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(3, 3, 3, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.subSelection = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subSelection.sizePolicy().hasHeightForWidth())
        self.subSelection.setSizePolicy(sizePolicy)
        self.subSelection.setMinimumSize(QtCore.QSize(80, 0))
        self.subSelection.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.subSelection.setObjectName("subSelection")
        self.gridLayout.addWidget(self.subSelection, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gaugeLayout = QtWidgets.QGridLayout()
        self.gaugeLayout.setSpacing(3)
        self.gaugeLayout.setObjectName("gaugeLayout")
        self.gridLayout.addLayout(self.gaugeLayout, 2, 0, 1, 7)
        self.configLayout = QtWidgets.QHBoxLayout()
        self.configLayout.setObjectName("configLayout")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setMaximumSize(QtCore.QSize(16777215, 20))
        self.message.setStyleSheet("color: rgb(204, 0, 0);\n"
"font: 13pt \"Ubuntu\";")
        self.message.setObjectName("message")
        self.configLayout.addWidget(self.message)
        self.gridLayout.addLayout(self.configLayout, 3, 0, 1, 7)
        self.availableInputs = QtWidgets.QComboBox(Dialog)
        self.availableInputs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.availableInputs.setObjectName("availableInputs")
        self.gridLayout.addWidget(self.availableInputs, 0, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 6, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minValue = QtWidgets.QDoubleSpinBox(Dialog)
        self.minValue.setMinimumSize(QtCore.QSize(100, 0))
        self.minValue.setMinimum(-65535.0)
        self.minValue.setMaximum(65535.0)
        self.minValue.setObjectName("minValue")
        self.horizontalLayout.addWidget(self.minValue)
        self.maxValue = QtWidgets.QDoubleSpinBox(Dialog)
        self.maxValue.setMinimumSize(QtCore.QSize(100, 0))
        self.maxValue.setMinimum(-65535.0)
        self.maxValue.setMaximum(65535.0)
        self.maxValue.setObjectName("maxValue")
        self.horizontalLayout.addWidget(self.maxValue)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.init)
        self.availableInputs.currentIndexChanged['int'].connect(Dialog.selectSensor)
        self.subSelection.currentIndexChanged['int'].connect(Dialog.subSelectionChanged)
        self.toolButton_2.clicked.connect(Dialog.confirm)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configure Axis"))
        self.pushButton.setText(_translate("Dialog", "REFRESH"))
        self.message.setText(_translate("Dialog", "."))
        self.toolButton_2.setText(_translate("Dialog", "CONFIRM"))
        self.minValue.setPrefix(_translate("Dialog", "Min "))
        self.maxValue.setPrefix(_translate("Dialog", "Max "))

from . import res_rc