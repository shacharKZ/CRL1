import os
from subprocess import Popen, run
import shlex
import time
import multiprocessing

# os.system("""osascript -e 'tell aplication "Terminal" to do script "ls -l"'""")
# os.system(f"gnome-terminal -e ll")
# os.system(f"gnome-terminal -e '\"ll\"'")
# os.system(f"gnome-terminal -e 'bash -c \". install/setup.bash; ros2 launch ./src/crl_executer/crl_executer/gazebo.py; exec bash\"'")
# os.system(f". install/setup.bash; ros2 launch ./src/crl_executer/crl_executer/gazebo.py")
# subprocess.Popen(['gnome-terminal', 'ls'])
# os.system("gnome-terminal -e 'bash -c \"ls; . install/setup.bash; ros2 launch ./src/crl_executer/crl_executer/gazebo.py; sleep 1000000\" '"
#
# run(shlex.split('ls'))

# p1 = Popen("gnome-terminal -e 'bash -c \". install/setup.bash; ros2 launch ./src/crl_executer/crl_executer/gazebo.py\"'", shell=True)
# time.sleep(10)
# p2 = Popen("gnome-terminal -e 'bash -c \". install/setup.bash; ros2 run crl_executer executer\"'", shell=True)
# time.sleep(3)
# p3 = Popen("gnome-terminal -e 'bash -c \". install/setup.bash; ros2 run mock_publisher publisher\"'", shell=True)
# time.sleep(3)


# os.system("gnome-terminal -e 'bash -c \". install/setup.bash; ros2 launch ./src/crl_executer/crl_executer/gazebo.py\" '")
# time.sleep(4)
# os.system("gnome-terminal -e 'bash -c \"ls\"'")
# time.sleep(1000)

def f1():
    # os.system("bash 'ls'")
    # p1 = Popen("gnome-terminal -e 'bash -c \" source ~/.bashrc; . install/setup.bash; ros2 launch ./src/crl_executer/crl_executer/gazebo.py\"'", shell=True)
    os.system("gnome-terminal -e 'bash -c \"ls; bash\" '")

if __name__ == '__main__':
    p = multiprocessing.Process(target=f1)
    p.start()
    time.sleep(1000)
    # p.join()
