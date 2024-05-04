be.based.run("cp nano.lja /bin/nano.lja")

be.based.run("mkdir /bin/nano")
for pv[get_pid()]["filee"] in ["init.py", "main.py", "loop.py"]:
    be.based.run("cp " + vr("filee") + " /bin/nano/" + vr("filee"))

be.api.setvar("return", "0")
