class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.foodRating = {}
        self.foodCuisine = {}
        self.cuisineRating = {}
        self.expired = set()

        for i in range(n):
            food = foods[i]
            rating = ratings[i] * -1
            cuisine = cuisines[i]

            self.foodRating[food] = rating
            self.foodCuisine[food] = cuisine

            if cuisine not in self.cuisineRating:
                self.cuisineRating[cuisine] = []

            value = (rating, food)
            heapq.heappush(self.cuisineRating[cuisine], value)


    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.foodRating[food]
        oldValue = (oldRating, food)
        self.expired.add(oldValue)
        newRating *= -1

        self.foodRating[food] = newRating
        newValue = (newRating, food)
        if newValue in self.expired:
            self.expired.remove(newValue)

        cuisine = self.foodCuisine[food]
        heapq.heappush(self.cuisineRating[cuisine], newValue)

        

        # food -> key -> able to change rating 
        # need to update the heap too!
        # food -> key -> cuisine
        # cuisine -> heap, with heap select food and change it

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineRating[cuisine]

        while True:
            rating, food = heapq.heappop(heap)

            if (rating, food) in self.expired:
                continue
            else:
                heapq.heappush(heap, (rating,food))
                break


        return food


        # ideally we have cuisine as a key -> we have a self sorting array where we can get the highest rated
        # and find the food and return that
        # cuisine we have heap to self sort whats the highest rated food
        # if menu item is old, we store that somewhere s.t. we check for that anf if wehat we pop is that, we dont consider it lol


# modfying rating of food
# return highest rated food item

# we store the food and its ratiing, and cuisine
# we change rating
# return highest rated for their cuisine, if tie, return the smaller name
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)