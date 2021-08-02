# this func sets the working dir to the one stated in dirwanted variable 

def dirfunc():
    import subprocess,os

    dirwanted='/Users/devan'

    proc=subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]

    currentdir=output.strip().decode("utf-8")

    os.chdir(dirwanted)

#Notes
# print(output)
# print("-------------")
# print(output.strip().decode("utf-8"))
# print("")
# print("\n\n\n\n")
# new = output.strip()
# print(new)
# qnext = new.strip()
# print(qnext.decode("utf-8"))
# changing working dir
# print(os.getcwd())
# print(os.getcwd())    