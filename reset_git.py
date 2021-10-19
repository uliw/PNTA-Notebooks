import subprocess

subprocess.run(["git", "pull"])
subprocess.run("git reset --hard HEAD".split())
subprocess.run("git fetch; git reset --hard origin/main".split())
subprocess.run("git clean -qfdx; git fetch; git reset --hard origin/main".split())
