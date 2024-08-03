# Use the built-in `platform` module to print out the following info:
import platform
placeholder = "remove me :)"
 
print(f"{platform.platform():>10} {placeholder}",)  # platform.platform()
print(f"{platform.python_compiler():>10} {placeholder}",)  # platform.python_compiler()
print(f"{platform.python_version():>10} {placeholder}",)  # platform.python_version()
print(f"{platform.system():>10} {placeholder}",)  # platform.system()
print(f"{platform.release():>10} {placeholder}",)  # platform.release()
print(f"{platform.processor():>10} {placeholder}",)  # platform.processor()