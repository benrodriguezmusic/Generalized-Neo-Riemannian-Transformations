p_axis_offset = 5
l_axis_offset = -3
r_axis_offset = 2

# here is the pitch-class-set object class
class PitchClassSet:
    def __init__(self, prime_form, orientation, pitch_offset):
        self.prime = prime_form # as a list
        self.orientation = orientation # clockwise is true, counterclockwise is false
        self.offset = pitch_offset #

    def apply_offsets(self):
        result = []
        prime = self.prime
        invert = 1
        if not self.orientation:
            invert = -1
        for element in prime:
            result.append((element * invert + self.offset) % 12)
        return result

    def rhino_man(self, axis):
        result = []
        prime = self.prime
        invert = 1
        if not self.orientation:
            invert = -1
        for element in prime:
            result.append(((element + axis) * -invert + self.offset) % 12)
        return result


#modify the parameters of this triad get different pitch collections!
# pitch_offset will transpose, orientation will invert major/minor, and prime_form does exactly what you think it does
Triad = PitchClassSet(prime_form=[0, 3, 7], orientation=False, pitch_offset=5)

# prints the triad as is
print(f'Original: {Triad.apply_offsets()}')

# prints the transformed triads, choose your preferred axis_offset: r, p, or l
print(f'Transformed: {Triad.rhino_man(p_axis_offset)}')



