# search.py
'''
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
'''
import argparse

parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filenames', metavar='filename', nargs='*')

parser.add_argument('-p', '--pat', metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')

parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')

parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')

parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow', 'fast'}, default='slow',
                    help='search speed')

args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)
# name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
#
# action - 当参数在命令行中出现时使用的动作基本类型。
#
# nargs - 命令行参数应当消耗的数目。
#
# const - 被一些 action 和 nargs 选择所需求的常数。
#
# default - 当参数未在命令行中出现时使用的值。
#
# type - 命令行参数应当被转换成的类型。
#
# choices - 可用的参数的容器。
#
# required - 此命令行选项是否可省略 （仅选项可用）。
#
# help - 一个此选项作用的简单描述。
#
# metavar - 在使用方法消息中使用的参数值示例。
#
# dest - 被添加到 parse_args() 所返回对象上的属性名。
