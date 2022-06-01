class Cell:
    'Base class for an organism, also called a cell.'
    
    # General Organism Values

    # Cell Detail Values
    cellcir = 0 # Cell circumference. Higher value = More energy consumption over time, and higher chance of eating.
    cellwll = 0 # Cell wall thickness. Higher value = More energy consumption over time, and higher safety. 

    def __init__(self, idnt, energy, celtyp, circ, wall):
        self.idnt = idnt
        self.energy = energy
        self.celtyp = celtyp
        self.circ = circ
        self.wall = wall
    
    def cellDetails(self, hours_sur):
        tmpstr = str("ID: {0} | Cell Circum: {1} | Cell Wall: {2} | Hours Survived: {3}\n").format(self.idnt, self.circ, self.wall, hours_sur)
        return tmpstr