class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        count = 0
        for x in damage:
            if x >= armor:
                count += x - armor
                armor = 0
            else:
                count += x
        if armor== 0:
            return count + 1
        
        count -= max(damage)

        if count < 0:
            return 0
        return count +1

     