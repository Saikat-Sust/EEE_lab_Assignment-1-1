'''
Figure              : 3-24
page                : 91
Name of the book    : digital systems (principles & applications)
Writer              :  1) NEAL S. WIDMER
                       2)GREGORY L. MOSS
                       3)RONALD J. TOCCI
Edition             : 12TH

Submitted by-
Name of Student     : Israt Jahan Chadni
Department          : Software Engineering(IICT)-SUST   
Registration No     : 2021831036

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
    
    # Create a two input Nor gate
    d += (Y := logic.Nor())
    d += logic.Line().left(d.unit*2).at(Y.in1).label('1').dot().label('C', 'left')
    d += logic.Line().left(d.unit*2).at(Y.in2).label('0',loc='bottom').dot().label('D', 'left')
    d += logic.Line().right(d.unit*1).at(Y.out).label('$\overline{C+D}$')
    d += logic.Line().right(d.unit*2)

    # Create a two input Nand gate
    d += (X := logic.Nand(inputs=3).anchor('in1'))
    d += logic.Line().left().at(X.in1).label('0').at(X.in1)
    d += logic.Line().left().at(X.in2)

    #Connect input and ouput line with wire 
    d += logic.Line().down()
    d += logic.Line().left().label('1').dot().label('B','left')
    d += logic.Line().down().at(X.in3)
    d += logic.Line().left().label('1')
    d += logic.Line().left().dot().label('A','left')
    d += logic.Line().right(d.unit*2).at(X.out).dot().label('1').label('x=$\overline{AB\overline{(C+D)}}$','right')


#saving the drawing as a pdf file.
d.draw()
d.save('DS_Figure3-24_Tocci12E.pdf')