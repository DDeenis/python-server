import json

def main():
    try:
        with open("sample.json", mode="r", encoding="utf-8") as f:
            j = json.load(f)
    except:
        print("JSON load error")
        return
    
    print(type(j), j)
    
    for k in j:
        print(k, j[k])

    j['newitem1'] = "dsasdfsdff"
    j['newitem2'] = "влдыфдывфы"

    print(json.dumps(j))
    print(json.dumps(j, ensure_ascii=False, indent=4))

    key = "arr"
    if key in j:
        print(key, "exists")
    else:
        print(key, "does not exist")

    try:
        with open("sample2.json", "w", encoding="utf-8") as f:
            json.dump(j, f, ensure_ascii=False)
    except:
        print("Write fail")
    else:
        print("Write ok")

if __name__ == "__main__":
    main()