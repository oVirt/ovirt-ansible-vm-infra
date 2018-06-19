#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'ovirtvmip': self.ovirtvmip,
            'ovirtvmips': self.ovirtvmips,
            'ovirtvmipv4': self.ovirtvmipv4,
            'ovirtvmipsv4': self.ovirtvmipsv4,
            'ovirtvmipv6': self.ovirtvmipv6,
            'ovirtvmipsv6': self.ovirtvmipsv6,
        }
 
    def ovirtvmip(self, ovirt_vms, attr=None):
        return self.__get_first_ip(self.ovirtvmips(ovirt_vms, attr))

    def ovirtvmips(self, ovirt_vms, attr=None):
        return self._parse_ips(ovirt_vms, attr=attr)

    def ovirtvmipv4(self, ovirt_vms, attr=None):
        return self.__get_first_ip(self.ovirtvmipsv4(ovirt_vms, attr))

    def ovirtvmipsv4(self, ovirt_vms, attr=None):
        return self._parse_ips(ovirt_vms, lambda version: version == 'v4', attr)

    def ovirtvmipv6(self, ovirt_vms, attr=None):
        return self.__get_first_ip(self.ovirtvmipsv6(ovirt_vms, attr))

    def ovirtvmipsv6(self, ovirt_vms, attr=None):
        return self._parse_ips(ovirt_vms, lambda version: version == 'v6', attr)

    def _parse_ips(self, ovirt_vms, version_condition=lambda version: True, attr=None):
        if not isinstance(ovirt_vms, list):
            ovirt_vms = [ovirt_vms]

        if attr is None:
            return self._parse_ips_aslist(ovirt_vms, version_condition)
        else:
            return self._parse_ips_asdict(ovirt_vms, version_condition, attr)

    def _parse_ips_asdict(self, ovirt_vms, version_condition=lambda version: True, attr=None):
        vm_ips = {}
        for ovirt_vm in ovirt_vms:
            ips = []
            for device in ovirt_vm.get('reported_devices', []):
                for ip in device.get('ips', []):
                    if version_condition(ip.get('version')):
                        ips.append(ip.get('address'))
            vm_ips[ovirt_vm.get(attr)] = ips
        return vm_ips

    def _parse_ips_aslist(self, ovirt_vms, version_condition=lambda version: True):
        ips = []
        for ovirt_vm in ovirt_vms:
            for device in ovirt_vm.get('reported_devices', []):
                for ip in device.get('ips', []):
                    if version_condition(ip.get('version')):
                        ips.append(ip.get('address'))
        return ips

    def __get_first_ip(self, res):
        return res[0] if isinstance(res, list) and res else res
