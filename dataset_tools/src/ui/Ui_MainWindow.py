# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 1030)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dataset_type = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataset_type.setFont(font)
        self.dataset_type.setObjectName("dataset_type")
        self.verticalLayout_9.addWidget(self.dataset_type)
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(500, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollBars = QtWidgets.QWidget()
        self.scrollBars.setGeometry(QtCore.QRect(0, 0, 643, 694))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollBars.sizePolicy().hasHeightForWidth())
        self.scrollBars.setSizePolicy(sizePolicy)
        self.scrollBars.setObjectName("scrollBars")
        self.scrollArea.setWidget(self.scrollBars)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.label_info_text = QtWidgets.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info_text.sizePolicy().hasHeightForWidth())
        self.label_info_text.setSizePolicy(sizePolicy)
        self.label_info_text.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_info_text.setObjectName("label_info_text")
        self.verticalLayout_9.addWidget(self.label_info_text)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1105, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView_2 = QtWidgets.QMenu(self.menuBar)
        self.menuView_2.setObjectName("menuView_2")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuTools_2 = QtWidgets.QMenu(self.menuBar)
        self.menuTools_2.setObjectName("menuTools_2")
        self.menuDepth = QtWidgets.QMenu(self.menuBar)
        self.menuDepth.setObjectName("menuDepth")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dock_file_list = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dock_file_list.sizePolicy().hasHeightForWidth())
        self.dock_file_list.setSizePolicy(sizePolicy)
        self.dock_file_list.setMaximumSize(QtCore.QSize(300, 524287))
        self.dock_file_list.setObjectName("dock_file_list")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fileList = QtWidgets.QListWidget(self.dockWidgetContents)
        self.fileList.setObjectName("fileList")
        self.verticalLayout_5.addWidget(self.fileList)
        self.dock_file_list.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_file_list)
        self.dock_resize_files = QtWidgets.QDockWidget(MainWindow)
        self.dock_resize_files.setObjectName("dock_resize_files")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.dockWidgetContents_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.resize_mode = QtWidgets.QComboBox(self.widget)
        self.resize_mode.setObjectName("resize_mode")
        self.resize_mode.addItem("")
        self.resize_mode.addItem("")
        self.resize_mode.addItem("")
        self.resize_mode.addItem("")
        self.resize_mode.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.resize_mode)
        self.label_width = QtWidgets.QLabel(self.widget)
        self.label_width.setObjectName("label_width")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_width)
        self.new_img_width = QtWidgets.QSpinBox(self.widget)
        self.new_img_width.setMaximum(20000)
        self.new_img_width.setProperty("value", 500)
        self.new_img_width.setObjectName("new_img_width")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.new_img_width)
        self.label_height = QtWidgets.QLabel(self.widget)
        self.label_height.setObjectName("label_height")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_height)
        self.new_img_height = QtWidgets.QSpinBox(self.widget)
        self.new_img_height.setMaximum(20000)
        self.new_img_height.setProperty("value", 500)
        self.new_img_height.setObjectName("new_img_height")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.new_img_height)
        self.label_scale = QtWidgets.QLabel(self.widget)
        self.label_scale.setObjectName("label_scale")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_scale)
        self.img_scale_ratio = QtWidgets.QDoubleSpinBox(self.widget)
        self.img_scale_ratio.setEnabled(True)
        self.img_scale_ratio.setDecimals(6)
        self.img_scale_ratio.setSingleStep(0.01)
        self.img_scale_ratio.setProperty("value", 1.0)
        self.img_scale_ratio.setObjectName("img_scale_ratio")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.img_scale_ratio)
        self.label_resize_roi = QtWidgets.QLabel(self.widget)
        self.label_resize_roi.setObjectName("label_resize_roi")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_resize_roi)
        self.label_resize_file = QtWidgets.QLabel(self.widget)
        self.label_resize_file.setObjectName("label_resize_file")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_resize_file)
        self.resize_file = QtWidgets.QLineEdit(self.widget)
        self.resize_file.setObjectName("resize_file")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.resize_file)
        self.roi_widget = ROIWidget(self.widget)
        self.roi_widget.setObjectName("roi_widget")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.roi_widget)
        self.verticalLayout_7.addWidget(self.widget)
        self.widget_rgb_resize = RGBWidget(self.frame)
        self.widget_rgb_resize.setObjectName("widget_rgb_resize")
        self.verticalLayout_7.addWidget(self.widget_rgb_resize)
        self.resize_images = QtWidgets.QPushButton(self.frame)
        self.resize_images.setObjectName("resize_images")
        self.verticalLayout_7.addWidget(self.resize_images)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame)
        self.dock_resize_files.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_resize_files)
        self.dock_change_pixel_values = QtWidgets.QDockWidget(MainWindow)
        self.dock_change_pixel_values.setObjectName("dock_change_pixel_values")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame1 = QtWidgets.QFrame(self.dockWidgetContents_3)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.old_value_text = QtWidgets.QLineEdit(self.frame1)
        self.old_value_text.setObjectName("old_value_text")
        self.gridLayout.addWidget(self.old_value_text, 1, 0, 1, 1)
        self.modifyPixelValues = QtWidgets.QPushButton(self.frame1)
        self.modifyPixelValues.setObjectName("modifyPixelValues")
        self.gridLayout.addWidget(self.modifyPixelValues, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.newPixelValue = QtWidgets.QSpinBox(self.frame1)
        self.newPixelValue.setMaximum(256)
        self.newPixelValue.setProperty("value", 1)
        self.newPixelValue.setObjectName("newPixelValue")
        self.gridLayout.addWidget(self.newPixelValue, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.modify_none_zero = QtWidgets.QCheckBox(self.frame1)
        self.modify_none_zero.setChecked(True)
        self.modify_none_zero.setObjectName("modify_none_zero")
        self.gridLayout.addWidget(self.modify_none_zero, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame1)
        self.dock_change_pixel_values.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_change_pixel_values)
        self.dock_logger = QtWidgets.QDockWidget(MainWindow)
        self.dock_logger.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dock_logger.setObjectName("dock_logger")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.dockWidgetContents_4)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setSpacing(6)
        self.formLayout_4.setObjectName("formLayout_4")
        self.loggingLevel = QtWidgets.QComboBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loggingLevel.sizePolicy().hasHeightForWidth())
        self.loggingLevel.setSizePolicy(sizePolicy)
        self.loggingLevel.setObjectName("loggingLevel")
        self.loggingLevel.addItem("")
        self.loggingLevel.addItem("")
        self.loggingLevel.addItem("")
        self.loggingLevel.addItem("")
        self.loggingLevel.addItem("")
        self.loggingLevel.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.loggingLevel)
        self.clear_log = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_log.sizePolicy().hasHeightForWidth())
        self.clear_log.setSizePolicy(sizePolicy)
        self.clear_log.setObjectName("clear_log")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.clear_log)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.logger = QtWidgets.QPlainTextEdit(self.dockWidgetContents_4)
        self.logger.setObjectName("logger")
        self.verticalLayout_4.addWidget(self.logger)
        self.dock_logger.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dock_logger)
        self.dock_augment_data = QtWidgets.QDockWidget(MainWindow)
        self.dock_augment_data.setObjectName("dock_augment_data")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_contrast = MinMaxWidget(self.dockWidgetContents_6)
        self.widget_contrast.setObjectName("widget_contrast")
        self.verticalLayout_6.addWidget(self.widget_contrast)
        self.widget_brightness = MinMaxWidget(self.dockWidgetContents_6)
        self.widget_brightness.setObjectName("widget_brightness")
        self.verticalLayout_6.addWidget(self.widget_brightness)
        self.widget_scale = MinMaxWidget(self.dockWidgetContents_6)
        self.widget_scale.setObjectName("widget_scale")
        self.verticalLayout_6.addWidget(self.widget_scale)
        self.widget_rotation = MinMaxWidget(self.dockWidgetContents_6)
        self.widget_rotation.setObjectName("widget_rotation")
        self.verticalLayout_6.addWidget(self.widget_rotation)
        self.widget_translation = MinMaxWidget(self.dockWidgetContents_6)
        self.widget_translation.setObjectName("widget_translation")
        self.verticalLayout_6.addWidget(self.widget_translation)
        self.widget_rgb_increase = RGBWidget(self.dockWidgetContents_6)
        self.widget_rgb_increase.setObjectName("widget_rgb_increase")
        self.verticalLayout_6.addWidget(self.widget_rgb_increase)
        self.widget_2 = QtWidgets.QWidget(self.dockWidgetContents_6)
        self.widget_2.setObjectName("widget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.augment_times = QtWidgets.QSpinBox(self.widget_2)
        self.augment_times.setProperty("value", 10)
        self.augment_times.setObjectName("augment_times")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.augment_times)
        self.remain_ratio_in_aug = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.remain_ratio_in_aug.setMaximum(1.0)
        self.remain_ratio_in_aug.setProperty("value", 0.97)
        self.remain_ratio_in_aug.setObjectName("remain_ratio_in_aug")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.remain_ratio_in_aug)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.augment_data = QtWidgets.QPushButton(self.dockWidgetContents_6)
        self.augment_data.setObjectName("augment_data")
        self.verticalLayout_6.addWidget(self.augment_data)
        self.dock_augment_data.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_augment_data)
        self.dock_rename_files = QtWidgets.QDockWidget(MainWindow)
        self.dock_rename_files.setObjectName("dock_rename_files")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_7)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rename_files = QtWidgets.QPushButton(self.dockWidgetContents_7)
        self.rename_files.setObjectName("rename_files")
        self.gridLayout_2.addWidget(self.rename_files, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.dockWidgetContents_7)
        self.widget_3.setObjectName("widget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.prefix_list = QtWidgets.QComboBox(self.widget_3)
        self.prefix_list.setObjectName("prefix_list")
        self.prefix_list.addItem("")
        self.prefix_list.addItem("")
        self.prefix_list.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prefix_list)
        self.start_idx = QtWidgets.QSpinBox(self.widget_3)
        self.start_idx.setMaximum(10000000)
        self.start_idx.setObjectName("start_idx")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.start_idx)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)
        self.dock_rename_files.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_rename_files)
        self.dock_merge_dir = QtWidgets.QDockWidget(MainWindow)
        self.dock_merge_dir.setObjectName("dock_merge_dir")
        self.dockWidgetContents_8 = QtWidgets.QWidget()
        self.dockWidgetContents_8.setObjectName("dockWidgetContents_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_3 = MergeDirDialog(self.dockWidgetContents_8)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8.addWidget(self.frame_3)
        self.dock_merge_dir.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_merge_dir)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.mainToolBar.setOrientation(QtCore.Qt.Vertical)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.mainToolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_Dir = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen_Dir.setIcon(icon1)
        self.actionOpen_Dir.setObjectName("actionOpen_Dir")
        self.actionOpen_Recent = QtWidgets.QAction(MainWindow)
        self.actionOpen_Recent.setObjectName("actionOpen_Recent")
        self.actionNext_Image = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext_Image.setIcon(icon2)
        self.actionNext_Image.setObjectName("actionNext_Image")
        self.actionPrev_Image = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrev_Image.setIcon(icon3)
        self.actionPrev_Image.setObjectName("actionPrev_Image")
        self.actionShow_File_List = QtWidgets.QAction(MainWindow)
        self.actionShow_File_List.setCheckable(True)
        self.actionShow_File_List.setChecked(True)
        self.actionShow_File_List.setObjectName("actionShow_File_List")
        self.actionResize_Params = QtWidgets.QAction(MainWindow)
        self.actionResize_Params.setCheckable(True)
        self.actionResize_Params.setChecked(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionResize_Params.setIcon(icon4)
        self.actionResize_Params.setObjectName("actionResize_Params")
        self.actionChange_Pixel_Values = QtWidgets.QAction(MainWindow)
        self.actionChange_Pixel_Values.setCheckable(True)
        self.actionChange_Pixel_Values.setChecked(False)
        self.actionChange_Pixel_Values.setIcon(icon4)
        self.actionChange_Pixel_Values.setObjectName("actionChange_Pixel_Values")
        self.actionMerge_Dir = QtWidgets.QAction(MainWindow)
        self.actionMerge_Dir.setCheckable(True)
        self.actionMerge_Dir.setChecked(True)
        self.actionMerge_Dir.setIcon(icon4)
        self.actionMerge_Dir.setObjectName("actionMerge_Dir")
        self.actionSplit_Dir = QtWidgets.QAction(MainWindow)
        self.actionSplit_Dir.setObjectName("actionSplit_Dir")
        self.actionAugment_Data = QtWidgets.QAction(MainWindow)
        self.actionAugment_Data.setCheckable(True)
        self.actionAugment_Data.setIcon(icon4)
        self.actionAugment_Data.setObjectName("actionAugment_Data")
        self.actionRename_Files = QtWidgets.QAction(MainWindow)
        self.actionRename_Files.setCheckable(True)
        self.actionRename_Files.setIcon(icon4)
        self.actionRename_Files.setObjectName("actionRename_Files")
        self.actionShow_Log = QtWidgets.QAction(MainWindow)
        self.actionShow_Log.setCheckable(True)
        self.actionShow_Log.setChecked(True)
        self.actionShow_Log.setObjectName("actionShow_Log")
        self.actionVoc_Data_Format = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVoc_Data_Format.setIcon(icon5)
        self.actionVoc_Data_Format.setObjectName("actionVoc_Data_Format")
        self.actionWrite_File_List = QtWidgets.QAction(MainWindow)
        self.actionWrite_File_List.setIcon(icon4)
        self.actionWrite_File_List.setObjectName("actionWrite_File_List")
        self.actionMerge_Images_Labels = QtWidgets.QAction(MainWindow)
        self.actionMerge_Images_Labels.setIcon(icon4)
        self.actionMerge_Images_Labels.setObjectName("actionMerge_Images_Labels")
        self.actionXml_To_Json = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/fit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionXml_To_Json.setIcon(icon6)
        self.actionXml_To_Json.setObjectName("actionXml_To_Json")
        self.actionJson_To_Xml = QtWidgets.QAction(MainWindow)
        self.actionJson_To_Xml.setIcon(icon6)
        self.actionJson_To_Xml.setObjectName("actionJson_To_Xml")
        self.actionStart_Format_DataSet = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStart_Format_DataSet.setIcon(icon7)
        self.actionStart_Format_DataSet.setObjectName("actionStart_Format_DataSet")
        self.actionBmp_To_Jpg = QtWidgets.QAction(MainWindow)
        self.actionBmp_To_Jpg.setIcon(icon4)
        self.actionBmp_To_Jpg.setObjectName("actionBmp_To_Jpg")
        self.actionShuffle = QtWidgets.QAction(MainWindow)
        self.actionShuffle.setIcon(icon4)
        self.actionShuffle.setObjectName("actionShuffle")
        self.actionDepth_Encoding = QtWidgets.QAction(MainWindow)
        self.actionDepth_Encoding.setObjectName("actionDepth_Encoding")
        self.actionCompute_rgb_mean = QtWidgets.QAction(MainWindow)
        self.actionCompute_rgb_mean.setObjectName("actionCompute_rgb_mean")
        self.actionSave_mask = QtWidgets.QAction(MainWindow)
        self.actionSave_mask.setObjectName("actionSave_mask")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuView_2.addAction(self.actionPrev_Image)
        self.menuView_2.addAction(self.actionNext_Image)
        self.menuView.addAction(self.actionShow_File_List)
        self.menuView.addAction(self.actionResize_Params)
        self.menuView.addAction(self.actionChange_Pixel_Values)
        self.menuView.addAction(self.actionAugment_Data)
        self.menuView.addAction(self.actionRename_Files)
        self.menuView.addAction(self.actionMerge_Dir)
        self.menuView.addAction(self.actionShow_Log)
        self.menuTools.addAction(self.actionVoc_Data_Format)
        self.menuTools.addAction(self.actionXml_To_Json)
        self.menuTools.addAction(self.actionJson_To_Xml)
        self.menuTools_2.addAction(self.actionWrite_File_List)
        self.menuTools_2.addAction(self.actionMerge_Images_Labels)
        self.menuTools_2.addAction(self.actionSplit_Dir)
        self.menuTools_2.addAction(self.actionShuffle)
        self.menuTools_2.addAction(self.actionCompute_rgb_mean)
        self.menuTools_2.addAction(self.actionSave_mask)
        self.menuDepth.addAction(self.actionDepth_Encoding)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView_2.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuTools_2.menuAction())
        self.menuBar.addAction(self.menuDepth.menuAction())
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addAction(self.actionOpen_Dir)
        self.mainToolBar.addAction(self.actionStart_Format_DataSet)
        self.mainToolBar.addAction(self.actionXml_To_Json)
        self.mainToolBar.addAction(self.actionJson_To_Xml)
        self.mainToolBar.addAction(self.actionWrite_File_List)
        self.mainToolBar.addAction(self.actionResize_Params)
        self.mainToolBar.addAction(self.actionRename_Files)
        self.mainToolBar.addAction(self.actionAugment_Data)
        self.mainToolBar.addAction(self.actionMerge_Dir)
        self.mainToolBar.addAction(self.actionChange_Pixel_Values)
        self.mainToolBar.addAction(self.actionBmp_To_Jpg)
        self.mainToolBar.addAction(self.actionShuffle)
        self.mainToolBar.addAction(self.actionVoc_Data_Format)
        self.mainToolBar.addAction(self.actionDepth_Encoding)
        self.mainToolBar.addAction(self.actionCompute_rgb_mean)

        self.retranslateUi(MainWindow)
        self.loggingLevel.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dataset Tools"))
        self.dataset_type.setText(_translate("MainWindow", "Dataset Type: "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView_2.setTitle(_translate("MainWindow", "Canvas"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTools.setTitle(_translate("MainWindow", "Data Format"))
        self.menuTools_2.setTitle(_translate("MainWindow", "Tools"))
        self.menuDepth.setTitle(_translate("MainWindow", "Depth"))
        self.dock_file_list.setWindowTitle(_translate("MainWindow", "File List"))
        self.dock_resize_files.setWindowTitle(_translate("MainWindow", "Resize Params"))
        self.label_6.setText(_translate("MainWindow", "Mode"))
        self.resize_mode.setItemText(0, _translate("MainWindow", "Auto Fill"))
        self.resize_mode.setItemText(1, _translate("MainWindow", "Maintain H/W Ratio"))
        self.resize_mode.setItemText(2, _translate("MainWindow", "Crop"))
        self.resize_mode.setItemText(3, _translate("MainWindow", "ROI"))
        self.resize_mode.setItemText(4, _translate("MainWindow", "FILE"))
        self.label_width.setText(_translate("MainWindow", "New Image Width"))
        self.label_height.setText(_translate("MainWindow", "New Image Height"))
        self.label_scale.setText(_translate("MainWindow", "Scale Ratio"))
        self.label_resize_roi.setText(_translate("MainWindow", "ROI"))
        self.label_resize_file.setText(_translate("MainWindow", "Example File"))
        self.resize_images.setText(_translate("MainWindow", "Resize images"))
        self.dock_change_pixel_values.setWindowTitle(_translate("MainWindow", "Change Pixel Values"))
        self.label_4.setText(_translate("MainWindow", "new value"))
        self.old_value_text.setToolTip(_translate("MainWindow", "No White Space"))
        self.old_value_text.setText(_translate("MainWindow", "1,2"))
        self.modifyPixelValues.setText(_translate("MainWindow", "Modify Pixel Values"))
        self.label_3.setText(_translate("MainWindow", "old value"))
        self.modify_none_zero.setText(_translate("MainWindow", "modify all none-zero pixel values"))
        self.dock_logger.setWindowTitle(_translate("MainWindow", "Log"))
        self.loggingLevel.setToolTip(_translate("MainWindow", "Logging level"))
        self.loggingLevel.setItemText(0, _translate("MainWindow", "Verbose"))
        self.loggingLevel.setItemText(1, _translate("MainWindow", "Debug"))
        self.loggingLevel.setItemText(2, _translate("MainWindow", "Info"))
        self.loggingLevel.setItemText(3, _translate("MainWindow", "Warning"))
        self.loggingLevel.setItemText(4, _translate("MainWindow", "Error"))
        self.loggingLevel.setItemText(5, _translate("MainWindow", "Fatal"))
        self.clear_log.setText(_translate("MainWindow", "Clear"))
        self.dock_augment_data.setWindowTitle(_translate("MainWindow", "Augment Data"))
        self.label_2.setText(_translate("MainWindow", "Remain Ratio in aug"))
        self.label.setText(_translate("MainWindow", "Augment Times"))
        self.augment_data.setText(_translate("MainWindow", "Start Data Augmention"))
        self.dock_rename_files.setWindowTitle(_translate("MainWindow", "Rename Files"))
        self.rename_files.setText(_translate("MainWindow", "Rename Files"))
        self.prefix_list.setItemText(0, _translate("MainWindow", "2007_"))
        self.prefix_list.setItemText(1, _translate("MainWindow", "rgb_image_"))
        self.prefix_list.setItemText(2, _translate("MainWindow", "self-defined"))
        self.label_5.setText(_translate("MainWindow", "Prefix"))
        self.label_8.setText(_translate("MainWindow", "Idx"))
        self.dock_merge_dir.setWindowTitle(_translate("MainWindow", "Merge Dir"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_Dir.setText(_translate("MainWindow", "Open Dir"))
        self.actionOpen_Dir.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionOpen_Recent.setText(_translate("MainWindow", "Open Recent"))
        self.actionNext_Image.setText(_translate("MainWindow", "Next Image"))
        self.actionNext_Image.setShortcut(_translate("MainWindow", "Right"))
        self.actionPrev_Image.setText(_translate("MainWindow", "Prev Image"))
        self.actionPrev_Image.setShortcut(_translate("MainWindow", "Left"))
        self.actionShow_File_List.setText(_translate("MainWindow", "Show File List"))
        self.actionResize_Params.setText(_translate("MainWindow", "Resize Params"))
        self.actionChange_Pixel_Values.setText(_translate("MainWindow", "Change Pixel Values"))
        self.actionMerge_Dir.setText(_translate("MainWindow", "Merge Dir"))
        self.actionSplit_Dir.setText(_translate("MainWindow", "Split Dir"))
        self.actionAugment_Data.setText(_translate("MainWindow", "Augment Data"))
        self.actionRename_Files.setText(_translate("MainWindow", "Rename Files"))
        self.actionShow_Log.setText(_translate("MainWindow", "Show Log"))
        self.actionVoc_Data_Format.setText(_translate("MainWindow", "Voc Data Format"))
        self.actionWrite_File_List.setText(_translate("MainWindow", "Write File List"))
        self.actionMerge_Images_Labels.setText(_translate("MainWindow", "Merge Images/Labels To One Dir"))
        self.actionXml_To_Json.setText(_translate("MainWindow", "Xml To Json"))
        self.actionJson_To_Xml.setText(_translate("MainWindow", "Json To Xml"))
        self.actionStart_Format_DataSet.setText(_translate("MainWindow", "Start Format DataSet"))
        self.actionBmp_To_Jpg.setText(_translate("MainWindow", "Bmp To Jpg"))
        self.actionShuffle.setText(_translate("MainWindow", "Shuffle and Rename"))
        self.actionDepth_Encoding.setText(_translate("MainWindow", "Depth Encoding"))
        self.actionCompute_rgb_mean.setText(_translate("MainWindow", "compute rgb mean"))
        self.actionCompute_rgb_mean.setToolTip(_translate("MainWindow", "compute rgb mean"))
        self.actionSave_mask.setText(_translate("MainWindow", "Save mask"))

from ui.MergeDirDialog import MergeDirDialog
from ui.MinMaxWidget import MinMaxWidget
from ui.RGBWidget import RGBWidget
from ui.ROIWidget import ROIWidget
