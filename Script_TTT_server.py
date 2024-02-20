import os


def Run_Script_TTT_server():
    command7 = "python /Users/adityakhurana/Developer/CN_Proj_new/server_TTT.py"

    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command7}\"'")


if __name__ == "__main__":
    Run_Script_TTT_server()
