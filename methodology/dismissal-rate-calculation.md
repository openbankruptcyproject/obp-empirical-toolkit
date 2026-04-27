# Chapter 13 Dismissal Rate &mdash; Methodology

## Source

BAPCPA Table 6, FY2023 (October 1, 2022 - September 30, 2023). Published
annually by the Administrative Office of the U.S. Courts.

## Calculation

For each of the 90 federal bankruptcy districts:

```
dismissal_rate = (cases_dismissed / total_cases_closed) * 100
```

Where:
- `cases_dismissed` = Chapter 13 cases closed via dismissal (any ground)
- `total_cases_closed` = all Chapter 13 cases closed in the period
  (dismissed + discharged + converted + other)

## Notes

- "Closed" means the case reached final disposition in the period, regardless
  of when filed
- Conversions to Chapter 7 are tracked separately and not counted as dismissals
- The denominator excludes cases pending at year-end

## Limitations

- Multi-year cases are counted in their closure year, which can mask filing-year
  trends
- District-level reporting variation: a few districts have idiosyncratic
  conversion-tracking conventions
- "Dismissal" doesn't distinguish between voluntary dismissals (debtor's choice)
  and involuntary dismissals (trustee/creditor motion)

## Visualization

A choropleth of FY2023 dismissal rates by district is published at:
https://viz.openbankruptcyproject.org/dismissal-rate-by-district/

## Citation

Open Bankruptcy Project (2026). Chapter 13 Dismissal Rate by District,
FY2023, v1.0. Source: AOUSC BAPCPA Table 6. License: CC BY 4.0.
