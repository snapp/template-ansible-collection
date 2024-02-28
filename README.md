# Cookiecutter Template: Ⓐ Ansible Collection

[![Github License](https://img.shields.io/github/license/snapp/template-ansible-collection)](https://github.com/snapp/template-ansible-collection/blob/main/LICENSE)
[![Ansible Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Ansible-silver.svg)](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)
[![CI](https://github.com/snapp/template-ansible-collection/actions/workflows/main.yml/badge.svg)](https://github.com/snapp/template-ansible-collection/actions/workflows/main.yml)

This project provides an opinionated template for bootstrapping an Ansible Collection that extends the minimal structure provided by `ansible galaxy collection init`.

By leveraging [cookiecutter](https://www.cookiecutter.io) you will be asked a small number of questions (e.g., namespace, collection name, etc.) which will then be automatically applied to the resulting directory structure.

> [!NOTE]
> This template draws inspiration from the [Ansible Community GitHub Collection Template](https://github.com/ansible-collections/collection_template).

> [!WARNING]
>
> This code is NOT supported by Red Hat and may not work as expected.
>
> Red Hat does not guarantee its correctness, reliability, or performance.
>
> Use at your own risk!

## Requirements

```console
$ pip install cookiecutter
```

## Using this template

```console
$ cookiecutter https://github.com/snapp/template-ansible-collection
```

### Overriding template defaults

Cookiecutter provides a few options for specifying user configurations which can be used to override the template default question values.

Creating a `.cookiecutterrc` file in your home directory is the easiest way to specify a user configuration, but you can also pass a config file in at runtime using the `--config-file` option.

> [!NOTE]
> cookiecutter configuration files are formatted in YAML syntax

**Example:**
```yaml
---
default_context:
  author: "snapp@example.com"
  namespace: "snapp"
```

See the [Advanced Usage / User Config](https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html) documentation for more information.

# License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

snapp@redhat.com
