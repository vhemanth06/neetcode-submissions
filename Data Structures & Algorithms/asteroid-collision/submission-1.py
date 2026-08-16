class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        s=[]
        for num in asteroids:
            alive=True
            while s and s[-1]>0 and num<0 and alive:
                if s[-1]<abs(num):
                    s.pop()
                elif s[-1]==abs(num):
                    alive=False
                    s.pop()
                else:
                    alive=False
            if alive:
                s.append(num)
        return s