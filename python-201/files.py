def create_file():
    fname = "text.txt"
    f = None
    try:
        f = open(fname, mode="w", encoding="utf-8")
        f.write("Test 1")
        f.write("\nNew line")
        f.write("\nАвлфывфдщлстлячлвоф")
    except OSError as err:
        print("File 1 creation error", err)
    else:
        f.flush()
        print("File created:", fname)
    finally:
        if f != None: f.close()

def create_file2():
    fname = "text2.txt"
    try:
        with open(fname, mode="w", encoding="utf-8") as f:
            f.write("Host: localhost\r\n")
            f.write("Connection: close\r\n")
            f.write("Content-Type: text/html")
    except OSError as err:
        print("File 1 creation error", err)

def read_all_text(fname: str) -> str | None:
    try:
        with open(fname, mode="r", encoding="utf-8") as f:
            return f.read()
    except OSError as err:
        print("Read file error", err)

def read_lines(fname: str):
    try:
        with open(fname, mode="r", encoding="utf-8") as f:
            return f.readlines()
    except OSError as err:
        print("Read file error", err)
        
def parse_headers(fname) -> dict:
    header_dict = {}
   
    with open(fname, 'r') as f:
        header_dict = dict(
            filter(
                lambda kv: len(kv) == 2, 
                map(
                    lambda line: tuple(map(str.strip, line.split(':', 1))) if ':' in line else (), 
                    f.readlines()
                )
            )
        )
   
    return header_dict

def parse_headers2(fname) -> dict:
    return {
        k: v for k, v in (map(str.strip, line.split(':')) for line in read_lines(fname) if ':' in line)
    }

def main():
    print(parse_headers2("text2.txt"))
    for k, v in parse_headers2("text2.txt").items():
        print("> %s: %s" % (k, v))

if __name__ == "__main__":
    main()