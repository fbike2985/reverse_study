# 枚举手机上的所有进程 & 前台进程
import frida

# 获取设备信息
rdev = frida.get_remote_device()

# 枚举所有的进程
processes = rdev.enumerate_processes()
for process in processes:
    print(process)

# 获取在前台运行的APP
front_app = rdev.get_frontmost_application()
print(front_app)
# Application(identifier="com.iqilu.app137", name="爱安丘", pid=13190, parameters={})