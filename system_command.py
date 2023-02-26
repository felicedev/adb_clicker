import os
import subprocess


class SystemCommand:
    executables = {"adb": None}

    def get(self, cmd):
        return self.executables[cmd]

    def need_executable(self, cmd):
        return cmd in self.executables.keys()

    def update_executable(self, cmd, path):
        self.executables[cmd] = path

    def execute(self, cmd, args, output=True):
        if self.need_executable(cmd):
            cmd = self.executables[cmd]
        command = f"{cmd} {' '.join(args)}"
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if output:
            for line in p.stdout.readlines():
                print(line)
            retval = p.wait()
            print(retval)
