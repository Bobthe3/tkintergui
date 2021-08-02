# dont really need this file anymore its in main


# this func sets the working dir to the one stated in dirwanted variable 

def dirfunc(x):
    import os
    os.chdir(x)


#  below is to get the path of the file you are in
#  i wasted my time cus i could have done os.path.abspath("filename.")
# import subprocess

# proc=subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE, )
# output=proc.communicate()[0]

# currentdir=output.strip().decode("utf-8")
    
    

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