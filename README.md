# IT Compliance Action

Home of the Github action that scans your repository for Equinor compliance according to [developer.equinor](https://developer.equinor.com)

## How it works

When you add the action to your workflow, it will scan your repo and create an Issue with the tag `compliance` for each breach of compliance according to the guidelines outlined in [developer.equinor](https://developer.equinor.com)

> [!info]
> This is no substitute for being up to date with the guidelines, but will help you with uncovering the most common misstakes

The issues will contain a link to the correct site, where you can read more about how you can fix the issue

## Usage

Add the following to your workflow
```yaml
on: [push]
jobs: 
  compliance_test:
    runs-on: ubuntu-latest
    name: Compliance test
    permissions:
      issues:   write
      contents: read
    steps:
      - name: Checkout # Makes the source code available to be scanned
        id:   checkout
        uses: actions/checkout@v4 
      - name: Scan repo # Scans the source code and repo for compliance
        id:   scan
        uses: equinor/it-compliance-action@v0.2.1-alpha
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Team

This repo is maintained by the [technology accelerator team](https://github.com/equinor/fos-technology-accelerator/). Here is the link to our [Team API](https://github.com/equinor/fos-technology-accelerator/blob/main/TEAM_API.md)

## Contributing

Write a PR!