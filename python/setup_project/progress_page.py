# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from sgtk.platform.qt import QtGui
from sgtk.platform.qt import QtCore

from .base_page import BasePage


class RunSetupThread(QtCore.QThread):
    """ Simple thread to run the wizard in the background """
    success = QtCore.Signal()
    failure = QtCore.Signal(str)

    def __init__(self, wizard, parent=None):
        QtCore.QThread.__init__(self, parent)
        self._wizard = wizard

    def run(self):
        try:
            self._wizard.execute()
            self.success.emit()
        except Exception, e:
            self.failure.emit(str(e))


class ProgressPage(BasePage):
    """ Page to show the progress bar during configuration setup. """
    def setup_ui(self, page_id):
        BasePage.setup_ui(self, page_id)

        # setup additional details behavior
        self._down_arrow = QtGui.QIcon(":/tk-framework-adminui/setup_project/down_arrow.png")
        self._right_arrow = QtGui.QIcon(":/tk-framework-adminui/setup_project/right_arrow.png")

        wiz = self.wizard()
        wiz.ui.progress_output.hide()
        wiz.ui.additional_details_button.pressed.connect(self.additional_details_pressed)
        wiz.ui.additional_details_button.setIcon(self._right_arrow)

    def initializePage(self):
        # disable the cancel and back buttons
        wiz = self.wizard()
        wiz.button(wiz.CancelButton).setVisible(False)
        wiz.button(wiz.BackButton).setVisible(False)
        wiz.button(wiz.FinishButton).setEnabled(False)
        wiz.setButtonText(wiz.FinishButton, "Running...")

        # setup for progress reporting
        wiz.ui.progress.setValue(0)
        wiz.core_wizard.set_progress_callback(self.progress_callback)

        # run the thread
        self.execute_thread = RunSetupThread(wiz.core_wizard)
        self.execute_thread.success.connect(self._on_run_succeeded)
        self.execute_thread.failure.connect(self._on_run_failed)
        self.execute_thread.start()

    def additional_details_pressed(self):
        # handle the additional details toggle being pressed
        wiz = self.wizard()
        if wiz.ui.progress_output.isVisible():
            # hide the additional details
            wiz.ui.progress_output.hide()
            wiz.ui.additional_details_button.setText("Show details")
            wiz.ui.additional_details_button.setIcon(self._right_arrow)
        else:
            # show the additional details
            wiz.ui.progress_output.show()
            wiz.ui.additional_details_button.setText("Hide details")
            wiz.ui.additional_details_button.setIcon(self._down_arrow)

    def append_log_message(self, text):
        # append the log message to the end of the logging area
        wiz = self.wizard()
        wiz.ui.progress_output.appendHtml(text)
        cursor = wiz.ui.progress_output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.movePosition(cursor.StartOfLine)
        wiz.ui.progress_output.setTextCursor(cursor)
        wiz.ui.progress_output.ensureCursorVisible()

    def progress_callback(self, chapter, progress):
        if progress is not None:
            wiz = self.wizard()
            wiz.ui.progress.setValue(progress)
        print chapter

    def _on_run_finished(self):
        # thread has finished
        # clean up the page state
        wiz = self.wizard()
        wiz.button(wiz.FinishButton).setEnabled(True)

    def _on_run_succeeded(self):
        # thread finished successfully
        self._on_run_finished()

        wiz = self.wizard()
        wiz.ui.progress.setValue(100)
        wiz.setButtonText(wiz.FinishButton, "Done")

    def _on_run_failed(self, message):
        # thread failed
        self._on_run_finished()

        # show the failure icon and message
        wiz = self.wizard()
        wiz.setButtonText(wiz.FinishButton, "Quit")
        wiz.ui.complete_errors.setText(message)

    def isFinalPage(self):
        return True

    def validatePage(self):
        return self.execute_thread.isFinished()
