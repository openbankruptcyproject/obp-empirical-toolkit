# OBP Empirical Toolkit

Open-source tools and methodology for empirical research on U.S. consumer and
small-business bankruptcy. Built and maintained by the [Open Bankruptcy
Project](https://openbankruptcyproject.org), a 501(c)(3) public charity (EIN 41-5159631).

## What's in here

- `scrapers/` &mdash; sanitized example scrapers for CourtListener and PACER
- `classifiers/` &mdash; case-outcome classification heuristics
- `datasets/` &mdash; versioned snapshot CSVs (CC BY 4.0)
- `methodology/` &mdash; documented approach for each empirical project
- `examples/` &mdash; reproducible analysis notebooks

## Datasets currently published

- `subv_quarterly.csv` &mdash; Quarterly Subchapter V filing volume 2020-2025 (Administrative Office of U.S. Courts, Table F-2A)
- More datasets to be added as projects mature; see [openbankruptcyproject.org](https://openbankruptcyproject.org) for the live research portfolio.

## Citing this work

If you use the toolkit or any published dataset in academic, journalistic,
or advocacy work, please cite as:

```
Open Bankruptcy Project (2026). OBP Empirical Toolkit, v0.1.
501(c)(3) public charity (EIN 41-5159631).
URL: https://github.com/openbankruptcyproject/obp-empirical-toolkit
License: MIT (code) / CC BY 4.0 (datasets)
```

A `CITATION.cff` file is included for tools that consume it directly (Zenodo,
GitHub citation widgets, etc.).

## Related research subdomains

- [523a8.openbankruptcyproject.org](https://523a8.openbankruptcyproject.org/) &mdash; § 523(a)(8) AP filings dataset
- [1328f.openbankruptcyproject.org](https://1328f.openbankruptcyproject.org/) &mdash; § 1328(f) successive-filing research
- [viz.openbankruptcyproject.org](https://viz.openbankruptcyproject.org/) &mdash; visualization portfolio
- [eidl.openbankruptcyproject.org](https://eidl.openbankruptcyproject.org/) &mdash; EIDL discharge research

## Contributing

Contributions welcome. The toolkit is intentionally minimal &mdash; small,
focused utilities that other researchers can adapt rather than a monolithic
framework. Pull requests should:

1. Add documentation to `methodology/` for any new analysis approach
2. Include test data or example outputs
3. Maintain MIT (code) / CC BY 4.0 (data) licensing

For substantive contributions or research collaboration, contact
[research@openbankruptcyproject.org](mailto:research@openbankruptcyproject.org).

## License

- Code: MIT (see `LICENSE`)
- Datasets: Creative Commons Attribution 4.0 International (CC BY 4.0)

## Related projects

- [Free Law Project / CourtListener](https://www.courtlistener.com/) &mdash; the public PACER archive that makes most of this research possible
- [RECAP](https://free.law/recap/) &mdash; browser extension for PACER document liberation
- [Federal Judicial Center IDB](https://www.fjc.gov/research/idb) &mdash; integrated database of federal court cases
