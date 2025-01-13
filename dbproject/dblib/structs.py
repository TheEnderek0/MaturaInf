"""Manages structures"""
from .printlib import printa
from .concat_string import Concat_byline
from io import BufferedReader, BytesIO
from struct import pack, unpack

COL_ALLOWEDCHARS = "qwertyuiopasdfghjklzxcvbnm_-1234567890"

COL_START_END_PATTERN = """+
|
+"""

COL_EXTEND_PATTERN = """|
+"""


SIZE_HELPER = {
    "Q": 8,
    "B": 1,
    "i": 4,
    "?": 1,
    "f": 4,

}

ID_ROW_NAME = "ID"

ALLOWED_TYPES = [str, int, float, bool]
ALLOWED_TYPES_USER_DEFINED = []
TYPES_HANDLE = []

def AddType(_type_: any, serialize_method: str, deserialize_func):
    """Add a type definition to be able to put objects of that type into structures.
    Requires serialize method, passed as a str, it should return a bytearray object.
    Deserialize function given the bytearray object should deserialize it and return the object defined with '_type_' """

    ALLOWED_TYPES_USER_DEFINED.append(_type_)
    TYPES_HANDLE.append(  (_type_, serialize_method, deserialize_func)  )

def DecodePascalString(val: BufferedReader) -> str:
    """Automatically decodes pascal strings, moving the passed buffer and returning the decoded string"""
    try:
        str_len = val.read(SIZE_HELPER["i"])
    except AttributeError: # Means we have a bytes object
        str_len = val[:SIZE_HELPER["i"]]

    str_len = unpack("i", str_len)[0]

    try:
        str_val = val.read(str_len)
    except AttributeError:
        str_val = val[SIZE_HELPER["i"]:] # Read the rest

    str_val = str_val.decode()
    return str_val


def EncodePascalString(val: str) -> bytearray:

    len_ = len(val)
    toret = bytearray(pack("i", len_))

    toret.extend(bytearray(val.encode()))
    return toret

def DeserializeType(val: bytes, str_type: str):
    match str_type:
        case "str":
            return DecodePascalString(val)
        
        case "int":
            return unpack("i", val)[0]
        
        case "float":
            return unpack("f", val)[0]
        
        case "bool":
            return unpack("?", val)[0]
        
        case "NoneType":
            return None
        
        case _:
            pass

    if not str_type in [x.__name__ for x in ALLOWED_TYPES_USER_DEFINED]:
        printa(f"Unknown way of deserializing object called {str_type}! Replacing with 'None'!", 2)
        return "None"
    
    # Else we know how to deserialize it
    for _type_, _, deserialize_func in TYPES_HANDLE:
        if _type_.__name__ == str_type:
            break
    
    return deserialize_func(val)

def SerializeType(val) -> bytearray | None:

    to_return = EncodePascalString(type(val).__name__) # Encode the name of the object
    
    if not type(val) in ALLOWED_TYPES and not type(val) in ALLOWED_TYPES_USER_DEFINED and not val is None:
        printa(f"Attempting to serialize unkown type |{type(val)}|!", 2)
        return None

    match type(val).__name__:
        case "str":
            return to_return + EncodePascalString(val)
        
        case "int":
            return to_return + bytearray(pack("i", val))
        
        case "float":
            return to_return + bytearray(pack("d", val))
        
        case "bool":
            return to_return + bytearray(pack("?", val))
        
        case "NoneType":
            return to_return

        case _:
            pass
    
    # If we're here it means that we have a custom object to pack
    for deftype in TYPES_HANDLE:
        obj_def, serialize_method, deserialize_func = deftype
        if type(val).__name__ == obj_def.__name__:
            break
    
    callable = getattr(val, serialize_method)

    bytes_: bytearray = callable()
    #bytes_.extend(bytearray(pack("Q", len(bytes_)))) # Pack the size | Removed after using the block size value to specify the whole block size
    if type(bytes_).__name__ == bytearray.__name__:
        return to_return + bytes_
    else:
        printa(f"Method |{serialize_method}| of object {val} returned a non bytearray object!", 2)
        return None




class Row():
    def __init__(self, **kwargs):
        self.data = kwargs

    def add_cell(self, column_name, value):
        """Adds or overwrites the value at the cell of column |column_name| with the value of |value|."""
        if column_name in self.data.keys():
            printa(f"Overwriting cell value of column |{column_name}|!")
        
        self.data[column_name] = value
    
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.add_cell(key, value)

    def as_dict(self) -> dict:
        return self.data.copy()

    def __repr__(self) -> str:
        return "<ROW " + str(self.data) + ">"

