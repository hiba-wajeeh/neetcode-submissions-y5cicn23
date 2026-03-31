class Solution:
    
    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string = string+s+"\n"
        
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        result_str = ""

        for c in s:
            if c!="\n":
                result_str=result_str+c
            else:
                res.append(result_str)
                result_str = ""


        return res