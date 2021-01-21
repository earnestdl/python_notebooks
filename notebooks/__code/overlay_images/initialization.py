from qtpy.QtWidgets import QMainWindow, QVBoxLayout, QProgressBar, QApplication
from qtpy import QtGui
import os
from collections import OrderedDict
import pyqtgraph as pg

from __code._utilities.table_handler import TableHandler


class Initialization:

    def __init__(self, parent=None):
        self.parent = parent

    def dictionaries(self):
        list_high_res_files = self.parent.o_norm_high_res.data['sample']['file_name']
        list_high_res_files_basename = [os.path.basename(_file) for _file in list_high_res_files]
        list_low_res_files = self.parent.o_norm_low_res.data['sample']['file_name']
        list_low_res_files_basename = [os.path.basename(_file) for _file in list_low_res_files]

        dict_offsets = OrderedDict()
        for _index, _filename in enumerate(list_high_res_files_basename):
            dict_offsets[_filename] = {'offset': {'x': 0, 'y': 0},
                                       'low_resolution_filename': list_low_res_files_basename[_index],
                                       }
        self.parent.dict_images_offset = dict_offsets

    def statusbar(self):
        self.parent.eventProgress = QProgressBar(self.parent.ui.statusbar)
        self.parent.eventProgress.setVisible(False)
        self.parent.ui.statusbar.addPermanentWidget(self.parent.eventProgress)

    def widgets(self):
        # list of files table
        list_high_res_files = self.parent.o_norm_high_res.data['sample']['file_name']
        list_low_res_files = self.parent.o_norm_low_res.data['sample']['file_name']

        list_high_res_files_basename = [os.path.basename(_file) for _file in list_high_res_files]
        list_low_res_files_basename = [os.path.basename(_file) for _file in list_low_res_files]

        dict_images_offset = self.parent.dict_images_offset

        o_table = TableHandler(table_ui=self.parent.ui.tableWidget)
        _row = 0
        for _high_res_file, _low_res_file in zip(list_high_res_files_basename, list_low_res_files_basename):
            o_table.insert_empty_row(row=_row)
            o_table.insert_item(row=_row, column=0, value=_high_res_file, editable=False)
            o_table.insert_item(row=_row, column=1, value=_low_res_file, editable=False)
            o_table.insert_item(row=_row, column=2, value=dict_images_offset[_high_res_file]['offset']['x'])
            o_table.insert_item(row=_row, column=3, value=dict_images_offset[_high_res_file]['offset']['y'])
            _row += 1

        o_table.set_column_sizes(column_sizes=[200, 200, 50, 50])

        self.parent.ui.splitter_2.setSizes([200, 500])

    def pyqtgraph(self):
        self.parent.ui.high_resolution_image_view = pg.ImageView(view=pg.PlotItem())
        self.parent.ui.high_resolution_image_view.ui.roiBtn.hide()
        self.parent.ui.high_resolution_image_view.ui.menuBtn.hide()
        image_layout = QVBoxLayout()
        image_layout.addWidget(self.parent.ui.high_resolution_image_view)
        self.parent.ui.high_res_widget.setLayout(image_layout)

        self.parent.ui.low_resolution_image_view = pg.ImageView(view=pg.PlotItem())
        self.parent.ui.low_resolution_image_view.ui.roiBtn.hide()
        self.parent.ui.low_resolution_image_view.ui.menuBtn.hide()
        image_layout = QVBoxLayout()
        image_layout.addWidget(self.parent.ui.low_resolution_image_view)
        self.parent.ui.low_res_widget.setLayout(image_layout)

    def markers(self):
        width = self.parent.markers['width']
        height = self.parent.markers['height']

        red_pen = QtGui.QPen()
        red_pen.setColor(QtGui.QColor(255, 0, 0, 255))
        red_pen.setWidthF(0.05)

        blue_pen = QtGui.QPen()
        blue_pen.setColor(QtGui.QColor(0, 0, 255, 255))
        blue_pen.setWidthF(0.05)

        x = self.parent.markers['high_res']['1']['x']
        y = self.parent.markers['high_res']['1']['y']
        self.parent.markers['high_res']['1']['ui'] = pg.ROI([x, y], [width, height], scaleSnap=True, pen=red_pen)
        self.parent.ui.high_resolution_image_view.addItem(self.parent.markers['high_res']['1']['ui'])
        self.parent.markers['high_res']['1']['ui'].sigRegionChanged.connect(self.parent.markers_changed)

        x = self.parent.markers['high_res']['2']['x']
        y = self.parent.markers['high_res']['2']['y']
        self.parent.markers['high_res']['2']['ui'] = pg.ROI([x, y], [width, height], scaleSnap=True, pen=blue_pen)
        self.parent.ui.high_resolution_image_view.addItem(self.parent.markers['high_res']['2']['ui'])
        self.parent.markers['high_res']['2']['ui'].sigRegionChanged.connect(self.parent.markers_changed)

        x = self.parent.markers['low_res']['1']['x']
        y = self.parent.markers['low_res']['1']['y']
        self.parent.markers['low_res']['1']['ui'] = pg.ROI([x, y], [width, height], scaleSnap=True, pen=red_pen)
        self.parent.ui.low_resolution_image_view.addItem(self.parent.markers['low_res']['1']['ui'])
        self.parent.markers['low_res']['1']['ui'].sigRegionChanged.connect(self.parent.markers_changed)

        x = self.parent.markers['low_res']['2']['x']
        y = self.parent.markers['low_res']['2']['y']
        self.parent.markers['low_res']['2']['ui'] = pg.ROI([x, y], [width, height], scaleSnap=True, pen=blue_pen)
        self.parent.ui.low_resolution_image_view.addItem(self.parent.markers['low_res']['2']['ui'])
        self.parent.markers['low_res']['2']['ui'].sigRegionChanged.connect(self.parent.markers_changed)