# Standard
import subprocess
import csv
import webbrowser
import os
import glob
import git
import shutil

import sys

file_dir = os.path.join(os.path.dirname(__file__))
sys.path.append(file_dir)

from PySide6 import QtCore, QtGui, QtWidgets
import ui_BlenderAddonManager as ui


from collections import defaultdict
datapath = defaultdict(dict)
aztoolspath = defaultdict(dict)

datapath["blender"]["addon"] = os.path.expandvars("%USERPROFILE%/GoogleDrive/MyPreferences/Blender/BlenderRoaming/3.4/scripts/addons")
datapath["blender"]["git"] = file_dir + "\\data_git_.csv"
datapath["blender"]["init"] = file_dir + "\\data_init_.csv"
datapath["blender"]["py"] = file_dir + "\\data_py_.csv"
datapath["blender"]["bak"] = file_dir + "\\data_bak_.csv"
datapath["blender"]["enabled"] = file_dir + "\\data_enabled_.csv"


class AZBlenderAddonManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AZBlenderAddonManager, self).__init__(parent)
        self.ui = ui.Ui_BlenderAddonManager()
        self.ui.setupUi(self)

        # Table
        model_git = QtGui.QStandardItemModel()
        model_init = QtGui.QStandardItemModel()
        model_py = QtGui.QStandardItemModel()
        model_bak = QtGui.QStandardItemModel()

        ViewCSVTable(model_git, datapath["blender"]["git"])
        ViewCSVTable(model_init, datapath["blender"]["init"])
        ViewCSVTable(model_py, datapath["blender"]["py"])
        ViewCSVTable(model_bak, datapath["blender"]["bak"])

        self.ui.tableView_git.setModel(model_git)
        self.ui.tableView_git.setColumnWidth(3, 50)
        self.ui.tableView_git.setColumnWidth(4, 50)
        self.ui.tableView_git.setColumnWidth(5, 700)

        self.ui.tableView_init.setModel(model_init)
        self.ui.tableView_init.setColumnWidth(3, 50)
        self.ui.tableView_init.setColumnWidth(4, 50)
        self.ui.tableView_init.setColumnWidth(5, 700)

        self.ui.tableView_py.setModel(model_py)
        self.ui.tableView_py.setColumnWidth(3, 50)
        self.ui.tableView_py.setColumnWidth(4, 50)
        self.ui.tableView_py.setColumnWidth(5, 700)

        self.ui.tableView_bak.setModel(model_bak)
        self.ui.tableView_bak.setColumnWidth(3, 50)
        self.ui.tableView_bak.setColumnWidth(4, 50)
        self.ui.tableView_bak.setColumnWidth(5, 700)

        self.ui.tableView_git.doubleClicked.connect(lambda: getTableValueAndSetEvent(self.ui.tableView_git))
        self.ui.tableView_git.doubleClicked.connect(lambda: getTableValueAndSetEvent(self.ui.tableView_init))
        self.ui.tableView_git.doubleClicked.connect(lambda: getTableValueAndSetEvent(self.ui.tableView_py))
        self.ui.tableView_git.doubleClicked.connect(lambda: getTableValueAndSetEvent(self.ui.tableView_bak))

        # pushButton
        def reloadCSV(self):
            reloadCSVTable(self.ui.tableView_git, model_git, datapath["blender"]["git"])
            reloadCSVTable(self.ui.tableView_init, model_init, datapath["blender"]["init"])
            reloadCSVTable(self.ui.tableView_py, model_py, datapath["blender"]["py"])
            reloadCSVTable(self.ui.tableView_bak, model_py, datapath["blender"]["bak"])

        self.ui.pushButton_pull_gitaddon_selected.clicked.connect(lambda: pullGitAddonsSelected(self.ui.tableView_git))
        self.ui.pushButton_pull_gitaddons.clicked.connect(lambda: pullGitAddons())
        self.ui.pushButton_search_addons.clicked.connect(lambda: [searchAddons(), reloadCSV(self)])
        self.ui.pushButton_move_unused_addons.clicked.connect(lambda: [moveUnusedAddons(), searchAddons(), reloadCSV(self)])


