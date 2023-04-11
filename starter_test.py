# test_friend.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from datetime import date
from oop_loan_pmt import *


### unit tests ###
def getDiscountFactor():
    """
    GIVEN a user enters loan information
    WHEN the calculateDiscountFactor is called
    THEN the loan's discount is calculated
    """
    loan = Loan(loanAmount = 100000, numberYears = 30, annualRate = .06)
    loan.calculateDiscountFactor()
    print("\r")  
    print(" -- calculateDiscountFactor unit test")
    assert loan.getDiscountFactor() == pytest.approx(
        166.79, rel = 1e-3
    )  

def LoanPayment():
    """
    GIVEN a user enters their loan details
    WHEN calculateLoanPmt method is called
    THEN the loan payment is calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateLoanPmt()
    print("\r")
    print(" -- calculateLoanPmt method unit test")
    assert loan.getLoanPmt() == pytest.approx(
        599.55, rel=1e-3
    ) 


#Functional Test
def getcalculateLoanPmt():
    """
    GIVEN a user enters loan details
    WHEN user clicks calculate
    THEN the the monthly payment is calculated
    """
    response = client.post(
        "/", data={"loanAmt": "100000", "lengthOfLoan": "30", "intRate": "0.06"}
    )
    print("\r")
    print(" -- calculate loan functional test")
    assert response.status_code == 200
    assert b"$599.55" in response.data