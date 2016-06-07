---
Logs and Reports
---


## The Convergence Log

### Configuring the convergence log

Several things need to be done in order to have message display to the convergence log.

* In `$OSI\profiles\osii\agent.xml`, under `<localFailoverAliases>`, `OPENNET\FILE\SOURCE` needs to be added.

* The environment needs to be restarted after this (figure out which process actually needs to be restarted).

* In OpenViewNET, navigate to `Advanced Tabulars → EMS Applications → OpenNet`

	* To enable convergence log reporting for **Power Flow** 

* To view the report, in OpenViewNET, navigate to `Advanced Tabulars → EMS Applications → OpenNet → Control Displays → Report Generation` and select one of the reports listed under `Convergence Logs`.
