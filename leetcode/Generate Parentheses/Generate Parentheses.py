from typing import List


class Solution:
    def __init__(self):
        self.sel = []

    def valid(self, words: str) -> bool:
        stack = []
        for word in words:
            if word == '(':
                stack.append(word)
            elif stack and stack[-1] == '(' and word == ')':
                stack.pop(-1)
            else:
                return False
        else:
            return False if stack else True

    def go(self, str: str, cnt: int) -> None:
        if len(str) == cnt:
            if self.valid(str):
                print(str)
                self.sel.append(str)
            return

        for ele in ['(', ')']:
            self.go(str + ele, cnt)

    def generateParenthesis(self, n: int) -> List[str]:
        self.go('', n * 2)
        return self.sel