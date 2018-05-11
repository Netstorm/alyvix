# Alyvix allows you to automate and monitor all types of applications
# Copyright (C) 2015 Alan Pipitone
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Developer: Alan Pipitone (Violet Atom) - http://www.violetatom.com/
# Supporter: Wuerth Phoenix - http://www.wuerth-phoenix.com/
# Official website: http://www.alyvix.com/

import sys
import os
import time
import datetime
import cv2
import locale

from PyQt4.QtGui import QApplication, QDialog, QCursor, QImage, QPixmap, QListWidgetItem, QMessageBox, QKeySequence, QShortcut, QTableWidgetItem, QDateTimeEdit,QHeaderView, QAbstractItemView
from PyQt4.QtCore import Qt, QThread, SIGNAL, QTimer, QUrl, QString, QRect, QEvent, QDate,QDateTime, pyqtSlot, SLOT

from PyQt4.QtWebKit import QWebSettings

from alyvix_object_selection_view import Ui_Form
from alyvix_rect_finder_view import AlyvixRectFinderView
from alyvix_rect_finder_view import AlyvixRectFinderPropertiesView
from alyvix_image_finder_view import AlyvixImageFinderView
from alyvix_image_finder_view import AlyvixImageFinderPropertiesView
from alyvix_text_finder_view import AlyvixTextFinderView
from alyvix_text_finder_view import AlyvixTextFinderPropertiesView
from alyvix_object_finder_view import AlyvixObjectFinderView, PaintingView
from alyvix_code_view import AlyvixCustomCodeView

from alyvix.tools.screen import ScreenManager
from alyvix.tools.configreader import ConfigReader
from alyvix.tools.info import InfoManager


from stat import S_ISREG, ST_CTIME, ST_MODE, ST_MTIME

import shutil
from distutils.sysconfig import get_python_lib


