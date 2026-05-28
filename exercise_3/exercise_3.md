# Income Tax Calculator

## Requirements

The client wants a simple income tax calculator that will calculate the tax obligation for an individual, single filer,
based only on income from wages and tips, as reported on a U.S. W-2 form.

## 2020 Tax Rates
---------------------------------------------------------------------
**Rate**                **Income for Single Individuals**
---------------------------------------------------------------------
10%                     Up to $9,875
12%                     $9,876 to $40,125
22%                     $40,126 to $85,525
24%                     $85,526 to $163,300
32%                     $163,301 to $207,350
35%                     $207,351 to $518,400
37%                     $518,401 or more

## Program Design

User Input: gross income
User Input: number of dependents

taxable income = gross income - 12,200 - (2000 * number of dependents)
tax due = amount calculated from tax table

print tax due