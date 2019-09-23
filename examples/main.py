import os
import sys
import getopt

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    clear()

    ''' COMMAND LINE INPUT HANDLING '''
    A = []
    b = []
    c = []
    p = ''
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hA:b:c:p:", ["A=", "b=", "c=", "p="])
    except getopt.GetoptError:
        print('simplex.py -A <matrix> -b <vector> -c <vector> -p <type>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('simplex.py -A <matrix> -b <vector> -c <vector> -p <obj_func_type>')
            print('A: Matrix that represents coefficients of constraints.')
            print('b: Ax <= b')
            print('c: Coefficients of objective function.')
            print('p: Indicates max or min objective function.')
            sys.exit()
        elif opt in ("-A"):
            A = ast.literal_eval(arg)
        elif opt in ("-b"):
            b = ast.literal_eval(arg)
        elif opt in ("-c"):
            c = ast.literal_eval(arg)
        elif opt in ("-p"):
            p = arg.strip()
    if not A or not b or not c:
        print('Must provide arguments for A, b, c (use -h for more info)')
        sys.exit()
    ''' END OF COMMAND LINE INPUT HANDLING '''

    # Assume maximization problem as default.
    if p not in ('max', 'min'):
        p = 'max'

    SimplexSolver().run_simplex(A, b, c, prob=p, enable_msg=False, latex=True)