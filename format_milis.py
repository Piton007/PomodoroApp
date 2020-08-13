import re

SECOND = 1000
MINUTE = SECOND * 60
HOUR = MINUTE * 60



formats = {
    "s":SECOND,
    "m":MINUTE,
    "h":HOUR
}

REGX_PATTERN = r"^([0-9]*)\w$"

def calculateMilis(time):
    match = re.search(REGX_PATTERN,time)
    general_group = match.group(0)
    cant = match.group(1)
    try:
        return  -1 if formats.get(general_group[-1]) is None else int(cant) * formats.get(general_group[-1])  
    except :
        return -1
   


if __name__ == "__main__":

    def time_suffix_is_valid():
        time = "25b"
        result = -1
        assert calculateMilis(time) == result
    def time_suffix_is_invalid():
        time = "25m"
        result = 25*MINUTE
        assert calculateMilis(time) == result
    
    time_suffix_is_valid()
    time_suffix_is_invalid()
    
    