class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r, a in enumerate(s):
            chars[a] += 1
            maxf = max(maxf, chars[a])
            while (r - l + 1) - maxf > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res