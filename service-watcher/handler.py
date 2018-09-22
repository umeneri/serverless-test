import watcher
import platform_info

def hello(event, context):
    return platform_info.information()
