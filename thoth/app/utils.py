import sys


class bcolors:
    def __init__(self, color=False):
        self.HEADER = "\033[95m" if color else ""
        self.BLUE = "\033[94m" if color else ""
        self.CYAN = "\033[96m" if color else ""
        self.GREEN = "\033[92m" if color else ""
        self.YELLOW = "\033[93m" if color else ""
        self.RED = "\033[91m" if color else ""
        self.ENDC = "\033[0m" if color else ""
        self.BOLD = "\033[1m" if color else ""
        self.BEIGE = "\033[36m" if color else ""
        self.UNDERLINE = "\033[4m" if color else ""


def globals():
    global color
    color = bcolors()


def str_to_bool(str):
    if str == "True":
        return True
    elif str == "False":
        return False
    else:
        print("Wrong value in str_to_bool")
        sys.exit(1)


# Copy from cairo-lang
# https://github.com/starkware-libs/cairo-lang/blob/167b28bcd940fd25ea3816204fa882a0b0a49603/src/starkware/cairo/lang/tracer/tracer_data.py#L261-L273
def field_element_repr(val: int, prime: int) -> str:
    """Converts a field element (given as int) to a decimal/hex string according to its size.


    Args:
        val (int): The value
        prime (int): The prime

    Returns:
        str: The hex value
    """
    # Shift val to the range (-prime // 2, prime // 2).
    shifted_val = (val + prime // 2) % prime - (prime // 2)
    # If shifted_val is small, use decimal representation.
    if abs(shifted_val) < 2**40:
        return str(shifted_val)
    # Otherwise, use hex representation (allowing a sign if the number is close to prime).
    if abs(shifted_val) < 2**100:
        return hex(shifted_val)
    return hex(val)


def value_to_string(val: int, prime: int) -> str:
    """Check if the imm value is a printable string to add it as a comment

    Args:
        val (int): The value
        prime (int): The prime

    Returns:
        str: The string representation
    """
    repr = field_element_repr(val, prime)
    repr_hex = ""
    # print(f"here {bytearray.fromhex(repr[2:])} end")
    if repr[:2] != "0x":
        try:
            repr_hex = hex(int(repr))
        except Exception:
            return ""
    else:
        return ""
    try:
        repr_str = bytearray.fromhex(repr_hex[2:]).decode("utf-8")
        if not repr_str.isprintable():
            return hex(int(repr))
        return repr_str
    except Exception:
        return repr_hex