def ViewCSVTable(model, filename):

    enabled_addons = getEnabledAddons()

    with open(filename, "r") as fileInput:
        for i, row in enumerate(csv.reader(fileInput)):
            items = [QtGui.QStandardItem(field.strip()) for field in row]
            model.appendRow(items)

            try:
                addon_name = items[0].text()
                if ".py" in addon_name:
                    addon_name = addon_name.strip(".py")

                if addon_name in enabled_addons:
                    for j in range(7):
                        model.setData(model.index(i, j), QtGui.QBrush(QtGui.QColor("#deffcd")), QtCore.Qt.BackgroundRole)
                else:
                    for j in range(7):
                        model.setData(model.index(i, j), QtGui.QBrush(QtGui.QColor("#ec9093")), QtCore.Qt.BackgroundRole)
            except Exception as e:
                print(e)

def reloadCSVTable(table, model, filename):
    model = QtGui.QStandardItemModel()
    ViewCSVTable(model, filename)
    table.setModel(model)


def getTableValueAndSetEvent(table):
    index = table.selectionModel().currentIndex()
    value = index.sibling(index.row(), index.column()).data()
    print(value)
    if value.startswith("http"):
        webbrowser.open(value)
    elif value.startswith(r"%USERPROFILE%") or value.startswith("C:") or value.startswith("E:"):
        subprocess.Popen(["explorer", os.path.expandvars(value)])


def pullGitAddonsSelected(table):
    index = table.selectionModel().currentIndex()
    value = index.sibling(index.row(), 0).data()
    selected_addon = datapath["blender"]["addon"] + "\\" + value
    pullGitAddons(selected_addon)



def convert_size(size, unit="B"):
    units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB")
    i = units.index(unit.upper())
    size = round(size / 1024 ** i, 2)

    return f"{size} {units[i]}"


def getEnabledAddons():
    enabled_addons = []
    csv_path = datapath["blender"]["enabled"]
    with open(csv_path, "r") as f:
        for row in csv.reader(f):
            enabled_addons.append("".join(row))
    return enabled_addons


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def SearchFile(get_file, filename, dict):
    with open(get_file, 'rb') as file:
        lines = file.readlines()
        s_lines = [line.strip() for line in lines]

        get_file = get_file.replace("/", "\\")
        get_file = get_file.replace("\__init__.py", "")

        if os.path.isfile(get_file):
            filesize = os.path.getsize(get_file)
        else:
            filesize = get_dir_size(get_file)

        dict[filename] = [None, None, None, None, None, None]

        for line in s_lines[0:100]:

            if (b"\"name\":" in line) or (b"\"name\" :" in line) or (b"\'name\':" in line) or (b"\'name\' :" in line):
                line = line.decode('utf-8')
                line = line.replace("=", "")
                line = line.replace("{", "")
                line = line.replace("}", "")
                line = line.replace("\'", "")
                line = line.replace("\"", "")
                line = line.replace(",", "")
                line = line.replace("bl_info", "")
                line = line.replace("name", "")
                line = line.replace(":", "")
                line = line.strip()

                addon_name = line

                dict[filename][0] = addon_name

            elif (b"\"author\":" in line) or (b"\"author\" :" in line) or (b"\'author\':" in line) or (b"\'author\" :" in line):
                line = line.decode('utf-8')
                line = line.replace("=", "")
                line = line.replace("{", "")
                line = line.replace("}", "")
                line = line.replace("\'", "")
                line = line.replace("\"", "")
                line = line.replace(",", "")
                line = line.replace("bl_info", "")
                line = line.replace("author", "")
                line = line.replace(":", "")
                line = line.strip()

                addon_author = line

                dict[filename][1] = addon_author

            elif (b"\"version\":" in line) or (b"\"version\" :" in line) or (b"\'version\':" in line) or (b"\'version\" :" in line):
                line = line.decode('utf-8')
                line = line.replace("=", "")
                line = line.replace("{", "")
                line = line.replace("}", "")
                line = line.replace("\'", "")
                line = line.replace("\"", "")
                # line = line.replace(",", "")
                line = line.replace("bl_info", "")
                line = line.replace("version", "")
                line = line.replace(":", "")
                line = line.strip()

                addon_ver = line

                # バージョン
                dict[filename][2] = addon_ver

            # ファイルサイズ
            dict[filename][3] = convert_size(filesize, "MB")

            # パス
            dict[filename][4] = get_file

    file.close()
    return dict


