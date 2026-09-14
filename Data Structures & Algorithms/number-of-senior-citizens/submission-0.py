class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0

        for passengers in details:
            if int(passengers[11:13]) > 60:
                result += 1

        return result