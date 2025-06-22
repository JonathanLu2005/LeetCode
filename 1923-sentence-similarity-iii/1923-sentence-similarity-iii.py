class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # convert both into array
        # need traverse shortest on longest
        # if word in shortest same as start cool, then expect next word to be 2nd or last
        # if last good, expect next be 2nd or 2nd last, so forth, until sentence is done
        # can only put a sentence in middle
        # so shorter sentence first words should be smae as first words of another, and last words too
        # so traverse LHS and keep incrementing, if cant
        # then traverse RHS and keep decrementing
        # index should have a gap and should be cool
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        
        if len(s1) < len(s2):
            traverse = s1
            target = s2
            m = len(s1)
            n = len(s2)
        elif len(s2) < len(s1):
            traverse = s2
            target = s1
            m = len(s2)
            n = len(s1)
        else:
            return (sentence1 == sentence2)
        i = 0
        j = n-1
        while traverse:
            word = traverse[0]

            if word == target[i]:
                traverse.pop(0)
                i += 1
            else:
                word = traverse[-1]

                if word == target[j]:
                    j -= 1
                    traverse.pop(-1)
                else:
                    return False
        return True