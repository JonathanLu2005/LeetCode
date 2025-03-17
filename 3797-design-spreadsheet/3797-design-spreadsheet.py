class Spreadsheet:

    def __init__(self, rows: int):
        self.hashmap = {}

        for number in range(65, 91):
            self.hashmap[chr(number)] = [0] * rows

    def setCell(self, cell: str, value: int) -> None:
        column = cell[0]
        row = int(cell[1:]) - 1

        self.hashmap[column][row] = value

    def resetCell(self, cell: str) -> None:
        column = cell[0]
        row = int(cell[1:]) - 1    

        self.hashmap[column][row] = 0   

    def getValue(self, formula: str) -> int:
        formula = formula.replace("=", "")
        formula = formula.split("+")
        
        first = formula[0]
        second = formula[1]

        if first[0].isdigit():
            first = int(first)
        else:
            column = first[0]
            row = int(first[1:]) - 1

            first = self.hashmap[column][row]

        if second[0].isdigit():
            second = int(second)
        else:
            column = second[0]
            row = int(second[1:]) - 1

            second = self.hashmap[column][row]

        return first + second


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)