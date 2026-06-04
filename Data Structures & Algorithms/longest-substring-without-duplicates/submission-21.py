class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        running_set = {}
        helper_running = {}
        i, j, run, run_max = 0, 0, 0, 0
        while j < len(s):
            running_set[s[j]] = j
            run = len(running_set)
            j += 1
            if j < len(s) and s[j] in running_set:
                i = running_set[s[j]]
                run = len(running_set)
                run_max = max(run_max, run)
                for k, v in running_set.items():
                    if v > running_set[s[j]]:
                        helper_running[k] = v
                running_set.clear()
                for k, v in helper_running.items():
                    running_set[k] = v
                helper_running.clear()
                running_set[s[j]] = j
                print(running_set)
                run = len(running_set)
                run_max = max(run_max, run)
        run_max = max(run_max, run)
        return run_max

        #maybe try a hash map with position value