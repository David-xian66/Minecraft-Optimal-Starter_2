"""
MOS的print
由于文件名和模块一摸一样会报错 所以我加了个下划线
"""
import datetime
class MOS_print_colour:
    '''
        HEADER:偏粉的紫色(?)
        OKBLUE:蓝色
        OKCYAN:青色
        OKGREEN:绿色
        WARNING:黄色
        FAIL:红色
        FAIL_2:加粗的红色
        FAIL_3:有下划线的红色
        ENDC:正常的黑色
        BOLD:加粗的黑色
        UNDERLINE:有下横线的黑色
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    FAIL_2 = '\033[1;91m'
    FAIL_3 = '\033[4;91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def MOS_print(type_,MOS_print_1):
    '''type_{[error,错误]  [info,提示]}'''
    MOS_print = str(MOS_print_1)
    MOS_time = datetime.datetime.now().strftime('%H:%M:%S.%f')
    if type_ == 'error':
        tybe_1 = 'ERROR'
        tybe_2 = MOS_print_colour.FAIL_3 + tybe_1 + MOS_print_colour.ENDC
        MOS_time_2 = MOS_print_colour.FAIL_3 + MOS_time + MOS_print_colour.ENDC
        left = MOS_print_colour.FAIL + '[' + MOS_print_colour.ENDC
        right = MOS_print_colour.FAIL + ']' +MOS_print_colour.ENDC
        print(left + MOS_time_2 + right + left + tybe_2 + right + MOS_print_colour.FAIL_2 + MOS_print + MOS_print_colour.ENDC)
    elif type_ == 'info':
        tybe_1 = 'INFO'
        left = MOS_print_colour.ENDC + '[' + MOS_print_colour.ENDC
        right = MOS_print_colour.ENDC + ']' +MOS_print_colour.ENDC
        tybe_2 = MOS_print_colour.UNDERLINE + tybe_1 + MOS_print_colour.ENDC
        MOS_time_2 = MOS_print_colour.UNDERLINE + MOS_time + MOS_print_colour.ENDC
        print(left + MOS_time_2 + right + left + tybe_2 + right + MOS_print_colour.ENDC + MOS_print + MOS_print_colour.ENDC)
