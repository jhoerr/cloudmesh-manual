# Flavor

## AWS

### Gregors PC

This is don on Windows 10 in the 18.04 Ubuntu Linux subsystem with
python 3.7

```
+-----------------------------+--------+-----+----------------------+------+--------+-------------+-------------+
| timer                       | time   | tag | node                 | user | system | mac_version | win_version |
+-----------------------------+--------+-----+----------------------+------+--------+-------------+-------------+
| test_empty_database         | 0.01   | aws | ('DESKTOP-gregor9',) | blue | Linux  |             |             |
| test_provider_flavor        | 92.34  | aws | ('DESKTOP-gregor9',) | blue | Linux  |             |             |
| test_provider_flavor_update | 168.03 | aws | ('DESKTOP-gregor9',) | blue | Linux  |             |             |
| test_cms_flavor_refresh     | 182.62 | aws | ('DESKTOP-gregor9',) | blue | Linux  |             |             |
| test_cms_flavor             | 4.8    | aws | ('DESKTOP-gregor9',) | blue | Linux  |             |             |
| benchmark_start_stop        | 0.0    | aws | ('DESKTOP-gregor9',) | blue | Linux  |             |             |
+-----------------------------+--------+-----+----------------------+------+--------+-------------+-------------+
```

### Gregor's macOS Laptop

```
+-----------------------------+--------+-----+-----------+------+--------+-------------+-------------+
| timer                       | time   | tag | node      | user | system | mac_version | win_version |
+-----------------------------+--------+-----+-----------+------+--------+-------------+-------------+
| test_empty_database         | 0.02   | aws | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_provider_flavor        | 121.8  | aws | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_provider_flavor_update | 247.81 | aws | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_cms_flavor_refresh     | 259.92 | aws | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_cms_flavor             | 5.5    | aws | ('greg',) | greg | Darwin | 10.14.5     |             |
| benchmark_start_stop        | 0.0    | aws | ('greg',) | greg | Darwin | 10.14.5     |             |
+-----------------------------+--------+-----+-----------+------+--------+-------------+-------------+
```

## Openstack

### Gregor's macOS Laptop

```
+-----------------------------+------+-----------+-----------+------+--------+-------------+-------------+
| timer                       | time | tag       | node      | user | system | mac_version | win_version |
+-----------------------------+------+-----------+-----------+------+--------+-------------+-------------+
| test_empty_database         | 0.01 | chameleon | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_provider_flavor        | 1.36 | chameleon | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_provider_flavor_update | 0.74 | chameleon | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_cms_flavor_refresh     | 3.39 | chameleon | ('greg',) | greg | Darwin | 10.14.5     |             |
| test_cms_flavor             | 1.88 | chameleon | ('greg',) | greg | Darwin | 10.14.5     |             |
| benchmark_start_stop        | 0.0  | chameleon | ('greg',) | greg | Darwin | 10.14.5     |             |
+-----------------------------+------+-----------+-----------+------+--------+-------------+-------------+
```

