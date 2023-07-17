def split_string(input_string):
    tokens = input_string.split()
    return tokens

def is_hexadecimal(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def convert_nill_to_hex(s):
    return s if is_hexadecimal(s) else "0x00"

def diff(a, b):
    tokens = [int(a[i], 16) - int(b[i], 16) for i in range(min(len(a), len(b)))]
    return tokens

if __name__ == "__main__":
    # the offset is printed in decimal
    a = "0x56f36330 0xaf 0x5663ecdf 0xf7ca3d20 (nil) 0x56f263d2 0x56644180 (nil) 0x56f36330  0xaf (nil) 0x1 0x56f36330 (nil) 0x566421a9 0xaf (nil)  (nil) (nil) 0xf7b2f90b 0xf7ca1960 0xf7ca3d20 0xf7b26520 0xf7ca3d20 (nil)  (nil) 0x239f9600 0x56f263c3 0x56643efc 0xffa81708 0x5663e94a 0x56644180 0x56f263d2  0xffa81708 0x5663e8fd 0xf7f99000 0x566440e8 0xffa81738 0x5663f896 0xf7ca3d20 0x56643efc  0xffa81738 0x5663f89e 0x1 (nil) 0x566440f0 0x56f264c8 0x56f263d2 0x1a8 0x56f263c3 (nil) 0xf7ae9247 0x56643efc 0xffa81788 0x5663f32c (nil) 0xf7ca3000"
    b = "0x581e2330 0xaf 0x5662ccdf 0xf7c82d20 (nil) 0x581d23d2 0x56632180 (nil) 0x581e2330  0xaf (nil) 0x1 0x581e2330 (nil) 0x566301a9 0xaf (nil)  (nil) (nil) 0xf7b0e90b 0xf7c80960 0xf7c82d20 0xf7b05520 0xf7c82d20 (nil)  (nil) 0x83326900 0x581d23c3 0x56631efc 0xfff8ca88 0x5662c94a 0x56632180 0x581d23d2  0xfff8ca88 0x5662c8fd 0xf7f78000 0x566320e8 0xfff8cab8 0x5662d896 0xf7c82d20 0x56631efc  0xfff8cab8 0x5662d89e 0x1 (nil) 0x566320f0 0x581d24c8 0x581d23d2 0x1a8 0x581d23c3 (nil) 0xf7ac8247 0x56631efc 0xfff8cb08 0x5662d32c (nil) 0xf7c82000"

    chatz_server = [convert_nill_to_hex(token) for token in split_string(a)]
    localhost_server = [convert_nill_to_hex(token) for token in split_string(b)]

    size = min(len(chatz_server), len(localhost_server))
    for i in range(size):
        print(f"Comparing: {chatz_server[i]} and {localhost_server[i]}")
        print(f"Difference: {int(chatz_server[i], 16) - int(localhost_server[i], 16)}")
