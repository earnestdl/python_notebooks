from IPython.core.display import display
from qtpy.QtWidgets import QMainWindow
import os

from __code.ipywe import fileselector
from __code._utilities.folder import get_list_of_folders_with_specified_file_type
from __code._utilities.string import format_html_message
from __code import load_ui

from __code.panoramic_stitching.gui_initialization import GuiInitialization
from __code.panoramic_stitching.load_data import LoadData


class PanoramicStitching:

    def __init__(self, working_dir=''):
        self.working_dir = working_dir
        self.file_extension = ["tiff", "tif"]

    def select_input_folders(self):
        self.list_folder_widget = fileselector.FileSelectorPanel(instruction='select all the folders of images to '
                                                                             'stitch',
                                                                 start_dir=self.working_dir,
                                                                 type='directory',
                                                                 next=self.folder_selected,
                                                                 multiple=True)
        self.list_folder_widget.show()

    def folder_selected(self, folder_selected):
        final_list_folders = get_list_of_folders_with_specified_file_type(list_of_folders_to_check=folder_selected,
                                                                          file_extension=self.file_extension)
        if not final_list_folders:

            str_list_ext = ", ".join(self.file_extension)
            display(format_html_message(pre_message="None of the folder selected contains the file of extension "
                                                    "requested ({}}".format(str_list_ext),
                                        spacer=""))
            return

        final_list_folders.sort()
        nbr_folder = len(final_list_folders)
        display(format_html_message(pre_message="Notebook is about to work with {} folders!".format(nbr_folder),
                                    spacer=""))

        # gui initialization
        o_interface = Interface(working_dir=self.working_dir, list_folders=final_list_folders)
        o_interface.show()
        o_interface.load_data()

class Interface(QMainWindow):

    list_folders = None  # list of folders to work on

    # data_dictionary = {'folder_name1': {'file_name1': LoadData},
    #                                     'file_name2': LoadData,
    #                                     'file_name3': LoadData,
    #                                    },
    #                    'folder_name2': {...},
    #                     ...,
    #                    }
    data_dictionary = None

    horizontal_profile_plot = None
    vertical_profile_plot = None

    def __init__(self, parent=None, working_dir=None, list_folders=None):

        self.list_folders = list_folders

        display(format_html_message(pre_message="Check UI that popped up \
                    (maybe hidden behind this browser!)",
                                    spacer=""))
        super(Interface, self).__init__(parent)
        ui_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                    os.path.join('ui',
                                                 'ui_panoramic_stitching_manual.ui'))
        self.ui = load_ui(ui_full_path, baseinstance=self)
        self.setWindowTitle("Semi-Automatic Panoramic Stitching")

        # gui initialization
        o_init = GuiInitialization(parent=self)
        o_init.statusbar()

        # finish initialization
        o_init.run_all()

    def load_data(self):
        # load data and metadata
        o_load = LoadData(parent=self,
                          list_folders=self.list_folders)
        o_load.run()

    # event handler
    def list_folder_combobox_value_changed(self, new_folder_selected):
        print(new_folder_selected)