class AlyvixMainMenuController(QDialog, Ui_Form):

    def __init__(self):
        QDialog.__init__(self)
        
        self._deleted_obj_name = None
        self._deleted_file_name = None


        info_manager = InfoManager()
        self.scaling_factor = info_manager.get_info("SCALING FACTOR FLOAT")

        # Set up the user interface from Designer.
        self.setupUi(self)
        
                
        #self.listWidgetAlyObj = listWidgetAlyObj2()

        self.resize(int(self.frameGeometry().width() * self.scaling_factor),
                          int(self.frameGeometry().height() * self.scaling_factor))

        self.widget.setGeometry(int(self.widget.x() * self.scaling_factor), int(self.widget.y()*self.scaling_factor),
                                            int(self.widget.width()*self.scaling_factor), int(self.widget.height()*self.scaling_factor))
                                            
        
        self.widget_2.setGeometry(QRect(int(self.widget_2.x()*self.scaling_factor), int(self.widget_2.y()*self.scaling_factor),
                                      int(self.widget_2.width()*self.scaling_factor), int(self.widget_2.height()*self.scaling_factor)))
                                      
        self.gridLayoutWidget.setGeometry(QRect(int(self.gridLayoutWidget.geometry().x() * self.scaling_factor), int(self.gridLayoutWidget.geometry().y() * self.scaling_factor),
                                          int(self.gridLayoutWidget.geometry().width() * self.scaling_factor), int(self.gridLayoutWidget.geometry().height() * self.scaling_factor)))
                               
        self.gridLayoutWidget_2.setGeometry(QRect(int(self.gridLayoutWidget_2.geometry().x() * self.scaling_factor), int(self.gridLayoutWidget_2.geometry().y() * self.scaling_factor),
                                          int(self.gridLayoutWidget_2.geometry().width() * self.scaling_factor), int(self.gridLayoutWidget_2.geometry().height() * self.scaling_factor)))
                                          
        
        """
        self.pushButtonNew.setGeometry(QRect(int(8*self.scaling_factor), int(235*self.scaling_factor)
                                             , int(60*self.scaling_factor), int(23*self.scaling_factor)))
        self.pushButtonEdit.setGeometry(QRect(int(80*self.scaling_factor), int(235*self.scaling_factor),
                                              int(60*self.scaling_factor), int(23*self.scaling_factor)))
        self.pushButtonRemove.setGeometry(QRect(int(151*self.scaling_factor), int(235*self.scaling_factor),
                                                int(75*self.scaling_factor), int(23*self.scaling_factor)))

        self.listWidgetAlyObj.setGeometry(QRect(int(8*self.scaling_factor), int(28*self.scaling_factor),
                                                int(218*self.scaling_factor), int(191*self.scaling_factor)))

        self.spinBoxDelay.setGeometry(QRect(int(184*self.scaling_factor), int(9000*self.scaling_factor),
                                            int(42*self.scaling_factor), int(22*self.scaling_factor)))
        self.label_2.setGeometry(QRect(int(135*self.scaling_factor), int(9000*self.scaling_factor),
                                       int(37*self.scaling_factor), int(20*self.scaling_factor)))
         
        """         


        #self.setWindowTitle('Application Object Properties')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
        self.connect(self.pushButtonNew, SIGNAL("clicked()"), self.add_item)
        self.connect(self.pushButtonEdit, SIGNAL("clicked()"), self.edit_item)
        self.connect(self.pushButtonRemove, SIGNAL("clicked()"), self.remove_item)
        self.connect(self.pushButtonCancel, SIGNAL("clicked()"), self.cancel_action)
        
        self.connect(self.pushButtonRF, SIGNAL("clicked()"), self.open_rectfinder_view)
        self.connect(self.pushButtonIF, SIGNAL("clicked()"), self.open_imagefinder_view)
        self.connect(self.pushButtonTF, SIGNAL("clicked()"), self.open_textfinder_view)
        self.connect(self.pushButtonOF, SIGNAL("clicked()"), self.open_objectfinder_controller)
        
        self.connect(self.lineEditSearch, SIGNAL("textChanged(QString)"), self, SLOT("search_event(QString)"))
        self.lineEditSearch.installEventFilter(self)
        
        #self.connect(self.pushButtonCC, SIGNAL("clicked()"), self.open_customcode_controller)
        
        #self.listWidgetAlyObj.installEventFilter(self)
        self.tableWidget.keyPressEvent = lambda event: event.ignore()
        self.tableWidget.installEventFilter(self)
        
        self.window = None
        self.full_file_name = None
        self.path = None
        self.robot_file_name = None
        self.action = ""
        self.xml_name = ""
        
        if len(sys.argv) > 1:
            self.full_file_name = sys.argv[1]
            #print self.full_file_name
            
        self.update_path()
        self.update_list()
        
        self.widget_2.hide()
        
        QShortcut(QKeySequence("Ctrl+D"), self, self.doSomething)
        QShortcut(QKeySequence("down"), self, self.goDown)
        QShortcut(QKeySequence("up"), self, self.goUp)
        QShortcut(QKeySequence("return"), self, self.edit_item)
        
        self.old_window_w = None
        self.old_window_h = None 
        self.resizeTimer = QTimer()
        self.connect(self.resizeTimer, SIGNAL("timeout()"), self.resize_done)
        
        
        
    def resizeEvent(self, event):
    
        self.resize_all()
        
    def resize_done(self):
        self.old_window_w = self.frameGeometry().width()
        self.old_window_h = self.frameGeometry().height()
    
    def resize_all(self):

        
        #if resize_factor_h >= 1 and resize_factor_w >= 1:
        self.widget.setGeometry(QRect(self.widget.x(), self.widget.y(),
                                            int(self.frameGeometry().width()), int(self.frameGeometry().height())))
                                            
        self.gridLayoutWidget_2.setGeometry(QRect(self.gridLayoutWidget_2.x(), self.gridLayoutWidget_2.y(),
                                            int(self.frameGeometry().width() - (26*self.scaling_factor)), int(self.frameGeometry().height() - (60*self.scaling_factor))))
                                            
            
        #self.resizeTimer.start(500)
        self.widget_2.setGeometry(QRect(int((self.width()/2) - (self.widget_2.width()/2)), int(10*self.scaling_factor),
                               int(self.widget_2.width()), int(self.widget_2.height())))

    
        """
        window_w = self.frameGeometry().width()
        window_h = self.frameGeometry().height() 
        

        self.listWidgetAlyObj.setGeometry(QRect(int(8*self.scaling_factor), int(28*self.scaling_factor),
                                                int(window_w - (28*self.scaling_factor)), int(window_h - (112*self.scaling_factor))))
                
        list_w = self.listWidgetAlyObj.width() 
        list_h = self.listWidgetAlyObj.height() 
        
        
        self.pushButtonNew.setGeometry(QRect(int(8*self.scaling_factor), int(self.listWidgetAlyObj.y() + self.listWidgetAlyObj.height() + (12 * self.scaling_factor))
                                             , int(60*self.scaling_factor), int(23*self.scaling_factor)))
        self.pushButtonEdit.setGeometry(QRect(int(80*self.scaling_factor), int(self.listWidgetAlyObj.y() + self.listWidgetAlyObj.height() + (12 * self.scaling_factor)),
                                              int(60*self.scaling_factor), int(23*self.scaling_factor)))
        self.pushButtonRemove.setGeometry(QRect(int(151*self.scaling_factor), int(self.listWidgetAlyObj.y() + self.listWidgetAlyObj.height() + (12 * self.scaling_factor)),
                                                int(75*self.scaling_factor), int(23*self.scaling_factor)))

        self.old_window_h = window_h
        """
        
    def doSomething(self):
        self.remove_item()
        
    def goUp(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        selected_index = -1
        for index in sorted(indexes):
            #print('Row %d is selected' % index.row())
            selected_index = index.row()
        
        new_index = selected_index - 1
        if new_index < 0:
            new_index = self.tableWidget.rowCount()-1
        
        self.tableWidget.selectRow(new_index)
    
    def goDown(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        selected_index = -1
        for index in sorted(indexes):
            #print('Row %d is selected' % index.row())
            selected_index = index.row()
        
        new_index = selected_index + 1
        if new_index >  self.tableWidget.rowCount()-1:
            new_index = 0
        
        self.tableWidget.selectRow(new_index)
        
    @pyqtSlot(QString)
    def search_event(self, text):
        if text == "search...":
            self.update_list()
        elif text == "":
            self.update_list()
        else:
            self.update_list(str(text.toUtf8()))
        
    def eventFilter(self, object, event):
        #print event
        #if event.type() == QEvent.KeyPress:

        
        try:
            if event.type() == event.MouseButtonPress:
            
                if self.lineEditSearch.text() == "search..." and object.objectName() == "lineEditSearch":
                    self.lineEditSearch.setText("")
                    return True
                    
            if event.type()== event.FocusOut:
                if self.lineEditSearch.text() == "" and object.objectName() == "lineEditSearch":
                    self.lineEditSearch.setText("search...")
                    return True
                
            if event.matches(QKeySequence.Copy):
            #if Qt.ControlModifier == QApplication.keyboardModifiers() and event.key() == Qt.Key_C: 
                indexes = self.tableWidget.selectionModel().selectedRows()
                last_index = -1
                for index in sorted(indexes):
                    #print('Row %d is selected' % index.row())
                    last_index = index.row()
                    
                text = str(self.tableWidget.item(last_index, 2).data(Qt.EditRole).toString())
                #print selected_item_data

                clipboard = QApplication.clipboard()
                clip_text = clipboard.text()
                
                if clip_text != text:
                    clipboard.setText(text)
                    #print "\"" + text + "\""
        except:
            pass
        return super(AlyvixMainMenuController, self).eventFilter(object, event)
        
            
    def update_path(self):
        lines = self.full_file_name.split(os.sep)
        self.path = ""
        
        cnt = 0
        for line in lines:
        
            if cnt == len(lines) - 1:
                break
            self.path = self.path + line + os.sep
            cnt = cnt + 1
        
        self.robot_file_name = lines[len(lines) - 1]
        self.robot_file_name = self.robot_file_name.split('.')[0]
        self.robot_file_name = self.robot_file_name
        
        self.path = self.path[:-1] + os.sep + "Alyvix" + lines[len(lines) - 1].split('.')[0] + "Objects"
        
        #print "path", self.path
    
    def remove_item(self):
        self.action = "remove"
        
        indexes = self.tableWidget.selectionModel().selectedRows()
        last_index = -1
        for index in sorted(indexes):
            #print('Row %d is selected' % index.row())
            last_index = index.row()
            
        #print "type", self.tableWidget.item(last_index, 0).data(Qt.EditRole).toString()
        #print "name", self.tableWidget.item(last_index, 2).data(Qt.EditRole).toString()
        #print "filename", self.tableWidget.item(last_index, 0).data(Qt.UserRole).toString()
        
        self.xml_name = str(self.tableWidget.item(last_index, 0).data(Qt.UserRole).toString())
        #self.xml_name = selected_text + ".xml"
        if self.xml_name.endswith("_RectFinder.xml"):
            self.alyvix_finder_controller = AlyvixRectFinderView(self)
        elif self.xml_name.endswith("_ImageFinder.xml"):
            self.alyvix_finder_controller = AlyvixImageFinderView(self)
        elif self.xml_name.endswith("_TextFinder.xml"):
            self.alyvix_finder_controller = AlyvixTextFinderView(self)
        elif self.xml_name.endswith("_ObjectFinder.xml"):
            self.alyvix_finder_controller = AlyvixObjectFinderView(self)
        elif self.xml_name.endswith("_CustomCode.xml"):
            self.alyvix_finder_controller = AlyvixCustomCodeView(self)
        
        self.alyvix_finder_controller.remove_code_from_py_file()
        
        
        if self.xml_name.endswith("_ObjectFinder.xml"):
            self._deleted_obj_name = self.alyvix_finder_controller.delete_lock_list()
            
            os.remove(self.path + os.sep + str(self.xml_name).replace("_ObjectFinder.xml","_old_code.txt"))
            
            if (os.path.exists(self.path + os.sep + str(self.xml_name).replace("_ObjectFinder.xml","_ObjectFinder.alyscraper"))):
                os.remove(self.path + os.sep + str(self.xml_name).replace("_ObjectFinder.xml","_ObjectFinder.alyscraper"))
        elif self.xml_name.endswith("_CustomCode.xml"):
            os.remove(self.path + os.sep + str(self.xml_name).replace("_CustomCode.xml","_old_code.txt"))
        else:
            os.remove(self.path + os.sep + str(self.xml_name).replace("xml","png"))
            
        """
        if not self.xml_name.endswith("_ObjectFinder.xml"):
            os.remove(self.path + os.sep + str(self.xml_name).replace("xml","png"))
        else:
            self.alyvix_finder_controller.delete_lock_list()
            os.remove(self.path + os.sep + str(self.xml_name).replace("_ObjectFinder.xml","_old_code.txt"))
        """

        os.remove(self.path + os.sep + str(self.xml_name))
        
        #print "item removed", self.path + os.sep + str(self.xml_name)

        template_path = self.path + os.sep + str(self.xml_name).replace("_ImageFinder.xml","")
        
        ##tttttttttt
        
        if os.path.exists(template_path):
            shutil.rmtree(template_path)
        #self.update_list()
        
        extra_path = get_python_lib() + os.sep + "alyvix" + os.sep + "robotproxy" + os.sep + self.path.split(os.sep)[-1] + "_extra"
        scraper_path = extra_path + os.sep + str(self.xml_name).replace("_TextFinder.xml","")
        
        if os.path.exists(scraper_path):
            shutil.rmtree(scraper_path)
        
        self.tableWidget.removeRow(last_index)
        
        index_main_obj = self.update_list()
        
        if index_main_obj == -1:
            index_main_obj = last_index
        
        self.tableWidget.selectRow(index_main_obj)
        #self.listWidgetAlyObj.setFocus();
        print index_main_obj
    
    def update_list(self, text_to_search=None):
    
    
        cnt = 0
        deleted_index = -1
    
        #self.listWidgetAlyObj.clear()
        self.tableWidget.setRowCount(0)
    
        #dirs = os.listdir(self.full_file_name)
        #dirs = [d for d in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, d))]
        
        # path to the directory (relative or absolute)
        dirpath = self.path

        try:
            # get all entries in the directory w/ stats
            entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
            entries = ((os.stat(path), path) for path in entries)
        except:
            return

        # leave only regular files, insert creation date
        entries = ((stat[ST_MTIME], path)
                   for stat, path in entries if S_ISREG(stat[ST_MODE]))
        #NOTE: on Windows `ST_CTIME` is a creation date 
        #  but on Unix it could be something else
        #NOTE: use `ST_MTIME` to sort by a modification date
        
        if os.path.exists(self.path + os.sep + "lock_list.xml"):
            f = open(self.path + os.sep + "lock_list.xml")
            string = f.read()
            
        #print sorted(entries)

        for cdate, path in sorted(entries):
            filename = os.path.basename(path)
            print cdate
            
            extra_path = get_python_lib() + os.sep + "alyvix" + os.sep + "robotproxy" + os.sep + self.path.split(os.sep)[-1] + "_extra"
            
            #print extra_path + os.sep + filename
            
            if os.path.exists(self.path + os.sep + "lock_list.xml"):
                if "<name>" + filename + "</name>" in string:
                    continue
            #print "fname", filename
            if filename.endswith('.xml') and not filename.endswith('list.xml') and not filename.endswith('data.xml'):
                item_type = QTableWidgetItem()
                item_date = QTableWidgetItem()
                item_name = QTableWidgetItem()
                if filename.endswith('_RectFinder.xml'):
                    item_name.setData(Qt.EditRole, filename[:-15]);#item.setText(filename[:-15] + " [RF]")
                    item_type.setData(Qt.EditRole, "RF")
                elif filename.endswith('_ImageFinder.xml'):
                    item_name.setData(Qt.EditRole, filename[:-16]);#item.setText(filename[:-15] + " [RF]")
                    item_type.setData(Qt.EditRole, "IF")
                elif filename.endswith("_TextFinder.xml"):
                    if os.path.exists(extra_path + os.sep + filename.replace("_TextFinder.xml","") + os.sep + "scraper.txt"):
                        #item.setText(filename[:-15] + " [TS]")
                        item_name.setData(Qt.EditRole, filename[:-15]);#item.setText(filename[:-15] + " [RF]")
                        item_type.setData(Qt.EditRole, "TS")
                    else:
                        item_name.setData(Qt.EditRole, filename[:-15]);#item.setText(filename[:-15] + " [RF]")
                        item_type.setData(Qt.EditRole, "TF")
                elif filename.endswith('_ObjectFinder.xml'):
                    if os.path.exists(path.replace("_ObjectFinder.xml","_ObjectFinder.alyscraper")):
                        item_name.setData(Qt.EditRole, filename[:-17]);#item.setText(filename[:-15] + " [RF]")
                        item_type.setData(Qt.EditRole, "OS")
                    else:
                        item_name.setData(Qt.EditRole, filename[:-17]);#item.setText(filename[:-15] + " [RF]")
                        item_type.setData(Qt.EditRole, "OF")
                        
                    

                if self._deleted_obj_name is not None and (filename[:-15] == self._deleted_obj_name or filename[:-16] == self._deleted_obj_name or filename[:-17] == self._deleted_obj_name):
                    deleted_index = cnt
                    self._deleted_obj_name = None
                date = datetime.datetime.fromtimestamp(cdate)
                #print date.strftime("%Y-%m-%d %H:%M:%S")

                some_date =  QDateTime.fromString (date.strftime("%Y-%m-%d %H:%M:%S"), "yyyy-MM-dd HH:mm:ss")
                #print some_date.toString("yyyy-MM-dd HH:mm:ss")
                #myDTE = QDateTimeEdit()
                #myDTE.setDateTime(some_date)
                item_date.setData(Qt.EditRole, some_date)
                    
                item_type.setData(Qt.UserRole, filename)
                if text_to_search is None:


                    self.tableWidget.insertRow ( self.tableWidget.rowCount() );
                    self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                             0, 
                             item_type)
                    self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                             1, 
                             item_date);
                    self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                             2, 
                             item_name);
                else:

                    name = str(item_name.data(Qt.EditRole).toString()) + " " + date.strftime("%Y-%m-%d %H:%M:%S")
                    
                    if text_to_search in name:
                        self.tableWidget.insertRow ( self.tableWidget.rowCount() );
                        self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                                 0, 
                                 item_type)
                        self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                                 1, 
                                 item_date);
                        self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                                 2, 
                                 item_name);
                        

 
                #item.setData(Qt.UserRole, filename)
                #self.listWidgetAlyObj.addItem(item)
                
                
                #print time.ctime(cdate), os.path.basename(path)
                cnt += 1
                
            header = self.tableWidget.horizontalHeader();
            header.setResizeMode(QHeaderView.ResizeToContents)
            
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers);

    
        """
        files = []
        files += [each for each in os.listdir(self.path) if each.endswith('.xml')]
        
        for file in files:
            item = QListWidgetItem()
            #item.setCheckState(Qt.Checked)
            item.setText(file[:-4])
            self.listWidgetAlyObj.addItem(item)
            
        print self.listWidgetAlyObj.count() 
        """
            
        return deleted_index
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            #print "dummy"
            self.close()
            
    def closeEvent(self, event):
        if self.window is not None:
            self.window.close()
    
    def cancel_action(self):
        self.restore_view()
        
    def restore_view(self):
        self.widget.show()
        self.widget_2.hide()
        self.resize_all()
    
    def add_item(self):
    
        self.action = "new"
        self.lineEditSearch.setText("search...")
        self.widget.hide()
        self.widget_2.show()
        
                               
        self.resize_all()
        
                    
    def edit_item(self):
        self.action = "edit"
    
        if self.tableWidget.currentRow() < 0:
            return
            
        #print self.listWidgetAlyObj.currentRow()
        
        #selected_row = self.listWidgetAlyObj.currentRow()
        #print "row", selected_row
        indexes = self.tableWidget.selectionModel().selectedRows()
        last_index = -1
        for index in sorted(indexes):
            #print('Row %d is selected' % index.row())
            last_index = index.row()
            
        #print "type", self.tableWidget.item(last_index, 0).data(Qt.EditRole).toString()
        #print "name", self.tableWidget.item(last_index, 2).data(Qt.EditRole).toString()
        #print "filename", self.tableWidget.item(last_index, 0).data(Qt.UserRole).toString()
        
        self.xml_name = str(self.tableWidget.item(last_index, 0).data(Qt.UserRole).toString())
        #print selected_item_data
        
        if self.xml_name.endswith("_ObjectFinder.xml"):
            #info_manager = InfoManager()
            self.hide()
            #self.scaling_factor = info_manager.get_info("SCALING FACTOR FLOAT")
            time.sleep(0.600)
            self.alyvix_finder_controller = AlyvixObjectFinderView(self)
            
            self.alyvix_finder_controller.pv = PaintingView(self.alyvix_finder_controller)
            image = QImage(self.alyvix_finder_controller._main_object_finder.xml_path.replace("xml", "png"))   
            self.alyvix_finder_controller.pv.set_bg_pixmap(image)
            self.alyvix_finder_controller.pv.showFullScreen()
            
            self.alyvix_finder_controller.show()
            return
            
        if self.xml_name.endswith("_CustomCode.xml"):
            self.hide()
            time.sleep(0.600)
            self.alyvix_finder_controller = AlyvixCustomCodeView(self)
            self.alyvix_finder_controller.show()
            return
        #info_manager = InfoManager()
        self.hide()
        #self.scaling_factor = info_manager.get_info("SCALING FACTOR FLOAT")
        time.sleep(0.600)
        img_color = cv2.imread(str(self.xml_name).replace("xml","png")) #screen_manager.grab_desktop(screen_manager.get_color_mat)
        #print "imgggg", self.path + os.sep + self.xml_name
        image = QImage(self.path + os.sep + self.xml_name.replace("xml", "png"))
        #print self.path, self.robot_file_name, self.xml_name
        
        if self.xml_name.endswith("_RectFinder.xml"):
            self.alyvix_finder_controller = AlyvixRectFinderView(self)
        elif self.xml_name.endswith("_ImageFinder.xml"):
            self.alyvix_finder_controller = AlyvixImageFinderView(self)
        elif self.xml_name.endswith("_TextFinder.xml"):
            self.alyvix_finder_controller = AlyvixTextFinderView(self)
            
        #self.alyvix_rect_finder_controller.set_path(self.full_file_name)
        self.alyvix_finder_controller.set_bg_pixmap(image)
        self.alyvix_finder_controller.showFullScreen()
        
                
        try:
            if self.alyvix_finder_controller._main_rect_finder is not None:
                self.alyvix_finder_controller.rect_view_properties = AlyvixRectFinderPropertiesView(self.alyvix_finder_controller)
                self.alyvix_finder_controller.rect_view_properties.show()
        except:
            pass
            
        try:
            if self.alyvix_finder_controller._main_text is not None:
                self.alyvix_finder_controller.image_view_properties = AlyvixTextFinderPropertiesView(self.alyvix_finder_controller)
                self.alyvix_finder_controller.image_view_properties.show()
        except:
            pass
            
        try:
            if self.alyvix_finder_controller._main_template is not None:
                self.alyvix_finder_controller.image_view_properties = AlyvixImageFinderPropertiesView(self.alyvix_finder_controller)
                self.alyvix_finder_controller.image_view_properties.show()
        except:
            pass
 
    def add_new_item_on_list(self): 
    
        #self.update_list()

        extra_path = get_python_lib() + os.sep + "alyvix" + os.sep + "robotproxy" + os.sep + self.path.split(os.sep)[-1] + "_extra"
    
        dirpath = self.path

        # get all entries in the directory w/ stats
        entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath) if not fn.endswith(".txt") and not fn.endswith(".png") and not fn.endswith('list.xml') and not fn.endswith('data.xml'))
        
 
        
        #print entries
        
        entries = ((os.stat(path), path) for path in entries)

        # leave only regular files, insert creation date
        entries = ((stat[ST_MTIME], path)
                   for stat, path in entries if S_ISREG(stat[ST_MODE]))
        
        """
        for entry in entries:
            cdate, path = entry
            print path
        """
                   
        #print entries
        #NOTE: on Windows `ST_CTIME` is a creation date 
        #  but on Unix it could be something else
        #NOTE: use `ST_MTIME` to sort by a modification date
        
        list_sorted = sorted(entries)
        #print list_sorted
        cdate, path = list_sorted[-1]

        filename = os.path.basename(path)
        #print filename
        #print cdate
        
        #print extra_path + os.sep + filename
        
        #print filename
        item_type = QTableWidgetItem()
        item_date = QTableWidgetItem()
        item_name = QTableWidgetItem()
        
        #print filename

        if filename.endswith('_RectFinder.xml'):
            item_name.setData(Qt.EditRole, filename[:-15])#item.setText(filename[:-15] + " [RF]")
            item_type.setData(Qt.EditRole, "RF")
        elif filename.endswith('_ImageFinder.xml'):
            item_name.setData(Qt.EditRole, filename[:-16])
            item_type.setData(Qt.EditRole, "IF")
        elif filename.endswith("_TextFinder.xml"):
            if os.path.exists(extra_path + os.sep + filename.replace("_TextFinder.xml","") + os.sep + "scraper.txt"):
                item_name.setData(Qt.EditRole, filename[:-15])
                item_type.setData(Qt.EditRole, "TS")
            else:
                item_name.setData(Qt.EditRole, filename[:-15])
                item_type.setData(Qt.EditRole, "TF")
        elif filename.endswith("_ObjectFinder.xml"):
            if os.path.exists(path.replace("_ObjectFinder.xml","_ObjectFinder.alyscraper")):
                item_name.setData(Qt.EditRole, filename[:-17])
                item_type.setData(Qt.EditRole, "OS")
            else:
                item_name.setData(Qt.EditRole, filename[:-17])
                item_type.setData(Qt.EditRole, "OF")

        date = datetime.datetime.fromtimestamp(cdate)
        #print date.strftime("%Y-%m-%d %H:%M:%S")

        some_date =  QDateTime.fromString (date.strftime("%Y-%m-%d %H:%M:%S"), "yyyy-MM-dd HH:mm:ss")
        
        item_date.setData(Qt.EditRole, some_date)
        
        item_type.setData(Qt.UserRole, filename)
        
        self.tableWidget.insertRow ( self.tableWidget.rowCount() );
        self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                 0, 
                 item_type)
        self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                 1, 
                 item_date);
        self.tableWidget.setItem   ( self.tableWidget.rowCount()-1, 
                 2, 
                 item_name);
        #self.update()
        
    def open_rectfinder_view(self):
        self.xml_name = None
        self.restore_view()
        screen_manager = ScreenManager()
        self.hide()
        self.sleep_before_action()
        time.sleep(0.600)
        img_color = screen_manager.grab_desktop(screen_manager.get_color_mat)
        img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        image = QImage(img_color, img_color.shape[1], img_color.shape[0], img_color.strides[0], QImage.Format_RGB888)
        self.alyvix_rect_finder_controller = AlyvixRectFinderView(self)
        self.alyvix_rect_finder_controller.set_bg_pixmap(image)
        self.alyvix_rect_finder_controller.showFullScreen()
          
        
    def open_imagefinder_view(self):
        self.xml_name = None
        self.restore_view()
        screen_manager = ScreenManager()
        self.hide()
        self.sleep_before_action()
        time.sleep(0.600)
        img_color = screen_manager.grab_desktop(screen_manager.get_color_mat)
        img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        image = QImage(img_color, img_color.shape[1], img_color.shape[0], img_color.strides[0], QImage.Format_RGB888)
        self.alyvix_image_finder_controller = AlyvixImageFinderView(self)
        self.alyvix_image_finder_controller.set_bg_pixmap(image)
        self.alyvix_image_finder_controller.showFullScreen()
        
    def open_textfinder_view(self):
        self.xml_name = None
        self.restore_view()
        screen_manager = ScreenManager()
        self.hide()
        self.sleep_before_action()
        time.sleep(0.600)
        img_color = screen_manager.grab_desktop(screen_manager.get_color_mat)
        img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        image = QImage(img_color, img_color.shape[1], img_color.shape[0], img_color.strides[0], QImage.Format_RGB888)
        self.alyvix_text_finder_controller = AlyvixTextFinderView(self)
        self.alyvix_text_finder_controller.set_bg_pixmap(image)
        self.alyvix_text_finder_controller.showFullScreen()
        
    def open_objectfinder_controller(self):
        self.xml_name = None
        self.restore_view()
        self.hide()
        self.sleep_before_action()
        time.sleep(0.600)
        #img_color = screen_manager.grab_desktop(screen_manager.get_color_mat)
        #img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        #image = QImage(img_color, img_color.shape[1], img_color.shape[0], img_color.strides[0], QImage.Format_RGB888)
        self.alyvix_objectfinder_controller = AlyvixObjectFinderView(self)
        #self.alyvix_objectfinder_controller.set_bg_pixmap(image)
        self.alyvix_objectfinder_controller.show()
        
    def open_customcode_controller(self):
        self.xml_name = None
        self.restore_view()
        #screen_manager = ScreenManager()
        self.hide()
        time.sleep(0.600)
        #img_color = screen_manager.grab_desktop(screen_manager.get_color_mat)
        #img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        #image = QImage(img_color, img_color.shape[1], img_color.shape[0], img_color.strides[0], QImage.Format_RGB888)
        self.alyvix_custom_code_controller = AlyvixCustomCodeView(self)
        #self.alyvix_objectfinder_controller.set_bg_pixmap(image)
        self.alyvix_custom_code_controller.show()
        
    def sleep_before_action(self):
        time.sleep(int(self.spinBoxDelay.value()))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    screen_manager = ScreenManager()
    config_reader = ConfigReader()
    if config_reader.get_bg_res_check() == True:
        if screen_manager.is_resolution_ok() is False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Alyvix Background Service is installed but the screen resolution doesn't match with the config file")
            #msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Error")
            #msg.setDetailedText("The details are as follows:")
            msg.show()
        else:
            window = AlyvixMainMenuController()
            window.show()
    else:
        window = AlyvixMainMenuController()
        window.show()

    sys.exit(app.exec_())