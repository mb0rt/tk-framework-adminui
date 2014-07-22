# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_project.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(456, 408)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/shotgun_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Wizard.setWindowIcon(icon)
        Wizard.setModal(True)
        Wizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        Wizard.setOptions(QtGui.QWizard.CancelButtonOnLeft|QtGui.QWizard.DisabledBackButtonOnLastPage|QtGui.QWizard.IndependentPages)
        Wizard.setTitleFormat(QtCore.Qt.RichText)
        self.setup_type_page = SetupTypePage()
        self.setup_type_page.setStyleSheet("QRadioButton {\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 12px;\n"
"    color: rgb(120, 120,120);\n"
"}")
        self.setup_type_page.setObjectName("setup_type_page")
        self.verticalLayout = QtGui.QVBoxLayout(self.setup_type_page)
        self.verticalLayout.setContentsMargins(25, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.select_standard = QtGui.QRadioButton(self.setup_type_page)
        self.select_standard.setChecked(True)
        self.select_standard.setObjectName("select_standard")
        self.verticalLayout.addWidget(self.select_standard)
        self.label_standard = QtGui.QLabel(self.setup_type_page)
        self.label_standard.setIndent(20)
        self.label_standard.setObjectName("label_standard")
        self.verticalLayout.addWidget(self.label_standard)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.select_project = QtGui.QRadioButton(self.setup_type_page)
        self.select_project.setObjectName("select_project")
        self.verticalLayout.addWidget(self.select_project)
        self.label_project = QtGui.QLabel(self.setup_type_page)
        self.label_project.setIndent(20)
        self.label_project.setObjectName("label_project")
        self.verticalLayout.addWidget(self.label_project)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.select_github = QtGui.QRadioButton(self.setup_type_page)
        self.select_github.setObjectName("select_github")
        self.verticalLayout.addWidget(self.select_github)
        self.label_github = QtGui.QLabel(self.setup_type_page)
        self.label_github.setIndent(20)
        self.label_github.setObjectName("label_github")
        self.verticalLayout.addWidget(self.label_github)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.select_disk = QtGui.QRadioButton(self.setup_type_page)
        self.select_disk.setObjectName("select_disk")
        self.verticalLayout.addWidget(self.select_disk)
        self.label_disk = QtGui.QLabel(self.setup_type_page)
        self.label_disk.setIndent(20)
        self.label_disk.setObjectName("label_disk")
        self.verticalLayout.addWidget(self.label_disk)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        Wizard.addPage(self.setup_type_page)
        self.project_config_page = ProjectConfigPage()
        self.project_config_page.setObjectName("project_config_page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.project_config_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.project_list = QtGui.QListView(self.project_config_page)
        self.project_list.setFrameShape(QtGui.QFrame.NoFrame)
        self.project_list.setFrameShadow(QtGui.QFrame.Plain)
        self.project_list.setAutoScroll(False)
        self.project_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.project_list.setProperty("showDropIndicator", False)
        self.project_list.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.project_list.setTextElideMode(QtCore.Qt.ElideNone)
        self.project_list.setMovement(QtGui.QListView.Static)
        self.project_list.setFlow(QtGui.QListView.LeftToRight)
        self.project_list.setProperty("isWrapping", True)
        self.project_list.setResizeMode(QtGui.QListView.Adjust)
        self.project_list.setLayoutMode(QtGui.QListView.Batched)
        self.project_list.setSpacing(10)
        self.project_list.setViewMode(QtGui.QListView.IconMode)
        self.project_list.setUniformItemSizes(True)
        self.project_list.setWordWrap(True)
        self.project_list.setSelectionRectVisible(False)
        self.project_list.setObjectName("project_list")
        self.verticalLayout_2.addWidget(self.project_list)
        self.project_errors = QtGui.QLabel(self.project_config_page)
        self.project_errors.setStyleSheet("color: rgb(231, 109, 125);")
        self.project_errors.setText("")
        self.project_errors.setAlignment(QtCore.Qt.AlignCenter)
        self.project_errors.setWordWrap(True)
        self.project_errors.setObjectName("project_errors")
        self.verticalLayout_2.addWidget(self.project_errors)
        Wizard.addPage(self.project_config_page)
        self.github_config_page = GithubConfigPage()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.github_config_page.sizePolicy().hasHeightForWidth())
        self.github_config_page.setSizePolicy(sizePolicy)
        self.github_config_page.setObjectName("github_config_page")
        self.gridLayout = QtGui.QGridLayout(self.github_config_page)
        self.gridLayout.setContentsMargins(30, 30, 60, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.github_url = QtGui.QLineEdit(self.github_config_page)
        self.github_url.setText("")
        self.github_url.setObjectName("github_url")
        self.gridLayout.addWidget(self.github_url, 0, 1, 1, 1)
        self.octocat = QtGui.QLabel(self.github_config_page)
        self.octocat.setMaximumSize(QtCore.QSize(30, 30))
        self.octocat.setText("")
        self.octocat.setPixmap(QtGui.QPixmap(":/tk-framework-adminui/setup_project/octocats/original.png"))
        self.octocat.setScaledContents(True)
        self.octocat.setObjectName("octocat")
        self.gridLayout.addWidget(self.octocat, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        self.github_errors = QtGui.QLabel(self.github_config_page)
        self.github_errors.setStyleSheet("color: rgb(231, 109, 125);")
        self.github_errors.setText("")
        self.github_errors.setAlignment(QtCore.Qt.AlignCenter)
        self.github_errors.setWordWrap(True)
        self.github_errors.setObjectName("github_errors")
        self.gridLayout.addWidget(self.github_errors, 2, 0, 1, 2)
        self.gridLayout.setRowStretch(1, 1)
        Wizard.addPage(self.github_config_page)
        self.disk_config_page = DiskConfigPage()
        self.disk_config_page.setObjectName("disk_config_page")
        self.gridLayout_2 = QtGui.QGridLayout(self.disk_config_page)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.path = QtGui.QLineEdit(self.disk_config_page)
        self.path.setObjectName("path")
        self.gridLayout_2.addWidget(self.path, 0, 0, 1, 1)
        self.disk_browse_button = QtGui.QPushButton(self.disk_config_page)
        self.disk_browse_button.setObjectName("disk_browse_button")
        self.gridLayout_2.addWidget(self.disk_browse_button, 0, 1, 1, 1)
        self.disk_errors = QtGui.QLabel(self.disk_config_page)
        self.disk_errors.setStyleSheet("color: rgb(231, 109, 125);")
        self.disk_errors.setText("")
        self.disk_errors.setAlignment(QtCore.Qt.AlignCenter)
        self.disk_errors.setWordWrap(True)
        self.disk_errors.setObjectName("disk_errors")
        self.gridLayout_2.addWidget(self.disk_errors, 2, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        Wizard.addPage(self.disk_config_page)
        self.project_name_page = ProjectNamePage()
        self.project_name_page.setObjectName("project_name_page")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.project_name_page)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.project_name = QtGui.QLineEdit(self.project_name_page)
        self.project_name.setObjectName("project_name")
        self.verticalLayout_3.addWidget(self.project_name)
        self.project_directories = QtGui.QLabel(self.project_name_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_directories.sizePolicy().hasHeightForWidth())
        self.project_directories.setSizePolicy(sizePolicy)
        self.project_directories.setFrameShape(QtGui.QFrame.NoFrame)
        self.project_directories.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.project_directories.setObjectName("project_directories")
        self.verticalLayout_3.addWidget(self.project_directories)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.project_name_errors = QtGui.QLabel(self.project_name_page)
        self.project_name_errors.setStyleSheet("color: rgb(231, 109, 125);")
        self.project_name_errors.setText("")
        self.project_name_errors.setAlignment(QtCore.Qt.AlignCenter)
        self.project_name_errors.setWordWrap(True)
        self.project_name_errors.setObjectName("project_name_errors")
        self.verticalLayout_3.addWidget(self.project_name_errors)
        Wizard.addPage(self.project_name_page)
        self.config_location_page = ConfigLocationPage()
        self.config_location_page.setObjectName("config_location_page")
        self.gridLayout_3 = QtGui.QGridLayout(self.config_location_page)
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.linux_browse = QtGui.QPushButton(self.config_location_page)
        self.linux_browse.setEnabled(False)
        self.linux_browse.setObjectName("linux_browse")
        self.gridLayout_3.addWidget(self.linux_browse, 3, 3, 1, 1)
        self.mac_browse = QtGui.QPushButton(self.config_location_page)
        self.mac_browse.setEnabled(False)
        self.mac_browse.setObjectName("mac_browse")
        self.gridLayout_3.addWidget(self.mac_browse, 0, 3, 1, 1)
        self.mac_label = QtGui.QLabel(self.config_location_page)
        self.mac_label.setObjectName("mac_label")
        self.gridLayout_3.addWidget(self.mac_label, 0, 0, 1, 1)
        self.mac_path = QtGui.QLineEdit(self.config_location_page)
        self.mac_path.setObjectName("mac_path")
        self.gridLayout_3.addWidget(self.mac_path, 0, 2, 1, 1)
        self.windows_path = QtGui.QLineEdit(self.config_location_page)
        self.windows_path.setObjectName("windows_path")
        self.gridLayout_3.addWidget(self.windows_path, 2, 2, 1, 1)
        self.windows_label = QtGui.QLabel(self.config_location_page)
        self.windows_label.setObjectName("windows_label")
        self.gridLayout_3.addWidget(self.windows_label, 2, 0, 1, 1)
        self.linux_path = QtGui.QLineEdit(self.config_location_page)
        self.linux_path.setObjectName("linux_path")
        self.gridLayout_3.addWidget(self.linux_path, 3, 2, 1, 1)
        self.linux_label = QtGui.QLabel(self.config_location_page)
        self.linux_label.setObjectName("linux_label")
        self.gridLayout_3.addWidget(self.linux_label, 3, 0, 1, 1)
        self.windows_browse = QtGui.QPushButton(self.config_location_page)
        self.windows_browse.setEnabled(False)
        self.windows_browse.setObjectName("windows_browse")
        self.gridLayout_3.addWidget(self.windows_browse, 2, 3, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 4, 0, 1, 3)
        self.config_location_errors = QtGui.QLabel(self.config_location_page)
        self.config_location_errors.setStyleSheet("color: rgb(231, 109, 125);")
        self.config_location_errors.setText("")
        self.config_location_errors.setAlignment(QtCore.Qt.AlignCenter)
        self.config_location_errors.setWordWrap(True)
        self.config_location_errors.setObjectName("config_location_errors")
        self.gridLayout_3.addWidget(self.config_location_errors, 5, 0, 1, 4)
        Wizard.addPage(self.config_location_page)
        self.progress_page = ProgressPage()
        self.progress_page.setSubTitle("")
        self.progress_page.setObjectName("progress_page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.progress_page)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.complete_icon = QtGui.QLabel(self.progress_page)
        self.complete_icon.setMaximumSize(QtCore.QSize(80, 80))
        self.complete_icon.setText("")
        self.complete_icon.setPixmap(QtGui.QPixmap(":/tk-framework-adminui/setup_project/checkmark.png"))
        self.complete_icon.setScaledContents(True)
        self.complete_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.complete_icon.setObjectName("complete_icon")
        self.horizontalLayout.addWidget(self.complete_icon)
        self.complete_label = QtGui.QLabel(self.progress_page)
        self.complete_label.setAlignment(QtCore.Qt.AlignCenter)
        self.complete_label.setObjectName("complete_label")
        self.horizontalLayout.addWidget(self.complete_label)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.progress_output = QtGui.QPlainTextEdit(self.progress_page)
        self.progress_output.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.progress_output.setUndoRedoEnabled(False)
        self.progress_output.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.progress_output.setReadOnly(True)
        self.progress_output.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.progress_output.setObjectName("progress_output")
        self.verticalLayout_5.addWidget(self.progress_output)
        self.complete_errors = QtGui.QLabel(self.progress_page)
        self.complete_errors.setStyleSheet("color: rgb(231, 109, 125);")
        self.complete_errors.setText("")
        self.complete_errors.setAlignment(QtCore.Qt.AlignCenter)
        self.complete_errors.setWordWrap(True)
        self.complete_errors.setObjectName("complete_errors")
        self.verticalLayout_5.addWidget(self.complete_errors)
        Wizard.addPage(self.progress_page)
        self.label_standard.setBuddy(self.select_standard)
        self.label_project.setBuddy(self.select_project)
        self.label_github.setBuddy(self.select_github)
        self.label_disk.setBuddy(self.select_disk)
        self.octocat.setBuddy(self.github_url)
        self.project_directories.setBuddy(self.project_name)
        self.mac_label.setBuddy(self.mac_path)
        self.windows_label.setBuddy(self.windows_path)
        self.linux_label.setBuddy(self.linux_path)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)
        Wizard.setTabOrder(self.select_standard, self.select_project)
        Wizard.setTabOrder(self.select_project, self.select_github)
        Wizard.setTabOrder(self.select_github, self.select_disk)
        Wizard.setTabOrder(self.select_disk, self.project_list)
        Wizard.setTabOrder(self.project_list, self.github_url)
        Wizard.setTabOrder(self.github_url, self.path)
        Wizard.setTabOrder(self.path, self.disk_browse_button)
        Wizard.setTabOrder(self.disk_browse_button, self.project_name)
        Wizard.setTabOrder(self.project_name, self.mac_path)
        Wizard.setTabOrder(self.mac_path, self.mac_browse)
        Wizard.setTabOrder(self.mac_browse, self.windows_path)
        Wizard.setTabOrder(self.windows_path, self.windows_browse)
        Wizard.setTabOrder(self.windows_browse, self.linux_path)
        Wizard.setTabOrder(self.linux_path, self.linux_browse)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QtGui.QApplication.translate("Wizard", "Shotgun Setup Project Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.setup_type_page.setTitle(QtGui.QApplication.translate("Wizard", "<p></p><font size=18>Select Configuration Type</font><p></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.setup_type_page.setSubTitle(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sitLorm ispum dolor sit Lorem", None, QtGui.QApplication.UnicodeUTF8))
        self.select_standard.setText(QtGui.QApplication.translate("Wizard", "Standard Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_standard.setText(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sit", None, QtGui.QApplication.UnicodeUTF8))
        self.select_project.setText(QtGui.QApplication.translate("Wizard", "Use Another Project\'s Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_project.setText(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sit", None, QtGui.QApplication.UnicodeUTF8))
        self.select_github.setText(QtGui.QApplication.translate("Wizard", "Use a Configuration from Github", None, QtGui.QApplication.UnicodeUTF8))
        self.label_github.setText(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sit", None, QtGui.QApplication.UnicodeUTF8))
        self.select_disk.setText(QtGui.QApplication.translate("Wizard", "Use a Configuration from Disk", None, QtGui.QApplication.UnicodeUTF8))
        self.label_disk.setText(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sit", None, QtGui.QApplication.UnicodeUTF8))
        self.project_config_page.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Select a Project to copy the config from.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_config_page.setTitle(QtGui.QApplication.translate("Wizard", "<p></p><font size=18>Select Project</font><p></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_config_page.setSubTitle(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sitLorm ispum dolor sit Lorem", None, QtGui.QApplication.UnicodeUTF8))
        self.github_config_page.setTitle(QtGui.QApplication.translate("Wizard", "<p></p><font size=18>Select GitHub URL</font><p></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.github_config_page.setSubTitle(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sitLorm ispum dolor sit Lorem", None, QtGui.QApplication.UnicodeUTF8))
        self.github_url.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Enter the url to a github repo containing a configuration to clone.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.github_url.setPlaceholderText(QtGui.QApplication.translate("Wizard", "GitHub URL", None, QtGui.QApplication.UnicodeUTF8))
        self.disk_config_page.setTitle(QtGui.QApplication.translate("Wizard", "<p></p><font size=18>Select Source Path</font><p></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.disk_config_page.setSubTitle(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sitLorm ispum dolor sit Lorem", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Enter the path to a configuration on disk.  Either a valid configuration directory or a zip of one.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setPlaceholderText(QtGui.QApplication.translate("Wizard", "/Path/To/Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.disk_browse_button.setText(QtGui.QApplication.translate("Wizard", "&Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name_page.setTitle(QtGui.QApplication.translate("Wizard", "<p></p><font size=18>Enter Project Name </font><p></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name_page.setSubTitle(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sitLorm ispum dolor sit Lorem", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Enter a valid project name.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name.setPlaceholderText(QtGui.QApplication.translate("Wizard", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.project_directories.setText(QtGui.QApplication.translate("Wizard", "<html><head/><body><p><span style=\" font-size:large;\">Project Directories will be:</span></p><p>/mnt/foo/bar</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.config_location_page.setTitle(QtGui.QApplication.translate("Wizard", "<p></p><font size=18>Select Config Location</font><p></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.config_location_page.setSubTitle(QtGui.QApplication.translate("Wizard", "Lorem ispum dolor sitLorm ispum dolor sit Lorem", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_browse.setText(QtGui.QApplication.translate("Wizard", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_browse.setText(QtGui.QApplication.translate("Wizard", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_label.setText(QtGui.QApplication.translate("Wizard", "Mac:", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_path.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Enter the path on disk where the configuration will be stored.</p><p>The current operating system\'s directory will be used to install the configuration.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_path.setPlaceholderText(QtGui.QApplication.translate("Wizard", "/Path/On/Mac", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_path.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Enter the path on disk where the configuration will be stored.</p><p>The current operating system\'s directory will be used to install the configuration.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_path.setPlaceholderText(QtGui.QApplication.translate("Wizard", "\\\\Path\\On\\Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_label.setText(QtGui.QApplication.translate("Wizard", "Windows:", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_path.setToolTip(QtGui.QApplication.translate("Wizard", "<html><head/><body><p>Enter the path on disk where the configuration will be stored.</p><p>The current operating system\'s directory will be used to install the configuration.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_path.setPlaceholderText(QtGui.QApplication.translate("Wizard", "/path/on/linux", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_label.setText(QtGui.QApplication.translate("Wizard", "Linux:", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_browse.setText(QtGui.QApplication.translate("Wizard", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.complete_label.setText(QtGui.QApplication.translate("Wizard", "<html><head/><body><p><span style=\" font-size:26pt;\">Setting up Project</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

from ..setup_project.setup_type_page import SetupTypePage
from ..setup_project.config_location_page import ConfigLocationPage
from ..setup_project.project_config_page import ProjectConfigPage
from ..setup_project.github_config_page import GithubConfigPage
from ..setup_project.disk_config_page import DiskConfigPage
from ..setup_project.project_name_page import ProjectNamePage
from ..setup_project.progress_page import ProgressPage
from . import resources_rc
