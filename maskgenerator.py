from numeralsystems import system_converter
from pyperclip import copy

def mask_generator(express):
    data = list(express.split())
    bin_string = ""
    for i in data:
        if (i.find("-") > 0):
            from_, to_ = map(int, i.split("-"))
            from_, to_ = min(from_, to_), max(from_, to_)
            if (len(bin_string) < to_):
                bin_string = "0" * (to_ - len(bin_string)) + bin_string
            bin_len = len(bin_string)
            for j in range(from_, to_ + 1):
                bin_string = bin_string[:bin_len - j] + "1" + bin_string[bin_len - j + 1:]
        else:
            tmp = int(i)
            if (len(bin_string) < tmp):
                bin_string = "0" * (tmp - len(bin_string)) + bin_string
            bin_len = len(bin_string)
            bin_string = bin_string[:bin_len - tmp] + "1" + bin_string[bin_len - tmp + 1:]
    return system_converter(2, 16, bin_string)

if __name__ == "__main__":
    result = mask_generator(input())
    print("Mask:", result)
    copy(result)