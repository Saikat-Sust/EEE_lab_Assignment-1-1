'''
Figure              : 4-24(b)
page                : 168
Name of the book    : digital systems (principles & applications)
Writer              :  1) NEAL S. WIDMER
                       2)GREGORY L. MOSS
                       3)RONALD J. TOCCI
Edition             : 12TH

Submitted by-
Name of Student     : Mehedi Hasan Tareq
Department          : Software Engineering(IICT)-SUST   
Registration No     : 2021831027

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
    d.config(unit=.5)

    #create two input Xnor gate
    d += (X := logic.Xnor())
    d += logic.Line().left(d.unit*2).at(X.in1).dot().label('B', 'left')
    d += logic.Line().left(d.unit*2).at(X.in2).dot().label('C', 'left')
    d += logic.Line().right(d.unit*1).at(X.out).label('$\overline{B⊕C}}$')

    #create three input AND gate anchor with output of Xnor
    d += (Y := logic.And(inputs=3).right().anchor('in1'))
    d += (N:=logic.Line().left(d.unit*1).at(Y.in2))
    d += logic.Line().down(d.unit*1).at(Y.in3)
    d += logic.Line().left(d.unit*5)
    d += logic.Line().down(d.unit*2).dot()

    #create a Nor gate that connect its input to three input AND gate
    d += (Z := logic.Nor().right().anchor('in2'))
    d += logic.Line().left(d.unit*2).at(Z.in2).dot().label('D', 'left')
    d += (M:=logic.Line().left(d.unit*1).at(Z.in1).dot())
    d += logic.Line().left(d.unit*1).at(M.end).dot().dot().label('A', 'left')
    d += logic.Line().up(d.unit*1.5).at(M.end)
    d += logic.Wire('-|').to(N.end) 
    d += logic.Line().right(d.unit*2).at(Y.out).label('AD$\overline{(B⊕C)}}$')

    #create a OR gate that is the output of AND gate and NOR gate
    d += (W := logic.Or().right().anchor('in1'))
    d += logic.Line().left(d.unit*1).at(W.in2)
    d += logic.Wire('|-').to(Z.out).label('$\overline{A+D}=\overline{A}\overline{D}}$')
    d += logic.Line().right().at(W.out).dot().label('Z=AD$\overline{(B⊕C)}+\overline{A}\overline{D}}$','right')


#saving the drawing as a pdf file.
d.draw()
d.save('DS_Figure4-24(b)_Tocci12E.pdf')