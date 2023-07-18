'''
Figure              : 2-2(b)
page                : 48
Name of the book    : digital systems (principles & applications)
Name of the book    :Digital design  
Writer              : 1) M. Morrris Mano
                      2) Michael D. Ciletti
Edition             : 5TH

Submitted by-
Name of Student     : Antu Kalower
Department          : Software Engineering(IICT)-SUST   
Registration No     : 2021831052

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
     
     # First Create a NOT gate name Y that basically input of an AND gate
     d += (Y:=logic.Not())
     d += logic.Line().left(d.unit*3).at(Y.in1).label('Y', 'left')
     d += logic.Line().right(d.unit*3).at(Y.out)
     d += logic.Line().up()

     # Create a two input AND gate label input with X and Y'
     d += (S := logic.And().right().anchor('in2'))
     d += (X:=logic.Line().left(d.unit*6.5).at(S.in1).dot())
     d += logic.Line().down(d.unit*5)
     d += logic.Line().right(d.unit*2)

     # Create a Not gate of X And Anchor with other AND gate input
     d += logic.Not()
     d += logic.Line().right(d.unit*3)

     # Create a Another AND gate with input label Z and X'
     d += (Z := logic.And().right().anchor('in1'))
     d += logic.Line().left(d.unit*8).at(Z.in2).label('Z', 'left')
     d += logic.Line().left(d.unit*1.3).at(X.end).label('X', 'left')
     d += logic.Line().right(d.unit*6).at(S.out)
     d += logic.Line().down()
     d += logic.Line().right(d.unit*2)
     
     # Create a two input OR gate label with F at output
     d += (M:=logic.Or().anchor('in1'))
     d += (N:=logic.Line().left(d.unit*2).at(M.in2))

     #Connect input and ouput line with wire 
     d += logic.Wire('|-').at(N.end).to(Z.out)
     d += logic.Line().right().at(M.out).label('$F_2$', 'right')


#saving the drawing as a pdf file.
d.draw()
d.save('DD_Figure2-2(b)_Mano5E.pdf')