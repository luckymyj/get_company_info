from xlwt import Workbook
import os
import yaml

class ExcelWriter:
    def __init__(self, excel_name, sheet_name = "Sheet1"):
        self.sheet_name = sheet_name
        self.excel_name = excel_name
        self.workbook = Workbook(encoding = "utf-8")
        self.sheet = self.workbook.add_sheet(self.sheet_name)
    
    def write_data_by_dict(self, data_dict):
           if os.path.exists(self.excel_name):
                 os.remove(self.excel_name)
           if data_dict != None:
                title_list = list(data_dict.keys())
                for j in range(len(title_list)):
                    self.sheet.write(0, j, title_list[j])
                    for i in range(1, len(data_dict.get(title_list[j]))+1):
                        self.sheet.write (i,j,data_dict.get(title_list[j])[i-1])
                
                self.workbook.save (self.excel_name)

class YamlLoader:
    def __init__(self, yamlrfp):
        if os.path.exists(yamlrfp):
            self.yamlrfp = yamlrfp
        else:
            raise FileNotFoundError

        self._data = None

    def data(self):
        if not self._data == None:
            with open(self.yamlrfp) as yrfp:
                self._data = yaml.load(yrfp)
        return self._data

class YamlSave(object):
    def __init__(self, yamlwfp):
        self.yamlwfp = yamlwfp
    
    def save_data(self, save_data_dict):
        if save_data_dict == None or type(save_data_dict) != dict:
            raise('要保存的数据非字典格式或为空')
        with open(self.yamlwfp, 'a', encoding= "utf-8") as yswfp:
            yaml.dump(save_data_dict, yswfp, default_flow_style=False, encoding = 'utf-8', allow_unicode = True)

if __name__ == '__main__':
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    temp_filepath = os.path.join(BASE_PATH, 'company_info.yaml')
    temp_datadict = {'基础信息': {'营业执照信息': {'统一社会信用代码': '91110105MA019WKH0Y', '企业名称': '九德（北京）艺术品展览有限公司'}}}

    yamlwr = YamlSave(temp_filepath)
    yamlwr.save_data(temp_datadict)
