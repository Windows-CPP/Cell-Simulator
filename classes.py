from random import randint

class Cell:
    'Base class for an organism, also called a cell.'
    
    def __init__(self, idnt):
        'Modify these variables as desired for simulator'
        self.idnt = idnt
        self.energy = 6
        self.celtyp = randint()
        self.circ = randint()
        self.wall = randint()
    
    def cellDetails(self, hours_sur):
        tmpstr = str("ID: {0} | Cell Circum: {1} | Cell Wall: {2} | Hours Survived: {3}\n").format(self.idnt, self.circ, self.wall, hours_sur)
        return tmpstr

## THIS CLASS IS COMPLETELY SEPERATE FROM THE CELL CLASS, THIS CLASS IS THE MAIN SIMULATOR- IT USES THE CELL CLASS, ESTABLISH CELL BEFOREHAND ##
class CellSim:
    'The simulator calcs for use in main- Should prob make my job easier ig'

    # private vars for use
    cell_id = 0


    def __init__(self, idnt,):
        'Inits variables- Remove comment when done'
    
    def writeLog(self, logFile, cellData):
        'Writes the cell data to the desired log file'

    def simCell(self, cell)