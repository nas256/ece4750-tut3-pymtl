#=========================================================================
# MinMaxUnit
#=========================================================================
# This module takes two inputs, compares them, and outputs the larger
# via the "max" output port and the smaller via the "min" output port.

from pymtl import *

class MinMaxUnit( Model ):

  # Constructor

  def __init__( s, nbits=8 ):

    s.in0     = InPort  ( nbits )
    s.in1     = InPort  ( nbits )
    s.out_min = OutPort ( nbits )
    s.out_max = OutPort ( nbits )
    
    @s.combinational
    def comb():
      if (s.in0.value > s.in1.value):
        s.out_min.value = s.in1.value
        s.out_max.value = s.in0.value
      else:
        s.out_min.value = s.in0.value
        s.out_max.value = s.in1.value

