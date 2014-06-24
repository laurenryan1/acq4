# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './acq4/analysis/modules/pbm_ImageAnalysis/ctrlTemplatePhysiology.ui'
#
# Created: Tue Jun 24 17:07:54 2014
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(315, 410)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 1, 2, 1)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.widget_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 5, 286, 156))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.widget = QtGui.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 25, 266, 93))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.ImagePhys_PhysThresh = QtGui.QDoubleSpinBox(self.widget)
        self.ImagePhys_PhysThresh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PhysThresh.setDecimals(1)
        self.ImagePhys_PhysThresh.setMinimum(0.0)
        self.ImagePhys_PhysThresh.setMaximum(2000.0)
        self.ImagePhys_PhysThresh.setSingleStep(5.0)
        self.ImagePhys_PhysThresh.setProperty("value", 50.0)
        self.ImagePhys_PhysThresh.setObjectName(_fromUtf8("ImagePhys_PhysThresh"))
        self.gridLayout_4.addWidget(self.ImagePhys_PhysThresh, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.ImagePhys_PhysSign = QtGui.QComboBox(self.widget)
        self.ImagePhys_PhysSign.setObjectName(_fromUtf8("ImagePhys_PhysSign"))
        self.ImagePhys_PhysSign.addItem(_fromUtf8(""))
        self.ImagePhys_PhysSign.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.ImagePhys_PhysSign, 2, 1, 1, 1)
        self.ImagePhys_PhysLPF = QtGui.QDoubleSpinBox(self.widget)
        self.ImagePhys_PhysLPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PhysLPF.setMinimum(-5000.0)
        self.ImagePhys_PhysLPF.setMaximum(50000.0)
        self.ImagePhys_PhysLPF.setProperty("value", 2500.0)
        self.ImagePhys_PhysLPF.setObjectName(_fromUtf8("ImagePhys_PhysLPF"))
        self.gridLayout_4.addWidget(self.ImagePhys_PhysLPF, 0, 1, 1, 1)
        self.ImagePhys_DetectSpikes = QtGui.QPushButton(self.groupBox_2)
        self.ImagePhys_DetectSpikes.setGeometry(QtCore.QRect(5, 125, 137, 32))
        self.ImagePhys_DetectSpikes.setMinimumSize(QtCore.QSize(5, 0))
        self.ImagePhys_DetectSpikes.setObjectName(_fromUtf8("ImagePhys_DetectSpikes"))
        self.groupBox_3 = QtGui.QGroupBox(self.widget_2)
        self.groupBox_3.setGeometry(QtCore.QRect(15, 160, 281, 221))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.widget1 = QtGui.QWidget(self.groupBox_3)
        self.widget1.setGeometry(QtCore.QRect(15, 120, 195, 90))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.formLayout = QtGui.QFormLayout(self.widget1)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ImagePhys_STA = QtGui.QPushButton(self.widget1)
        self.ImagePhys_STA.setObjectName(_fromUtf8("ImagePhys_STA"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ImagePhys_STA)
        self.ImagePhys_BTA = QtGui.QPushButton(self.widget1)
        self.ImagePhys_BTA.setObjectName(_fromUtf8("ImagePhys_BTA"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.ImagePhys_BTA)
        self.ImagePhys_RevSTA = QtGui.QPushButton(self.widget1)
        self.ImagePhys_RevSTA.setEnabled(False)
        self.ImagePhys_RevSTA.setObjectName(_fromUtf8("ImagePhys_RevSTA"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.ImagePhys_RevSTA)
        self.widget2 = QtGui.QWidget(self.groupBox_3)
        self.widget2.setGeometry(QtCore.QRect(15, 30, 236, 86))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.widget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 2)
        self.ImagePhys_burstISI = QtGui.QDoubleSpinBox(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_burstISI.setFont(font)
        self.ImagePhys_burstISI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_burstISI.setDecimals(1)
        self.ImagePhys_burstISI.setMinimum(1.0)
        self.ImagePhys_burstISI.setMaximum(1000.0)
        self.ImagePhys_burstISI.setSingleStep(10.0)
        self.ImagePhys_burstISI.setProperty("value", 100.0)
        self.ImagePhys_burstISI.setObjectName(_fromUtf8("ImagePhys_burstISI"))
        self.gridLayout_3.addWidget(self.ImagePhys_burstISI, 0, 2, 1, 1)
        self.ImagePhys_minBurstSpikes = QtGui.QSpinBox(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_minBurstSpikes.setFont(font)
        self.ImagePhys_minBurstSpikes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_minBurstSpikes.setMinimum(2)
        self.ImagePhys_minBurstSpikes.setMaximum(20)
        self.ImagePhys_minBurstSpikes.setProperty("value", 3)
        self.ImagePhys_minBurstSpikes.setObjectName(_fromUtf8("ImagePhys_minBurstSpikes"))
        self.gridLayout_3.addWidget(self.ImagePhys_minBurstSpikes, 2, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 2)
        self.ImagePhys_withinBurstISI = QtGui.QDoubleSpinBox(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_withinBurstISI.setFont(font)
        self.ImagePhys_withinBurstISI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_withinBurstISI.setDecimals(1)
        self.ImagePhys_withinBurstISI.setMinimum(1.0)
        self.ImagePhys_withinBurstISI.setMaximum(1000.0)
        self.ImagePhys_withinBurstISI.setSingleStep(2.0)
        self.ImagePhys_withinBurstISI.setProperty("value", 40.0)
        self.ImagePhys_withinBurstISI.setObjectName(_fromUtf8("ImagePhys_withinBurstISI"))
        self.gridLayout_3.addWidget(self.ImagePhys_withinBurstISI, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 2, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.ImagePhys_PhysSign.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Physiology Analysis Functions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Physiology", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "LPF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Event Thresh", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysThresh.setSuffix(QtGui.QApplication.translate("Form", " pA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Event Sign", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysSign.setItemText(0, QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysSign.setItemText(1, QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DetectSpikes.setText(QtGui.QApplication.translate("Form", "Detect Spikes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Spike Triggered Averages", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_STA.setText(QtGui.QApplication.translate("Form", "Spike-triggered Average", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_BTA.setText(QtGui.QApplication.translate("Form", "Burst-triggered Average", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RevSTA.setText(QtGui.QApplication.translate("Form", "Rev STA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Minimum # spikes/burst", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Min Interburst Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Max burst ISI (msec)", None, QtGui.QApplication.UnicodeUTF8))

