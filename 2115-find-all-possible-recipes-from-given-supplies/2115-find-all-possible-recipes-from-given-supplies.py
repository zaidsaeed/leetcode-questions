class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        suppliesMap = self.createSuppliesMap(supplies)
        recipeIngMap = self.createRecIngMap(recipes, ingredients)
        ans = []
        for recipe in recipes:
            if self.findRecipe(recipe, suppliesMap, recipeIngMap, []):
                ans.append(recipe)
        return ans
    
    def findRecipe(self, recipe, suppliesMap, recipeIngMap, pRecipes):
        if not (recipe in suppliesMap) and not (recipe in recipeIngMap):
            return False
        if recipe in suppliesMap:
            return True
        for ingredient in recipeIngMap[recipe]:
            if not (ingredient in suppliesMap):
                newPRec = pRecipes + [ingredient]
                if ingredient in pRecipes or not self.findRecipe(ingredient, suppliesMap, recipeIngMap, newPRec):
                    return False
        suppliesMap.add(recipe)
        return True
                
            
    def createSuppliesMap(self, supplies):
        suppliesMap = set()
        for supply in supplies:
            suppliesMap.add(supply)
        return suppliesMap
    
    def createRecIngMap(self, recipes, ingredients):
        recIngMap = {}
        for recipe, ingredient in zip(recipes, ingredients):
            recIngMap[recipe] = ingredient
        return recIngMap