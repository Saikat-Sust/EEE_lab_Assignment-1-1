
'''
Figure              : 4-74
page                : 
Name of the book    : digital systems (principles & applications)
Writer              :  1) NEAL S. WIDMER
                       2)GREGORY L. MOSS
                       3)RONALD J. TOCCI
Edition             : 12TH

Submitted by-
Name of Student     : Md Julfikar Ali
Department          : Software Engineering(IICT)-SUST   
Registration No     : 2021831023

Submitted To-
Course teacher      : Dr. Md Rasedujjaman
                       Associate professor
                       Department of Electrical& Electronic Engineering-SUST, Sylhet
            
'''



#create and Import a new drawing object named d with a unit size of 0.5.
from schemdraw import logic
import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    # Create a two input AND gate 1
    d += (X := logic.And().label('BC', 'right'))
    d += (B:=logic.Line().left(d.unit*2).at(X.in1).dot())
    d += logic.Line().down(d.unit*7).at(B.end)
    d += logic.Line().left().at(B.end).label('B', 'left').dot()
    d += logic.Line().left(d.unit*3).at(X.in2).idot().label('c', 'left').dot()
    d += logic.Line().down(d.unit*3).at(X.in2)

    # Create a two input another AND gate 2
    d += (Y := logic.And().right().anchor('in2').label('AC'))
    d += (A:=logic.Line().left().at(Y.in1).dot())
    d += (L:=logic.Line().down(d.unit*3).at(A.end))
    d += logic.Line().right()
    d += (M:=logic.And().anchor('in1').label('AB', 'right'))
    d += logic.Line().left(d.unit*2).at(M.in2)
    d += logic.Line().left(d.unit*2).at(A.end).dot().label('A', 'left')

    # Create a three input another Or gate
    d += (N:=logic.Or(inputs=3).right().at(Y.out))
    d += logic.Wire('|-').at(X.out).to(N.in1)
    d += logic.Wire('|-').at(M.out).to(N.in3)

#saving the drawing as a pdf file.
d.draw()
d.save('DS_Figure4-7_Tocci12E.pdf')