# Contributing

It is highly recommended to follow a similar process as described in the documented [Ansible Development Cycle](https://docs.ansible.com/ansible/devel/community/development_process.html).

## pre-commit

To help ensure high-quality contributions this repository includes a [pre-commit](https://pre-commit.com) configuration which
corrects and tests against common issues that would otherwise cause CI to fail.

### Installation

Follow the [pre-commit-instructions](https://pre-commit.com/#install) provided with pre-commit and run `pre-commit install` under the repository base.

If for any reason you would like to disable the pre-commit hooks run `pre-commit uninstall`.

### Running pre-commit checks

You can trigger it locally with `pre-commit run --all-files` or even to run only for a given file `pre-commit run --files YOUR_FILE`.

## Release Workflow

This project uses [antisbull-changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst) for managing the `CHANGELOG.rst` file.

It is highly recommended that you ensure a changelog fragment exists for each Pull Request (PR) following the process defined in the [changelogs-how-to](https://docs.ansible.com/ansible/devel/community/development_process.html#changelogs-how-to).

When you are ready to perform the release, you should be able to run the `antsibull-changelog release` command to update the `CHANGELOG.rst` file with the contents of all changelog fragments that are not already mentioned.

Ensure that you increment the version tracked in the `galaxy.yml` file before committing the release.
