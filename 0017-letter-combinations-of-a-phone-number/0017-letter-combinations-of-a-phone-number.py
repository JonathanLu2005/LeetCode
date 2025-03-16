class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitsToChar = {"2":"abc", 
        "3":"def", 
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}

        def backtrack(i, current):
            if len(current) == len(digits):
                res.append(current)
                return

            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, current + c)
        # heres how use index and string, to avoid arrays
        if digits:
            backtrack(0, "")
        return res


        """
        if not digits:
            return []

        res = []
        hashmap = {"2":["a","b","c"], 
        "3":["d","e","f"], 
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}

        digitsArr = [x for x in digits]
        

        def backtrack(collection, digitsArr):
            if len(digitsArr) == 0:
                res.append(("".join(collection.copy())))
                return
            
            val = digitsArr[0]
            digitsArr = digitsArr[1:]
            for x in hashmap[val]:
                collection.append(x)
                backtrack(collection, digitsArr)
                collection.pop(len(collection) - 1)

            return

        backtrack([], digitsArr)
        return res"""