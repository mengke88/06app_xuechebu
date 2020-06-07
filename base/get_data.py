"""
读取获取data数据，实现数据代码分离
"""
import os

import yaml


class AnalysisData:

    @classmethod
    def get_yaml_data(cls, name):
        """
        解析文件，获取数据
        :param name:调用是需要传入存放数据的文件路径
        :return:
        """
        yaml_data = []
        with open("./data" + os.sep + name, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            for i in data.values():
                # 因为当登录成功时，是没有toact这个值的，所以我们用这个方法时，会因为少一个值导致失败
                # yaml_data.append(list(i.values()))
                # 所以我们用i.get(key)的方法，取不到时会传一个空值进去
                yaml_data.append((i.get("phone"), i.get("passwd"), i.get("toast"), i.get("exp")))
            print(yaml_data)
            return yaml_data
