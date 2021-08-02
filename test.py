import subprocess
proc=subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print("\n\n\n\n")
print(output)
print("-------------")

print(output.strip())
new = output.strip()
print(new)
qnext = new.strip()
print(qnext.decode("utf-8") )
