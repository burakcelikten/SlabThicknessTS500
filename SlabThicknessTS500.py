#Reinforce Concrete Building Minimum Slab Thickness For Turkish Standards TS500

# length unit should be taken in mm

# initial beam dimensions

beam0_b = 300  
beam0_h = 600 

slab_thick = []

# Slab calculations

class Slab :
   
    def __init__(self, L_long, L_short) :
        
        self.L_long = L_long
        
        self.L_short = L_short

    # Ratio of the long side and short side of a rectangular slab

    def m(self) :

        return self.L_long / self.L_short
    
    # Determination of slab working method
    
    def w_dir(self) :

        if Slab.m(self) >= 2 :

            return 'Two Way'
        
        else:

            return 'One Way'
        
    # Circumference of a rectangular slab
        
    def total_circumference(self) :

        return 2 * ( self.L_long + self.L_short )
    
    # Inserting the # of continuous long sides of a rectangle slab
    
    def continuouty_degree_long() :
        
        dofcont_l = int(input("Insert the number of continuous long sides of the slab:"))

        return dofcont_l
    
    # Inserting the # of continuous short sides of a rectangle slab
    
    def continuouty_degree_short() :
        
        dofcont_s = int(input("Insert the number of continuous short sides of the slab:"))

        return dofcont_s
    
    # Continuous circumference of a rectangular slab

    def continuous_circumference(self) :

        return self.L_long * Slab.continuouty_degree_long() + self.L_short * Slab.continuouty_degree_short()
    
    # Thickness limitations of a slab according to TS500

    def min_thickness(self) :

        # Net Span in the direction of the short edge

        L_sn = self.L_short - beam0_b

        # Ratio of continuous circumference and total circumference
            
        a_s = Slab.continuous_circumference(self) / Slab.total_circumference(self)

        if Slab.m(self) <= 2 :

            # Minimum thickness for beam slab flooring which works in two way

            h = max( ( L_sn / ( 15 + ( 20 / Slab.m(self) ) ) * ( 1 - a_s / 4) ), 80 )
            
        
        elif Slab.m(self) > 2 : 
            
            # Minimum thickness for slabs which works in one way console slabs such as balconys

            h = L_sn / 12
            
        slab_thick.append(h)

        return h
        
# Slab 1

D101 = Slab(5100, 4400)

D101_mint = D101.min_thickness()

# Slab 2

D102 = Slab(5900,4400)

D102_mint = D102.min_thickness()

#Global slab thickness

print(max(slab_thick))