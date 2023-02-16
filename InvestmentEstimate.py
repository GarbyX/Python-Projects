# A simple code for calculating the future value of an investment.
# Principle Amount (Present Value) = $10000
# Time/Period (nper) = 2 years
# Annual return rate = 8%
# Periodic Payments (pmt) = 0

import numpy_financial as npf
result = npf.fv(rate=0.08, nper=2, pmt=0, pv=10000)
print(result)
