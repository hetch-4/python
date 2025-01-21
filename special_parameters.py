print("""
    def f(pos1,pos2, /, pos_or_kwd, *, kwd1, kwd2):
         -----------   ------------   -------------
              |             |                |
              |        positional or keyword |
              |                              | - keyword only
              --positinal only
""")

def standard_arg(arg):
    print(arg)
standard_arg(4)
#arg above places no restriction on calling 
# convention and argument may be passed by position or keyword

def pos_only_arg(arg, /):
    print(arg)
pos_only_arg(23)
# / used restricted to only positionl parameters

def kwd_only_arg(*,arg):
    print(arg)
kwd_only_arg(arg = 20)
# " * " used restricts to only keyword arguments

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
combined_example(1,2, kwd_only= 3)
combined_example(1, standard = 2, kwd_only = 3)
# combined_example above combines all 3 calling convention 

