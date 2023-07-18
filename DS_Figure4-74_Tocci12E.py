
'''
Figure              : 4-74
page                : 225
Name of the book    : digital systems (principles & applications)
Writer              :  1) NEAL S. WIDMER
                       2)GREGORY L. MOSS
                       3)RONALD J. TOCCI
Edition             : 12TH

Submitted by-
Name of Student     : Md Mahabub Rana Saikat
Department          : Software Engineering(IICT)-SUST   
Registration No     : 2021831029

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


    #Creates a two input Xor Gate with label with it's input A,B
    d += (S := logic.Xor())
    d += logic.Line().left(d.unit*2).at(S.in1).dot().label('A', 'left')
    d += (B := logic.Line().at(S.in2).idot())
    d += logic.Line().left().label('B', 'left').dot()
    d += logic.Line().down(d.unit*3).at(S.in2)
    
    #Creates a two input Xnor Gate with label with it's input C and B(Anchor with it)
    d += (Y := logic.Xnor().right().anchor('in1'))
    d += logic.Line().left().at(Y.in2).idot()
    d += logic.Line().left(d.unit*2).at(Y.in2).dot().label('C', 'left')
    d += logic.Line().right(d.unit*3).at(S.out)

    #Creates a three input Xor Gate name X
    d += (X := logic.And(inputs=3).anchor('in1'))
    d += (Z:=logic.Line().left(d.unit*2).at(X.in2))

    #Connect input and ouput line with wire 
    d += logic.Wire('|-').at(Y.out).to(Z.end)
    d += logic.Line().down(d.unit*2).at(Y.in2)
    d += (M:=logic.Line().right(d.unit*5))
    d += logic.Wire('|-').at(M.end).to(X.in3)   
    d += logic.Line().right().at(X.out).dot().label('X', 'right')


#saving the drawing as a pdf file.
d.draw()
d.save('DS_Figure4-74_Tocci12E.pdf')