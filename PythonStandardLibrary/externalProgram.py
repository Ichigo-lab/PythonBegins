import subprocess

completed = subprocess.run(["ls"])

# it will not be available on the termiinal
# text=True to get values in text otherwise it gives it in binary
# completed = subprocess.run(["ls"], capture_output=True,text=True)
# for running python code  They will be different process so they will not share any variable or anything
#completed = subprocess.run(["python", "other.py"],capture_output=True,text=True)

# check=True raises when encounters error

print(type(completed))

print("args", completed.args)
print("returncode", completed.returncode)  # Non-zero value indicates error
print("stderr", completed.stderr)
print("stdout", completed.stdout)
