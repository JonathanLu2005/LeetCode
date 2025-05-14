class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # deck of card, ith card has an int, is unique
        # cards face down in 1 deck (Unrevealed)
        # keep doing until all revealed
        # take top card, reveal, take out of deck
        # if still cards in deck, put next top card at bottom
        # if still unrelvead do step 1 then stop
        # get an ordering that would reveal card in increasing order
        #    
        # 2 3 5 7 11 13 17
        # work backwards?
        # [1 2 3 4 5 6 7]
        # [2 13  3   4   7]

        deck.sort()
        
        n = len(deck)
        result = [0] * n
        indices = deque(range(n))
        
        for card in deck:
            idx = indices.popleft() 
            result[idx] = card       
            if indices:               
                indices.append(indices.popleft()) 
        return result