class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        if num == 0:
            return cards
        if len(cards)%2 == 0:
            mid_point = len(cards)//2
            if num%2 ==0:
                return Shuffle.modified_overhand(cards[(mid_point - (num//2)) : mid_point +(num//2)] + cards[0: (mid_point - (num//2))] + cards[mid_point +(num//2) :], num-1)
            else:
                return Shuffle.modified_overhand(cards[(mid_point - ((num+1)//2)) : (mid_point +((num+1)//2)-1)] + cards[0: (mid_point - ((num+1)//2))] + cards[(mid_point +((num+1)//2)-1) :], num-1)
        if len(cards)%2 != 0:
            mid_point = len(cards)//2
            if num%2 !=0:
                return Shuffle.modified_overhand(cards[(mid_point - num//2) : (mid_point + num//2 +1)] + cards[0 : (mid_point - num//2)] + cards[(mid_point + num//2 +1) :], num-1)
            else:
                return Shuffle.modified_overhand(cards[(mid_point - (num//2)) : mid_point + (num//2)] + cards[0: mid_point - (num//2)] + cards[mid_point +(num//2) :], num-1)
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        ...