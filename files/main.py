rename_process("nano")
gc.collect()
gc.collect()
be.io.ledset(1)  # we don't want to pretend activity
term.write("Running terminal detection.\nIf you get stuck here, try pressing enter")
vr("sizee", False)
while not vr("sizee"):
    try:
        vr("sizee", term.detect_size(3))
    except KeyboardInterrupt:
        pass
term.write("Detected: " + str(vr("sizee")))
if vr("sizee") != False and (vr("sizee")[0] > 14 and vr("sizee")[1] > 105):
    gc.collect()
    vr("ok", False)
    gc.collect()
    gc.collect()
    be.api.subscript("/bin/nano/init.py")
    if vr("ok"):
        gc.collect()
        gc.collect()
        be.api.subscript("/bin/nano/loop.py")
        term.buf[1] = ""
        term.nwrite(colors.endc)
        term.clear()

        be.api.setvar("return", "0")
    else:
        term.write("Failed to initialize nano!")
else:
    be.based.error(13, "15x106")  # minimum size error
    be.api.setvar("return", "1")
term.hold_stdout = False
term.flush_writes()
