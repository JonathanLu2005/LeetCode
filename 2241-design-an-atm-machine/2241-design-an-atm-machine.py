class ATM:
    def __init__(self):
        self.storage = {}
        self.notes = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(0,5):
            note = self.notes[i]
            amount = banknotesCount[i]
            self.storage[note] = self.storage.get(note,0) + amount

    def withdraw(self, amount: int) -> List[int]:
        notes = self.storage.keys()
        result = [0,0,0,0,0]

        for i in range(4, -1, -1):
            value = self.notes[i]
            current = self.storage.get(value,0)

            if current > 0:
                want = min(amount // value, current)
                result[i] = want
                amount -= (want * value)

        if amount == 0:
            for i in range(0,5):
                take = result[i]
                note = self.notes[i]
                self.storage[note] -= take
            return result
        return [-1]
        
"""
=> 20, 50, 100, 200, 500
ATM => empty

prioritse large bank note
machine will halt if attempt above doesnt work

deposit => increment notes
withdraw => return array of number of notes given, else -1

go through each maximum note, and we try to use as much as possible, if theres more notes than the actual request
amount // note, to get number we want, and we do that for next and next
if ok then we return, else we keep all same and return -1

"""

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)