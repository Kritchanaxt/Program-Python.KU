    
#! Exercises Calculate tax

def calculate_tax(income):
    
    def case_10(income):
        return income * 0.10
    
    def case_15(income):
        return 932.50 + 0.15 * (income - 9325)
    
    def case_25(income):
        return 5226.25 + 0.25 * (income - 37950)
    
    def case_28(income):
        return 18713.75 + 0.28 * (income - 91900)
    
    def case_33(income):
        return 46643.75 + 0.33 * (income - 191650)
    
    def case_35(income):
        return 120910.25 + 0.35 * (income - 416700)
    
    def case_396(income):
        return 21505.25 + 0.396 * (income - 418400)
    
    switch = {
        1: case_10,
        2: case_15,
        3: case_25,
        4: case_28,
        5: case_33,
        6: case_35,
        7: case_396
    }

    #? Normal if-Else Structure
    # if income <= 9325:
    #     return switch[1](income)
    # elif income <= 37950:
    #     return switch[2](income)
    # elif income <= 91900:
    #     return switch[3](income)
    # elif income <= 191650:
    #     return switch[4](income)
    # elif income <= 416700:
    #     return switch[5](income)
    # elif income <= 418400:
    #     return switch[6](income)
    # else:
    #     return switch[7](income)
    
    #? Ternary If-Else Struct: "value true" if condition else "value false" 
    return (
        switch[1](income) if income <= 9325 else
        switch[2](income) if income <= 37950 else
        switch[3](income) if income <= 91900 else
        switch[4](income) if income <= 191650 else
        switch[5](income) if income <= 416700 else
        switch[6](income) if income <= 418400 else
        switch[7](income)
    )
    
income = float(input("Enter your taxable income: "))
tax_owed = calculate_tax(income)
print("Tax owed:", tax_owed)