def ExportFile(path, dict):
    with open(path, "w", newline="", encoding='utf-8') as outfile:
        writerfile = csv.writer(outfile)
        for key, value in sorted(dict.items()):

            try:  # アドオンファイル名
                row1 = key
            except Exception as e:
                print(e)
                row1 = " "

            try:  # アドオン名
                row2 = value[0]
            except Exception as e:
                print(e)
                row2 = " "

            try:  # 作者
                row3 = value[1]
            except Exception as e:
                print(e)
                row3 = " "

            try:  # バージョン
                row4 = value[2][1:][:-2].replace(",", ".")
            except Exception as e:
                print(e)
                row4 = " "

            try:  # ファイルサイズ
                row5 = value[3]
            except Exception as e:
                print(e)
                row5 = " "

            try:  # パス
                row6 = value[4].replace(r"C:\Users\Daichi", r"%USERPROFILE%")
            except Exception as e:
                print(e)
                row6 = " "

            try:  # Gitリンク
                row7 = value[5]
            except Exception as e:
                print(e)
                row7 = " "

            try:
                writerfile.writerow([row1, row2, row3, row4, row5, row6, row7])
            except Exception as e:
                print(e)
                print("ERROR ENCODE " + str(key))

    outfile.close()


def serchAddonsCore(files=glob.glob(datapath["blender"]["addon"] + "/*")):
    git_dict = {}
    init_dict = {}
    py_dict = {}
    for file in files:
        filename = os.path.basename(file)

        if filename == "__bak__":
            pass

        elif os.path.isfile(file):
            get_py = file
            if os.path.exists(get_py):
                SearchFile(get_py, filename, py_dict)
            else:
                print("ERROR py")
                pass

        else:
            get_init = file + "\\__init__.py"
            if os.path.exists(get_init):
                git_file = file + "\\.git"
                if os.path.exists(git_file):
                    # filename = "[Git]" + filename
                    SearchFile(get_init, filename, git_dict)

                    with open(git_file + "\\config", 'r') as file:
                        lines = file.readlines()
                        s_lines = [line.strip() for line in lines]

                        for line in s_lines[0:100]:
                            if ("url = " in line):
                                git_url = line.replace("url = ", "")
                                print(git_url)
                                git_dict[filename][5] = str(git_url)

                else:
                    SearchFile(get_init, filename, init_dict)
            else:
                print("ERROR init " + str(file))
                pass

    return [git_dict, init_dict, py_dict]


def searchAddons():

    addon_dict_list = serchAddonsCore(
        files=glob.glob(datapath["blender"]["addon"] + "/*"))

    git_dict = addon_dict_list[0]
    init_dict = addon_dict_list[1]
    py_dict = addon_dict_list[2]

    ExportFile(datapath["blender"]["git"], git_dict)
    ExportFile(datapath["blender"]["init"], init_dict)
    ExportFile(datapath["blender"]["py"], py_dict)

    # __bak__
    bakAddon_dict_list = serchAddonsCore(files=glob.glob(
        datapath["blender"]["addon"] + "/__bak__/*"))

    bak_dict = bakAddon_dict_list[0] | bakAddon_dict_list[1] | bakAddon_dict_list[2]

    ExportFile(datapath["blender"]["bak"], bak_dict)

    print("FINISHED")

    return


def pullGitAddons(files=glob.glob(datapath["blender"]["addon"] + "/*")):
    if type(files) is str:
        files = [files]
    else:
        pass

    for file in files:
        filename = os.path.basename(file)

        if os.path.isfile(file):
            pass
        else:
            get_init = file + "\\__init__.py"
            # print(get_init)
            if os.path.exists(get_init):
                git_file = file + "\\.git"
                if os.path.exists(git_file):
                    git_addon = git.cmd.Git(file)
                    try:
                        git_addon.pull()
                        print("pull :" + filename)
                    except Exception as e:
                        print(e)
                        print("ERROR :" + filename)
                else:
                    pass
            else:
                pass


def moveUnusedAddons():
    files = glob.glob(datapath["blender"]["addon"] + "/*")
    bakDir = datapath["blender"]["addon"] + "/__bak__"

    if not os.path.exists(bakDir):
        os.mkdir(bakDir)

    enabled_addons = getEnabledAddons()

    for file in files:
        addon_name = os.path.basename(file)

        if addon_name != "__bak__":
            if ".py" in addon_name:
                addon_name = addon_name.strip(".py")

            if addon_name not in enabled_addons:
                shutil.move(file, bakDir + "/" + os.path.basename(file))


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    bam = AZBlenderAddonManager()
    bam.show()
    sys.exit(app.exec_())