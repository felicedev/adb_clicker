from config import get_or_create
from system_command import SystemCommand
from adb_commands import AdbCommand

config = get_or_create('config.json')

assert config is not None, "The config.json file doesn't exist, it was created for you. Edit the information requested " \
                         "therein before proceeding."

sys_cmd = SystemCommand()
sys_cmd.update_executable('adb', config['adb'])
#sys_cmd.execute('adb', ['devices'])

adb_cmd = AdbCommand(sys_cmd= sys_cmd)
adb_cmd.screenshot("")

