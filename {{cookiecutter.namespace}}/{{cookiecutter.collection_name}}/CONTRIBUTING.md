# Contributing

It is highly recommended to follow a similar process as described in the documented [Ansible Development Cycle](https://docs.ansible.com/ansible/devel/community/development_process.html).

Our project utilizes a collection of upstream tools to ensure code quality, facilitate continuous integration, and manage other aspects of the development workflow. Contributors have the ability to enable or disable certain tools in this collection as needed for their development process. Below is a list of the upstream tools that can be enabled or disabled within this collection:

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

## Release Workflow
{% if cookiecutter.enable_antsibull_changelog %}
This project uses [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst) for managing the `CHANGELOG.rst` file.

It is highly recommended that you ensure a changelog fragment exists for each Pull Request (PR) following the process defined in the [changelogs-how-to](https://docs.ansible.com/ansible/devel/community/development_process.html#changelogs-how-to).

When you are ready to perform the release, you should be able to run the `antsibull-changelog release` command to update the `CHANGELOG.rst` file with the contents of all changelog fragments that are not already mentioned.

{% endif %}
Ensure that you increment the version tracked in the `galaxy.yml` file before committing the release.
