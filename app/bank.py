def verification(age , income  , credit_score , employment):
    
    if (type(age) != int or age < 18 or age > 65
        or type(income) not in [float, int] or 5 > income or income > 500
        or type(credit_score) != int or credit_score < 300 or credit_score > 850
        or employment not in ["C", "F"]):
        return "Invalid Input" 
    income = float(income)
    income = round(income, 1)
    if 300 <= credit_score <= 500:
        return "REJECT"
    if income < 15:
        if employment == "F" or 500 < credit_score <= 700:
            return "REJECT"
        if employment == "C" and credit_score > 700:
            return "MANUAL REVIEW"
    else:
        if employment == "F":
            return "MANUAL REVIEW"
        if employment == "C":
            return "APPROVED"
        