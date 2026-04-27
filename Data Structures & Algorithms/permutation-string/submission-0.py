class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # build s1 frequency map
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)

        l = 0

        for r in range(len(s2)):
            # add right char to window
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)

            # shrink window if it's too big
            if r - l + 1 > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

            # check if match
            if window_count == s1_count:
                return True

        return False
