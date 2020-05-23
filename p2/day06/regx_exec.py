import re


class find_iterface_info:
    def __init__(self, filename, interface):
        self.filename = filename
        self.interface = interface
        self.target = self._get_target()

    def _get_target(self):
        with open(self.filename, "r") as f:
            content = f.read()
            f.flush()
        return content

    def is_exsit(self, interface_matching_result):
        if self.interface in [elem[:-2] for elem in interface_matching_result]:
            return True
        else:
            return False

    def do_return_info(self):
        pattern = self.interface+r".*^$"
        reg = re.compile(pattern)
        interface_matching_result = reg.findall(self.target)
        print(interface_matching_result)


    def match_interface_info(self):
        pattern = r"^[-/\.\w]+ i"
        reg = re.compile(pattern, flags=re.M)
        interface_matching_result = reg.findall(self.target)
        while not self.is_exsit(interface_matching_result):
            self.interface = input("重新输入")
        else:
            print("yes")
            self.do_return_info()


content = find_iterface_info("exc.txt", "Null0")

content.match_interface_info()
