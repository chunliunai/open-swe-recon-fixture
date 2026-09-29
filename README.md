# Open SWE Recon Fixture

A small, deterministic repository used by ReconBench to exercise software
engineering and GitHub workflows.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Known task

`normalize_slug` handles ordinary spaces but does not collapse mixed or repeated
whitespace. The open pull request contains a proposed fix and regression tests.

This repository contains no production credentials or user data.
