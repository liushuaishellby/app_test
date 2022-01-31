import openpyxl


# from common.log_handler import Logger_Handler


# 封装读取表格数据的类
class ExcelHandler:
    def __init__(self, file_path):
        """初始化"""
        self.file_path = file_path
        self.workbook = None

    # 打开文件
    def open_file(self):
        workbook = openpyxl.load_workbook(self.file_path)
        return workbook

    # 获取表格
    def get_sheet(self, name):
        return self.open_file()[name]

    # 读取数据
    def read_data(self, name):

        """每一行数据 存储到字典里"""
        sheet = self.get_sheet(name)
        """获取所有行"""
        rows = list(sheet.rows)
        data_data = []
        headers_title = []
        """获取标题"""
        for title in rows[0]:
            headers_title.append(title.value)
        """添加数据"""
        for row in rows[1:]:
            row_data = {}

            for idx, cell in enumerate(row):
                row_data[headers_title[idx]] = cell.value

            data_data.append(row_data)
        return data_data

    # 关闭文件
    def close(self):
        self.open_file().close()
