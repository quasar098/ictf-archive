import pickle
from io import BytesIO

class SecureUnpicklerFor1337Haxx0rsOnly(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> object:
        if module != '__main__':
            return "1m4o n0p3"

        if any(x in name for x in ['ex', 'ev', 'system', 'break', 'help', 'load', 'npickle']):
            return "t00 d4ng3r0u5"

        return super().find_class(module, name)

if __name__ == '__main__':
    data = bytes.fromhex(input('$ '))
    SecureUnpicklerFor1337Haxx0rsOnly(BytesIO(data)).load()
