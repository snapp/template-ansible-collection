# Contributing

This projects follows the process described in the documented [Ansible Development Cycle](https://docs.ansible.com/ansible/devel/community/development_process.html).

This project gains value through integration with various upstream tools. Below is the list of relevant upstream tools. Configuration files and directories will be generated, and users have the discretion to enable these as desired.

## pre-commit

To help ensure high-quality contributions this repository includes a [pre-commit](https://pre-commit.com) configuration which
corrects and tests against common issues that would otherwise cause CI to fail.

### Installation

Follow the [pre-commit-instructions](https://pre-commit.com/#install) provided with pre-commit and run `pre-commit install` under the repository base.

If for any reason you would like to disable the pre-commit hooks run `pre-commit uninstall`.

### Running pre-commit checks

You can trigger it locally with `pre-commit run --all-files` or even to run only for a given file `pre-commit run --files YOUR_FILE`.


Example:

The configuration for `pre-commit` can be found in the `.pre-commit-config.yaml` configuration file at the root of the project.

## ansible-lint

ansible-lint checks playbooks for practices and behavior that could potentially be improved. [ansible-lint](https://github.com/ansible/ansible-lint)

Example:

The configuration of what `ansible-lint` is going to error on can be found in the `.ansible-lint` configuration file at the root of the project.

## Antsibull Changelog Tool

A changelog generator used by ansible-core and Ansible collections. [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog)


## GitHub Actions

GitHub Actions is a CI/CD platform that automates software workflows, enabling you to build, test, and deploy your code right from GitHub. [GitHub Actions](https://github.com/features/actions)

Example:

The configuration directory for `GitHub Actions` is `.github/workflows` at the root of the project.

## Visual Studio Code

Visual Studio Code is a free, open-source code editor developed by Microsoft, offering powerful features such as debugging, syntax highlighting, intelligent code completion, snippets, and code refactoring, available for Windows, Linux, and macOS. [Visual Studio Code](https://code.visualstudio.com/)

Example:

The configuration directory for `Visual Studio Code` is `.vscode` at the root of the project.

## yamllint

yamllint is a tool that checks YAML files for syntax, key uniqueness, and style issues. [yamllint](https://github.com/adrienverge/yamllint)

Example:

The configuration file for `yamllint` is `.yamllint` at the root of the project.
