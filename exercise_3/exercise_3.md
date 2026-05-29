# Income Tax Calculator

## Requirements

The client wants a simple income tax calculator that will calculate the tax obligation for an individual, single filer,
based only on income from wages and tips, as reported on a U.S. W-2 form.

## 2020 Tax Rates
<table>
  <thead><th>Rate</th><th>Income for Single Individuals</th></thead>
  <tbody>
    <tr><td>10%</td><td>$9,875</td></tr>
    <tr><td>12%</td><td>$9,876 to $40,125</td></tr>
    <tr><td>22%</td><td>$40,126 to $85,525</td></tr>
    <tr><td>24%</td><td>$85,526 to $163,300</td></tr>
    <tr><td>32%</td><td>$163,301 to $207,350</td></tr>
    <tr><td>35%</td><td>$207,351 to $518,400</td></tr>
    <tr><td>37%</td><td>$518,401 or more</td></tr>
  </tbody>
</table>

## Other Standards
The number standards are as follows:
- Gross income must be entered to the nearest cent.
- The taxable income is expressed as a decimal number.
- The tax due is expressed as an integer.

All text that appears to the user should use correct grammar and spelling.

## Program Design

User Input: gross income
User Input: number of dependents

taxable income = gross income - 12,200 - (2000 * number of dependents)
tax due = amount calculated from tax table

print tax due
