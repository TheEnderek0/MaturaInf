def LoadFile(path:str) -> list[list[int]]:
    """Loads file, converts to lines of numbers"""

    with open(path, "r") as f:
        l = [x.strip() for x in f.readlines()] # Make sure lines are clear of whitespace chars
        NUMBERS = []
        for line in l:
            nums = [int(x) for x in line.split(" ")] # Split based on whitespace char, map to int
            NUMBERS.append(nums)

        return NUMBERS