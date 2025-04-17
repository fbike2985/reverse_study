import jpype

jvmPath = jpype.getDefaultJVMPath()
d = 'unidbg-android.jar'  # 对应jar地址
# jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=" + d + "")
jpype.startJVM(jvmPath, "-Dfile.encoding=utf-8", "-Djava.class.path=" + d + "")  # 输出乱码时使用
java = jpype.JClass("com.chezhiying.CheZhiYing")()     # 从com开始找到打包jar的类
signature = java.sign()
print(signature)
jpype.shutdownJVM()     # 关闭JVM（注意，必须在所有子线程结束后再关闭，不用子线程调用加密方法会失败）
