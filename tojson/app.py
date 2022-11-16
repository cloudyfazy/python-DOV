import json
def fileread(filename):
    user = open(filename, "r")
    final_user = user.read()
    convertjson = json.loads(final_user)
    x = {
        "name":"Christ Enoch",
        "email":"enochs@gm.com",
        "age":20,
        "profession":"Walker with God"
    }
    convertjson["Musa115"] = x
    user.close()
    return f"The json format is\n\n {final_user}\n\n and when converted to Python is \n\n{convertjson}."


x = fileread("info.json")
print(x)