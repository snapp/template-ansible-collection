# Ⓐ Ansible Role: {{ cookiecutter.role_name }}

{{ cookiecutter.role_description }}

<!-- TODO: ## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->

<!-- TODO: ## Role Variables

 A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

An example variable.

  {{ cookiecutter.role_name }}_variable1

Another example variable.

  {{ cookiecutter.role_name }}_variable2

<!-- TODO: ## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

None
-->

## Using this role in an Ansible playbook

The following example shows how this role can be defined in a playbook with parameters passed to override default variables.

> **INFORMATION**
> It is recommended that you use a Fully Qualified Collection Name (FQCN) when referencing your roles.
>
> For simplicity, this example shows the use of a role *without* a FQCN.

```yaml
---
- hosts: '{{target|default("all")}}'
  roles:
    - role: {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }}.{{ cookiecutter.role_name }}
      {{ cookiecutter.role_name | replace('.','_') | replace('-','_') }}_variable1: true
      {{ cookiecutter.role_name | replace('.','_') | replace('-','_') }}_variable2: false
      tags: {{ cookiecutter.namespace }}.{{ cookiecutter.collection_name }}.{{ cookiecutter.role_name }}
```{% if cookiecutter.license != 'none' %}

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
