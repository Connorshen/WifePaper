from os import path


class BaseFig:
    OUTPUT_DIR = path.join(path.dirname(path.dirname(path.abspath(__file__))), "result")

    def paint(self):
        raise Exception("subclass need override")
