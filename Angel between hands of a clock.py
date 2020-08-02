class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourHand=hour*30 + 0.5*minutes
        minuteHand=minutes*6
        ans=abs(hourHand-minuteHand)
        return min(ans,360-ans)
