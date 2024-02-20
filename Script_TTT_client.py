import os


def Run_Script_TTT_client():
    command6 = "python /Users/adityakhurana/Developer/CN_Proj_new/client_TTT.py"

    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command6}\"'")


if __name__ == "__main__":
    Run_Script_TTT_client()
