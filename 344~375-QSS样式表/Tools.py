'''
QSS 加载工具类
'''


class Tools:
    @staticmethod
    def set_qss_to_obj(file_path, obj):
        '''读取指定 qss 文件内容, 设置到指定对象中'''
        with open(file_path, 'r') as f:
            obj.setStyleSheet(f.read())
