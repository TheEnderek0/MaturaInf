# Concatenate multiline strings in the same line by Enderek | Kamil

def Concat_byline(*args, infill = " ", line_infill = " ") -> str:
    """
    Concatenates multiline strings by respect to particular lines. This function accepts strings, multiline strings and/or lists of both (but not reccuring lists!).
    Returns one multiline string that has been concatenated by these rules.
    This function will ensure that the indentation of these strings will remain the same as original when contatenated, though you can specify the infill pattern (by default it's just space).
    In case the line amount isn't the same line_infill is used as a pattern for filling in the missing lines (also default is space).
    """
    def MakeInfill(length: int, mode: bool):
        """
        Makes an infill for empty spaces/lines, internal function.
        Mode: 0 for char, 1 for line
        """
        infill_pat = ""

        if not mode:
            infill_pat = infill
        else:
            infill_pat = line_infill
        
        if infill_pat == "":
            raise ValueError("Infill pattern cannot be empty when there's a need of one!")
        
        a = length // len(infill_pat)
        b = length % len(infill_pat)

        return infill_pat * a + infill_pat[:b]

    list_of_lines: list = []

    # Convert arguments to list of lists containing particular lines to concatenate
    for element in args:
        if type(element) == str:
            
            lines = element.splitlines()
            list_of_lines.append(lines)

        elif type(element) == list:

            for sc_element in element:
                lines = sc_element.splitlines()
                list_of_lines.append(lines)
    
    # We have to make sure all of the lines are the same length and there is always the same amount of lines
    for lw in list_of_lines:
        # Every list of lines is taken as separate
        max_len = max([len(x) for x in lw])
        for line_id in range(len(lw)): # We have to iterate over indexes because we want to modify the elements
            line = lw[line_id]

            if len(line) < max_len:
                diff = max_len - len(line)
                lw[line_id] = MakeInfill(diff, False) + lw[line_id] # Fill the remaining spaces before
    
    # Now that we've ensured we have the same amount of chars in lines, we have to ensure we have the same amount of
    max_lines = max([len(x) for x in list_of_lines])
    for lines_id in range(len(list_of_lines)): # We also need to iterate over indexes
        lines = list_of_lines[lines_id]

        if len(lines) < max_lines:
            lin_am = max_lines - len(lines)
            line_len = len(lines[0])
            filler = MakeInfill(line_len, True)
            l_lin = [filler]
            new_lines = l_lin * lin_am
            list_of_lines[lines_id].extend(new_lines)

    # Now we concatenate the lines, feeling empty spaces with
    final: list = [""] * max_lines # List of concatenated lines, for now filled with empty strings
    for lines in list_of_lines:
        for line_id in range(len(lines)):
            final[line_id] += lines[line_id]

    # After this, hopefully "final" contains our concatenated lines, now we just need to insert \n to every string in that list and merge it
    end_str = ""
    for line in final:
        end_str += line + "\n"

    return end_str

        


# Test if everything works

if __name__ == "__main__":
    a = """Test 
Test 
Test 
Test w
"""
    
    b = """1
2
3
4
5
"""
    c = " is succesful"

    result = Concat_byline(a, b, c, infill=" ", line_infill=" ")
    print(result)