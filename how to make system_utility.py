import argparse
import sys
def cal(args):
    if args.o == 'sum':
        return  args.x + args.y
    elif args.o == 'multi':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'div':
        return args.x / args.y

if'__name__'=='__main__':
    project = argparse.ArgumentParser()
    project.add_argument('--x',type=float,default=1.0,help='you must have skiped a input retry')
    project.add_argument('--y',type=float,default=2.0,help='you must have skiped a input retry')
    project.add_argument('--o',type=str,default='add',help='you must have skiped a input retry')
    args = project.parse_args
    sys.stdout.write(cal(args))