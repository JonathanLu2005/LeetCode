class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(x) for x in favoriteCompanies]

        result = []
        #print(favoriteCompanies)

        for i in range(0, len(favoriteCompanies)):
            current = favoriteCompanies[i]
            count = 0

            for j in range(0, len(favoriteCompanies)):
                if i != j:
                    compare = favoriteCompanies[j]

                    if current - compare != set():
                        count += 1
                    else:
                        break
            if count == len(favoriteCompanies) - 1:
                result.append(i)
        return result