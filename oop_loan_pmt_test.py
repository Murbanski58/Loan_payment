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

def test_loan_init():
    loan = Loan(100000, .06, 30)
    assert loan.loanAmount == 100000
    assert loan.annualRate == .06
    assert loan.
def getDiscountFactor():
    """
    GIVEN a user enters their loan information
    WHEN calculateDiscountFactor  is called
    THEN the discount factor is  calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateDiscountFactor()
    print("\r")
    print(" -- calculateDiscountFactor method unit test")
    assert loan.getDiscountFactor() == pytest.approx(
        166.79, rel=1e-3
    )  


def getLoanPmt():
    """
    GIVEN a user enters their loan information
    WHEN calculateLoanPmt  is called
    THEN the loan payment is  calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateLoanPmt()
    print("\r")
    print(" -- calculateLoanPmt method unit test")
    assert loan.getLoanPmt() == pytest.approx(
        599.55, rel=1e-3
    )

# Functional Tests

def collectLoanDetails(client):
    """
    GIVEN a user enters their loan details
    WHEN the user clicks the calculate button
    THEN the user's loan amount, number of years, and discount amount is returned
    """
    response = client.post(
        "/", data={"loanAmt": "100000", "lengthOfLoan": "30", "intRate": "0.06"}
    )
    print("\r")
    print(" -- calculate loan functional test")
    assert response.status_code == 200
    assert b"$599.55" in response.data

def main():
    """
    GIVEN a user enters loan details
    WHEN the collectLoanDetails method is called
    THEN the user's monthly payment will be printed
    """