class Structure():
    def __init__(self, **kwargs):
        """Create a mysql-like table, pass kwargs to set columns. Variable name is the name of the column
            while the value passed is the default value. None sets the column type to REQUIRED.
        """
        self.__init__internal(kwargs)

    def __init__internal(self, kwargs_dict):
        if ID_ROW_NAME in list(kwargs_dict.keys()).copy():
            del kwargs_dict[ID_ROW_NAME]

        t = {ID_ROW_NAME: None}
        t.update(kwargs_dict)
        self.columns = t
        
        #Ensure we only have a max of 255 columns
        if len(self.columns.keys()) > 255:
            printa("Too many columns specified, max is 256. The rest will be deleted.", 1)

        while len(self.columns.keys()) > 255:
            keys = list(self.columns.keys())
            del self.columns[keys[-1]]

        for key in list(self.columns.keys()).copy():
            defval = self.columns[key]
            if type(defval) not in ALLOWED_TYPES and not defval is None:
                printa(f"Type {type(defval)} is unsupported!", 1)
                del self.columns[key]

        self.last_row = 1




        self.keyslist = list(self.columns.keys())
        self.rows = []

    def __getitem__(self, key):
        return self.get_row_by_id(key)

    def get_row_by_id(self, id_: int):
        for row in self.rows:
            if row[ID_ROW_NAME] == id_:
                return row

    def delete_row(self, id_: int):
        for i in range(len(self.rows)):
            row = self.rows[i]
            if row[ID_ROW_NAME] == id_:
                del self.rows[i]
                return True
        
        return False

    def get_free_id(self, start):
        id_ = start
        while self.get_row_by_id(id_):
            id_ += 1
        return id_

    def sort_rows(self, reverse_=False):
        rows_per_id = {} # This will help retrieve back the values later
        ids = []
        for row in self.rows:
            ids.append(row[ID_ROW_NAME])
            rows_per_id[row[ID_ROW_NAME]] = row
        
        ids.sort(reverse=reverse_)

        self.rows = [rows_per_id[x] for x in ids] # Retrieve the values back, sorted

    def add_row(self, row=Row) -> int:
        rdata = row.as_dict()

        if not ID_ROW_NAME in rdata.keys() or type(rdata[ID_ROW_NAME]) != int: # ID row has to be integer, we dissallow any other values
            # We're asking for automatic row id assignment
            self.last_row = self.get_free_id(self.last_row)
            rdata[ID_ROW_NAME] = self.last_row
        else: # This row has a specified ID
            self.delete_row(rdata[ID_ROW_NAME]) # Delete the old one, if exists
            # Don't have to do anything else, it will get added with the ID automatically



        # Clean the structure
        for keyvalpair in list(rdata.items()).copy():
            key = keyvalpair[0]

            if not key in self.keyslist:
                del rdata[key]
                printa(f"Specified cell of key {key} has no applicable column. Omitting...", lvl=1)


        # Merge into us, iter over our keys
        for ukey in self.keyslist:

            if ukey not in rdata.keys(): # Fetch the default value
                if (defval := self.columns[ukey]) is not None:
                    rdata[ukey] = defval
                else:
                    printa(f"No value specified for column |{ukey}|! Aborting...")
                    return 1
        
        # Now, append
        self.rows.append(rdata)
    
    def get_column_cfg(self) -> str:
        return str(self.columns).replace(",", " |")

    def __repr__(self):

        RET_str = COL_START_END_PATTERN
        
        col_widths = []
        # Calculate this column width
        for i in range(len(self.keyslist)):
            widths = [len(self.keyslist[i])]

            for item in self.rows:
                item = item[self.keyslist[i]]
                widths.append(len(str(item)))

            maxlen = max(widths) + 2 # Add two space chars

            col_widths.append(maxlen)

            borderstr = "-" * maxlen
            margin_l = (maxlen - widths[0]) // 2
            margin_r = margin_l

            if not (maxlen - widths[0]) % 2 == 0:
                margin_r += 1
            
            margin_l = " " * margin_l
            margin_r = " " * margin_r

            cell = f"{borderstr}\n{margin_l}{self.keyslist[i]}{margin_r}\n{borderstr}"

            RET_str = Concat_byline(RET_str, cell)
            
            RET_str = Concat_byline(RET_str, COL_START_END_PATTERN)

        RET_str += RET_str.splitlines()[-1] + "\n"

        # Now the items
        for i in range(len(self.rows)):

            row_str = COL_EXTEND_PATTERN

            col_id = -1
            for column in self.keyslist:
                col_id += 1

                item = self.rows[i][column]
                item = str(item)

                item_len = len(item)

                total_width = col_widths[col_id]

                margin_l = 1
                margin_r = total_width - item_len - 1


                cell = " " * margin_l + item + " " * margin_r + "\n" + "-" * total_width

                row_str = Concat_byline(row_str, cell)
                row_str = Concat_byline(row_str, COL_EXTEND_PATTERN)

            
            RET_str += row_str

        return RET_str

    def serialise(self) -> bytearray:
        return self.serialize()

    def serialize(self) -> bytearray:
        barray = bytearray()

        #Column header
        col_id = 0
        col_id_dict = {}
        barray_t = bytearray()
        for column in self.columns.items():
            barray_t_column = bytearray()
            col_id += 1
            column_name = column[0]
            
            col_id_dict[column_name] = col_id

            barray_t_column.extend( bytearray(pack("B", col_id))) # Column id
            barray_t_column.extend(EncodePascalString(column_name)) # # Column name

            defval = column[1]
            barray_t_column.extend(SerializeType(defval)) # Default value

            barray_t.extend(bytearray(pack("Q", len(barray_t_column)))) # Size of column block
            barray_t.extend(barray_t_column) # Column block
        
        col_header_size = len(barray_t)

        barray.extend(bytearray(pack("Q", col_header_size))) # Size of the column blockS
        barray.extend(barray_t) # Column blockS
        

        # Row blocks
        barray_t_2 = bytearray()
        for row in self.rows: 
            # Row
            barray_t = bytearray()
            for col_name, cell_value in row.items():
                # Cell
                barray_t_cell = bytearray()
                col_id = col_id_dict[col_name]

                barray_t_cell.extend(bytearray(pack("B", col_id)))
                barray_t_cell.extend(SerializeType(cell_value))

                barray_t.extend(bytearray(pack("Q", len(barray_t_cell)))) # Cell length
                barray_t.extend(barray_t_cell)
            
            barray_t_2.extend(bytearray(pack("Q", len(barray_t)))) # Row length
            barray_t_2.extend(barray_t)
        
        barray.extend(bytearray(pack("Q", len(barray_t_2)))) # Rows block length
        barray.extend(barray_t_2)



        return barray


    def deserialize(self, file: BufferedReader) -> None:

        column_header_size = file.read(SIZE_HELPER["Q"])
        column_header_size = unpack("Q", column_header_size)[0]

        column_headerS = BytesIO(file.read(column_header_size)) # A helper so we can read the bytes, while not touching the file
        # We're basically restricting ourselves to only read this amount of bytes and no bytes after

        columns_dict = {}
        column_id_to_name = {}
        while True:
            
            column_header_size = column_headerS.read(SIZE_HELPER["Q"])
            if not column_header_size:
                break # EOF

            column_header_size = unpack("Q", column_header_size)[0]

            column_block = BytesIO(column_headerS.read(column_header_size)) # This returns our actual block, starting with char

            # Column block processing
            column_id = column_block.read(SIZE_HELPER["B"])
            column_id = unpack("B", column_id)[0]

            # We expect a pascal string after this, and another one after
            column_name = DecodePascalString(column_block)

            column_id_to_name[column_id] = column_name

            defvalue_type = DecodePascalString(column_block)

            defvalue = DeserializeType(column_block.read(), defvalue_type)

            columns_dict[column_name] = defvalue
        
        self.__init__internal(columns_dict) # We should init here

        # Parse the row block

        row_blockS_size = file.read(SIZE_HELPER["Q"])
        row_blockS_size = unpack("Q", row_blockS_size)[0]

        row_blockS = BytesIO(file.read(row_blockS_size))

        while True:
            row_size = row_blockS.read(SIZE_HELPER["Q"])
            if not row_size:
                break # EOF

            row_size = unpack("Q", row_size)[0]

            row = BytesIO(row_blockS.read(row_size))

            row_obj = Row()
            while True:
                cell_size = row.read(SIZE_HELPER["Q"])
                if not cell_size:
                    break # EOF

                cell_size = unpack("Q", cell_size)[0]

                cell = BytesIO(row.read(cell_size))

                # Cell processing
                colmn_id = cell.read(SIZE_HELPER["B"])
                colmn_id = unpack("B", colmn_id)[0]
                colmn_id = column_id_to_name[colmn_id]

                val_type = DecodePascalString(cell)
                cell_val = DeserializeType(cell.read(), val_type)

                row_obj.add_cell(colmn_id, cell_val)
            
            self.add_row(row_obj)









        

        
        