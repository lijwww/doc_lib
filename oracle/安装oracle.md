#### /etc/security/limits.conf 

```
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
```

#### /etc/pam.d/login 

#### 

```
session required /lib/security/pam_limits.so
session required pam_limits.so
```

#### 

**session required /lib/security/pam_limits.so**
**********session required pam_limits.so**********

#### 