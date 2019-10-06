class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        classification_dict = {}
        for sub_str in strs:
            sorted_char_list = sorted(sub_str)
            sorted_sub_str = ''.join(sorted_char_list)
            if(sorted_sub_str not in classification_dict):
                classification_dict[sorted_sub_str] = []
                classification_dict[sorted_sub_str].append(sub_str)
            else:
                classification_dict[sorted_sub_str].append(sub_str)
        #print(classification_dict)
        ret = []
        for a in classification_dict:
            ret.append(classification_dict[a])
        #print(ret)
        return ret

if (__name__ == "__main__"):
    A = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    ret = sol.groupAnagrams(A)
    print('ans=',ret)        