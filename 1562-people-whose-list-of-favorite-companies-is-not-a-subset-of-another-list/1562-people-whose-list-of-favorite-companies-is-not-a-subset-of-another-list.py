class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(x) for x in favoriteCompanies]

        result = []
        #print(favoriteCompanies)

        for i in range(0, len(favoriteCompanies)):
            current = favoriteCompanies[i]

            add = True

            for j in range(0, len(favoriteCompanies)):
                if i != j:
                    if current.issubset(favoriteCompanies[j]):
                        add = False
            if add:
                result.append(i)
        return result