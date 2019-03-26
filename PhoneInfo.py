class MemeryInfo():
    def __init__(self):
        self.type = ''
        self.vendor = ''
        self.size = 0
        self.model = ''
        self.sn = ''

    def set_type(self, type):
        self.type = type

    def set_type(self, vendor):
        self.vendor = vendor


    def set_type(self, size):
        self.size = size

    def set_type(self, model):
        self.model = model

    def set_type(self, size):
        self.sn = sn


class PhoneInfo():
    def __init__(self):
        self.systeminfo = ''
        self.msn = ''
        self.imei = ''
        self.memory_info = MemeryInfo()
        self.loader_type = ''
        self.productioni_mode = ''
        self.boot_version = ''
        self.xfl_version = ''
        self.default_status = ''
        self.root_hash_key = ''



