# test_app.py

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
from oop_loan_pmt import *



# Unit Tests
def testLoanDiscountFactor():
    """
    GIVEN a user enters loan information
    WHEN calculateDiscountFactor is called
    THEN the discount factor will be calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateDiscountFactor()
    print("\r")
    print(" -- calculateDiscountFactor method unit test")
    assert loan.getDiscountFactor() == pytest.approx(
        166.79, rel=1e-3
    )

def testLoanPmt():
    """
    GIVEN a user enters loan information
    WHEN calculateLoanPmt is called
    THEN the loan payment will be calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateLoanPmt()
    print("\r")
    print(" -- calculateLoanPmt method unit test")
    assert loan.getLoanPmt() == pytest.approx(
        599.55, rel=1e-3
    ) 


# Functional Tests

def testcollectLoanDetails():
    """
    GIVEN a user enters their loan details
    WHEN the user clicks the calculate button
    THEN the user's loan amount, number of years, and discount amount is returned
    """
    input_values = ["100000", "30", ".06"]
    def mock_input(s):
        return input_values.pop(0)
    print("\r")
    print(" -- collectLoanDetailsfunctional test")
    assert collectLoanDetails() == (100000, 30, .06)

def test_main():
    """
    GIVEN a user enters loan details
    WHEN the collectLoanDetails method is called
    THEN the user's monthly payment will be printed
    """
    loanAmount = 100000
    annualRate = .06
    numberOfPmts = 30 *12
    periodicIntRate = annualRate /12
    discountFactor = (((1.0 + periodicIntRate) ** numberOfPmts) - 1.0) / (periodicIntRate * (1.0 + periodicIntRate) ** numberOfPmts)
    loanPmt = loanAmount / discountFactor

    input_values = [100000, .06, 30, 599.55]
    def mock_input(s):
        return input_values.pop(0)
    print("\r")
    print(" -- main method functional test")

  

