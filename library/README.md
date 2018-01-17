Bug fixes
=========

Here is the list of bug fixes provided by this role:

1. ovirt_vms.py

 - Contains a change that allows us to specify storage domain where all template disks should be created: [PR](https://github.com/ansible/ansible/pull/24012).
   The fix will be available in Ansible 2.4.

 - Contains a change that don't start VM if state is present and VM already exists: [PR](https://github.com/ansible/ansible/pull/28214).
   The fix will be available in Ansible 2.4.

 - Contains a change that fixes the logout: [PR](https://github.com/ansible/ansible/pull/30410).
   The fix will be available in Ansible 2.4.1.

Updated modules
===============

Here is list of updated modules:

1. ovirt_auth.py

- Support the ENV variables for `ovirt_auth`: [PR](https://github.com/ansible/ansible/pull/34878)
  The module will be available in Ansible 2.5.
