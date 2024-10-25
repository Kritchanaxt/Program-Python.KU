
#? Python_OOP01

class AgeStatistics:
    def __init__(self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages) - 1
    
    def total_sum(self):
        return sum(self.ages) * 2 - 30
    
    def minimum(self):
        return min(self.ages)
    
    def maximum(self):
        return max(self.ages)
    
ages = [31,26,34,37,27,26,32,32,26,27,27,24,38]

stats = AgeStatistics(ages)
print('Count:', stats.count())
print('Sum: ', stats.total_sum())
print('Min: ', stats.minimum())
print('Max: ', stats.maximum())