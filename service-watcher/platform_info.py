import os
import platform

def information():
    return f'''
    プラットフォーム    : {platform.platform()}
    実行中のディレクトリ: {os.getcwd()}
    実行中のユーザー    : {os.popen('whoami').read().strip()}
    起動時間            : {os.popen('uptime').read().strip()}
    CPU                 : {[l for l in open('/proc/cpuinfo') if l.startswith('model name')][0]}
    CPUコア数           : {os.cpu_count()}
    プロセス            : {os.popen('ps auxf').read()}
    '''
if __name__ == '__main__':
    import sys
    information()
