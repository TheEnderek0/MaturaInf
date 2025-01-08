"""Manages structures"""
from .printlib import printa

class Row():
    def __init__(self, **kwargs):
        self.data = kwargs

    def as_dict(self):
        return self.data.copy()

class Structure():
    def __init__(self, **kwargs):
        """Create a mysql-like table, pass kwargs to set columns. Variable name is the name of the column
            while the value passed is the default value. None sets the column type to REQUIRED.
        """
        self.columns = kwargs
        self.keyslist = list(self.columns.keys())
        self.rows = []



    def add_row(self, row=Row) -> int:
        rdata = row.as_dict()

        # Clean the structure
        for keyvalpair in rdata.items():
            key = keyvalpair[0]

            if not key in self.keyslist:
                del rdata[key]
                printa(f"Specified cell of key {key} has no applicable column. Omitting...", lvl=1)


        # Merge into us, iter over our keys
        for ukey in self.keyslist:

            if ukey not in rdata.keys(): # Fetch the default value
                if defval := self.columns[ukey] is not None:
                    rdata[ukey] = defval
                else:
                    printa(f"No value specified for column {ukey}! Aborting...")
                    return 1


