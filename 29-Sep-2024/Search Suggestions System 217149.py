# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        product = []
        for i in range(len(searchWord)):
            p = []
            for prod in products:
                if prod.startswith(searchWord[:i+1]):
                    p.append(prod)
            p = sorted(p)[:3]
            product.append(p)
        return product