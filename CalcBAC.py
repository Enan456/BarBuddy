class CalcBAC:
    def CalcBAC(gender, weight, standardDrinks, timeSinceFirstDrink):
        self.assertIsNotNone(gender, 'Violation of gender != ""')
        self.assertIsNotNone(weight, 'Violation of weight != None')
                # Formula taken from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2724514/
                # This formula was the most referenced from private and government entities
                # EBAC = ((0.806 * [Standred Drinks] * 1.2 ) / ([Blood Water Constant] * [Weight]) - ([Metabolism Constant] * [Drinking Period in hours]) * 10
                # 0.806 is constant for blood
                # 1.2 is constant used to convert grams to Swedish standards
                # 10 is constant to convert to percentage
                #
                # [Standred Drink] = drink containing 10g of ethanol
                # [Blood Water Constant] = 0.58 for men | 0.49 for women
                # [Metabolism Constant]  = 0.017
        if(gender == "Male"):
            BODY_WATER = 0.58
        elif(gender == "Female"):
            BODY_WATER = 0.49
        # Declare constnts
        METABOLISM = 0.017
        SWEDISH_FACTOR = 1.2
        WATER_BLOOD = 0.806
        CONVERT_TO_PERCENT = 10
        # run the calculations
        return ((WATER_BLOOD * standardDrinks * SWEDISH_FACTOR ) / (BODY_WATER * weight) - (METABOLISM * timeSinceFirstDrink) * CONVERT_TO_PERCENT)
