# Example 14: build and run the C core's test, if a C compiler is installed. Prints SKIPPED otherwise (not a pass).
import os, shutil, subprocess, tempfile
here = os.path.dirname(os.path.abspath(__file__))
core = os.path.join(here, "..", "..", "core_c")
cc = shutil.which("gcc") or shutil.which("cc")
if not cc:
    print("SKIPPED: no gcc or cc found")
else:
    exe = os.path.join(tempfile.gettempdir(), "rc_example_c")
    subprocess.run([cc, "-std=c99", "-O2", "-Wall", "-Wextra", "-Werror", "-o", exe,
                    os.path.join(here, "demo.c"), os.path.join(core, "reading.c"), "-I", core], check=True)
    print(subprocess.run([exe], capture_output=True, text=True, check=True).stdout.rstrip())
