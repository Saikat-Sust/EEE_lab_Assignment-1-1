
'''
Figure              : 3-38(a)
page                : 108
Name of the book    : digital systems (principles & applications)
Writer              :  1) NEAL S. WIDMER
                       2)GREGORY L. MOSS
                       3)RONALD J. TOCCI
Edition             : 12TH'''


#create logic parse Using Vs Code And jupyter Notebook
from schemdraw.parsing import logicparse
#create OR,AND and NOT gate using logic parse and connect them in 3 input or gate
logicparse('((A or B) or (C and D) or (not C))', outlabel = 'Z',gateH=1)

# Can't find saving method in logic parse and it also doesn't open in python karnel.
