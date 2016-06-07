---
title: Smoke Test
---

## Introduction

The smoke test is a tool used to check the integrity of the code put out by the EMS team.  



## Maintanace

If the `ems_dev2` VM is down, please see **Caleb Ahlquist** for restarting it.


For all credentials please see **Jeremy Mattke**, **Sam Handler** or **Jared Skinner**

### Connecting to ems\_dev2

The smoke test code can be accessed on `ems_dev2` via **remote desktop**.

```
user: ems_dev2\Administrator
```

### Starting Services

These instructions are for starting up the smoke test and static analysis tests.  

- Start the **WRBotSSHAgent** service.
- Start a shell as osiserv\_act 

		$ runas /user:osiserv_act cmd

		$ set SSH_AUTH_SOCK=/cygdrive/c/ems_services/authentication/ssh-agent.sock

 You will be prompted for a password 

- Add the ssh key

		$ C:\cygwin64\bin\ssh-add.exe /cygdrive/c/ems_services/authentication/id_rsa

 You will be prompted for a password

- Start the **WRBot** service.
