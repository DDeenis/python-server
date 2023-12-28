def throw():
    raise "aaa";

def throw_with_message():
    raise ValueError("ValueError");

def main():
    try:
        throw_with_message()
    except ValueError as err:
        print("Exception message: '%s'" % (err))
    except:
        print("Exception")

if __name__ == "__main__":
    main()