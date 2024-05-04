shutil.copy("nano.lja", path.join(root, "bin", "nano.lja"))

try:
    mkdir(path.join(root, "bin/nano"))
except FileExistsError:
    pass
for i in ["init.py", "main.py", "loop.py"]:
    shutil.copy(i, path.join(root, "bin/nano", i))
