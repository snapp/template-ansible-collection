# Ⓐ Ansible Collection: {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }}

{%- if cookiecutter.license != 'none' -%}
[![GitHub License](https://img.shields.io/github/license/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }})](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/blob/main/LICENSE)
{%- endif -%}
[![Ansible Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Ansible-silver.svg)](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

[![ansible-lint](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/actions/workflows/ansible-lint.yml)
[![ansible-test](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/actions/workflows/ansible-test.yml/badge.svg)](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/actions/workflows/ansible-test.yml)
[![antsibull-docs-lint](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/actions/workflows/antsibull-docs-lint.yml/badge.svg)](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/actions/workflows/antsibull-docs-lint.yml)

{{ cookiecutter.description }}

<!-- TODO: ## Code of Conduct

We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.
-->

<!-- TODO: ## Collection maintenance

The current maintainers are listed in the [CODEOWNERS](https://github.com/{{ cookiecutter.scm_repository | replace("https://github.com/", "") }}/.github/CODEOWNERS)) file. If you have questions or need help, feel free to mention them in the proposals.

To learn how to maintain / become a maintainer of this collection, refer to the [Maintainer guidelines](MAINTAINING.md).
-->

<!-- TODO: ## Tested with Ansible
List the versions of Ansible the collection has been tested with.e
Must match what is in galaxy.yml.
-->

<!-- TODO: ## External requirements
List any external resources the collection depends on, for example minimum versions of an OS, libraries, or utilities.
Do not list other Ansible collections here.
-->

<!-- TODO: ## Supported connections (Optional)
If your collection supports only specific connection types (such as HTTPAPI, netconf, or others), list them here.
-->

<!-- TODO: ## Included content
Galaxy will eventually list the module docs within the UI, but until that is ready, you may need to either describe your plugins etc here, or point to an external docsite to cover that information.
-->

## Using this collection

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```console
ansible-galaxy collection install {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }}
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }}
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:

```console
ansible-galaxy collection install {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }} --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```console
ansible-galaxy collection install {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }}:==0.1.0
```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

<!-- TODO: ### Examples
Include some quick examples that cover the most common use cases for your collection content.
-->{% if cookiecutter.enable_antsibull_changelog %}

## Release notes

See the [changelog]({{ cookiecutter.scm_repository }}/tree/main/CHANGELOG.rst).{% endif %}{% if cookiecutter.license != 'none' %}

## Licensing
{% if cookiecutter.license == "GPL-3.0-or-later" %}
GNU General Public License v3.0 or later

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.{% elif cookiecutter.license == "AGPL-3.0-or-later" %}
GNU Affero General Public License v3.0 or later

See [LICENSE](https://www.gnu.org/licenses/agpl-3.0.txt) to see the full text.{% elif cookiecutter.license == "Apache-2.0" %}
Apache License 2.0

See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0.txt) to see the full text.{% elif cookiecutter.license == "MIT" %}
MIT License

See [LICENSE](https://spdx.org/licenses/MIT.html) to see the full text.{% elif cookiecutter.license == "BSD-3-Clause" %}
BSD 3-Clause License

See [LICENSE](https://spdx.org/licenses/BSD-3-Clause.html) to see the full text.{% endif %}{% endif +%}
