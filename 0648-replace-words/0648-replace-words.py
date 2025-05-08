class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # split setnence, go through each word, if prefix exists, then cool, else no bother
        maxPrefix = 0

        for x in dictionary:
            maxPrefix = max(maxPrefix, len(x))
        dictionary = set(dictionary)

        sentence = sentence.split(" ")
        

        for i in range(0, len(sentence)):
            word = sentence[i] 
            word = [x for x in word]
            prefix = ""

            limit = min(maxPrefix, len(word))
            for j in range(0, limit):
                prefix += word[j]
                print(prefix)

                if prefix in dictionary:
                    sentence[i] = prefix
                    break

        return " ".join(sentence)
        
        