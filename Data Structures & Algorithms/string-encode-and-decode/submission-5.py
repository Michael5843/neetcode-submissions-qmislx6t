class Solution:

    def encode(self, strs: List[str]) -> str:
        return "æ".join(strs) if len(strs) > 0 else "đ"



    def decode(self, s: str) -> List[str]:
        return [s for s in s.split("æ")] if not s == "đ" else []
