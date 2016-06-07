---
Pre-Operation Analysis (POA)
---

# Introduction

## Scope and Limitations

### Scope 

* Create a new OpenNet POA process that will interface with the new SCADAInterface POA API to provide OpenNET POA support.

* Create a new, standalone OpenNET POA analysis program, that will be called by the new OpenNET POA process, to perform one more OpenNET POA analyses:

	* **Load drop** - The existing load drop functionality will be moved to this new program - this only applies to breaker opening operations

	* **Island Energized-Grounded** (GISA) - Given a breaker, check if:

		* Breaker is connected to an already energized-grounded island.

		* opening/closing the breaker would ground an energized island or energize a grounded island.

	* **Island unacknowledged SCADA STATUS point alarm** (GISA) - For breaker open/close: check if any SCADA STATUS point in the same OpenNET island as the POA breaker contains any unacknowledged alarms(Num_unack field value is greater than 0 - i.e. any AOR associated with STATUS point has not acknowledge one or more alarms.).

	* **New violation check** (PAC) - Check for any new OpenNET violations that would be caused by a breaker open/close operation.

* Add energized-grounded state to tp_status to support coloring of energized-grounded islands in one-line diagrams (GISA).

**Are one-line diagrams those circut images?**

* The existing topology() function in the OpenNET library exits if an energized-grounded state is detected.  This behavior will be modified to just return an error code.  Any products that call the OpenNET topology library function, e.g., OpenVSA, will need to be updated to check for this return status (if they care and they don't already do this).

**What's the big deal about energized grounded?**

* POA function identifiers will not be configurable.  Instead the will use name of the form opennet_...

**I don't know what is meant by *function identifiers* **

### Limitations

* The new violation check (PAC) will only be supported in OpenNET 6.x (monarch 44), the other features will also be supported in OpenNET 5.5.x (monarch 40).

* POA will only support operation on the real-time OpenNET and SCADA databases.

* Processing of POA requests will be done sequentially.

* If the OpenNET POA process is disconnected from the control adaptor or the OpenNET database goes offline, then all queued POA requests will be cleared and not processed.

* The only POA operations that will be supported are open/close control operations on SCADA STATUS objects that correspond to OpenNET breakers.

**do we mean SCADA STATUS points which belong to the same island as the breaker in question?**

* The PAC new violation POA will run power flow, but will not explicitly run state estimator.  It will depend on the last SE run by real time sequence, i.e., whatever is in the most recent snapshot of the OpenNET real-time database.

* If the operated breaker is connected to an OpenNET SBUS that is set to off-line, then most analyses won't give meaningful results since internally OpenNET opens all breakers connected to an off-line SBUS.  No warnings will be issued for this case.

* There will be no specific checks implemented for quad state devices that have undefined status (GISA requirement 3). It is assumed that the ability to configure OpenNET to treat these devices as closed (via the .rc file) and POA support for Energized-Grounded analysis meets this requirement.

**What the heck is a *quad state device*? **

* load_drop analysis will change somewhat:

	* Current version:

		* Runs on a specified version of OpenNET database (real-time or study)

		* Writes to OpenNET database (loac_mw_dropped, breaker_operated, load_dropped_count). New version won't.

		* Has a special interface to SCADAInterface

	* New version:

		* Runs only on study instance (a study instance will be reserved just for this)

		* Won't write anything to database

		* When run for automated POA it will run on a study instance that is a snapshot of the real-time database and has measurement updates SCADA.  **What is this snapshot about?**

		* Will operate using the new POA API.

	* Current version of load drop program will be retained (no changes) for use when SCADAInterface POA API is not available (older versions of SCADAInterface).

#### Island unacknowledged STATUS point alarm analysis scope

* The requirement for Island unacknowledged status alarm is:

> OSI will enhance the available features so that the system provides a warning message to the operator if the operator attempts to send a command to a circut breaker or switch and there is an unacknowledged alarm associated to a network topology change within the same portion of the electric network/island.

**what do we mean by the same portion?**

The GISA approach to meeting this requirement is:

* Add *island number* and *alarm acknowledgement status* fields to *SCADA STATUS* objects.

* OpenNET will write breaker island numbers to their corresponding SCADA STATUS objects.

* There will be a standalone permanent calc which will loop through all the status points in the system and check if any has an alarm which has not been acknowledged (value extracted for TLQ, 'L' field). Based on the findings, it will update the specific field (described above) all the other status point which have the same island value as the particular status point will be marked that they have an unacknowledged alarm.

Rather than implement the approach described above, this document takes the approach that OpenNET will simply

1. Add a num_unack field to each OpenNET breaker. **Does num_unack something in the SCADA database?  What does it mean?**

2. Modify the *OpenNET SCADA measurement update* process to copy this field from SCADA to OpenNET.

3. Define an OpenNET POA function that checks if the num_unack field is > 0 for all OpenNET breakers in the same island as the operated breaker (**what does operated breaker mean?**).  This requres no calc and no modifications to the SCADA database.  Note that num_unack will be > 0 if any AOR **what is AOR?** associated with a STATUS point has not acknowledged an alarm.

This new approach was reviewed with the GISA team to verify that if meets their needs.

### Definitions, Acronyms and Abbreviations

| Term                 | Definition             |
|----------------------|------------------------|
| POA                  | Pre-Operation Analysis |
| POA API              | Pre-Operation Analysis API.  This is a new API that will be created as part of this project that will be used by other applications that need to provide pre-operation analysis. |
| POA Process          | A Messaging based process taht uses the POA API to provide pre-operation analysis functionality. |
| POA Function         | A specific type of analysis provided by a POA Process. |
| ENERGIZED_GROUNDED   | An island containing an online generator or inverter that is also connected to a GROUND object. |


## Use cases

### Use Case - One-Line Coloring of Energized-Grounded Devices

Users want one-line diagrams to show energized-grounded portions of networks with special colors whenever this situation occurs.

* Configure one-line diagrams to use tp_status for coloring, and assign the desired coloring to a tp_status of ENERGIZES_GROUNDED.

* Setup OpenNET real-time sequence to run NTP (or PF or SE). **What is real-time sequence?**

* If a breaker operation changes the energized-grounded status of a device, then the change will automatically show up, via the tp_status field, the next time the real-time sequence runs.


### Use Case - Perform OpenNET Pre-Operation Analysis before opening or closing a SCADA STATUS point.

**this right here is, in a small way, an answer to what POA is suppose to be doing**

Prior to opening or closing a SCADA STATUS control point (corresponding to an OpenNET breaker) a user wants to do one or more OpenNET pre-operation analyses.

* Configure SCADAInterfact to run the desired OpenNET POAs (via SCADAInterface -> POA App Settings)

* Configure system to start OpenNET POA process on the OpenNET server.

* If energized-grounded analysis is to be done:

	* OpenNET GROUND objects must be appropriately configured

	* Ground analysis must be enabled by setting ground_flag in OpenNET.rc to an appropriate value.

* Analyses will automatically be done, triggered by SCADAInterface POA API, whenever an operater attempts to open or close a SCADA STATUS point.


### Use Case - Have OpenNET Energized-Grounded POA issue a warning if quad state devices with undefined status could cause an energized-grounded condition if they are treated as closed.

Prior to opening or closing a SCADA STATUS control point (corresponding to an OpenNET breaker) users want a warning if quad state devices with undefined status would cause an energized-grounded condition if they are treated as closed.

**Again, what is up with quad state devices?**

* Configure as noted in the previous case, including the steps for energized-grounded analysis.

* Configure OpenNET to treat quad state devices with unknown status as closed (via OpenNet.rc STATES_0,1,2,3 parameters).


## Requirements

### Input Requirements

The requirements specified in the GISA and PAC DPCR's are:

#### GISA

1. OSI will enhance the available features so that the system should provide a warning message to the operator if the operator attempts to send a command to a circuit breaker or switch and there is an unacknowledged alarm associated to a network topology change within the same portion of the electric network / island.

2. OSI will enhance the available features so that the system should provide a warning message to the operator if the operator attempts to send a command to a circuit breaker or switch that belongs to a portion of an energized electric network / island that is grounded.  In order for this feature to work properly GISA will have to define all of the ground SBUS/node on OpenNet database.

3. OSI will enhance the available features so that the system should provide a warning message to the operator if the operator attempts to send a command to a circut breaker or switch and there are grounds on undefined status within the same portion of the electrical network/island.  In order for this feature to work properly GISA will have to define all of the ground SBUS/node on OpenNet database.

4. OSI will implement the enhancements so when the energized network is grounded, the network coloring of the monarch system will show the energized-grounded network immediately.


#### PAC

| Development Title | Contract Language | 
|---|---|
| Load Loss Check | If the Operator elects to issue the control request immediately, and bypasses the warning, an event message shall be logged to record the action. |  
| Load Pickup Check | The Load Pickup Check (LPC) feature shall support real-time validation of supervisory control requests.  For an Operator-initiaed "Close" control request on a telemetered switching device (e.g., bus tie breaker), the system shall determine, prior to issuing the control request, if closing the switching device will result in overloads and/or voltage violations, given the current loading and network configuration at the time of the request.  <p> The LPC feature shall use the Normal Operating limits when checking for violations.  <p> When the LPC determines that a violation will occur, it shall warn the Operator of the pending violation.  The warning message shall include the device(s) whose limits would be exceeded, as well as the amount of such violation(s) in percentage and absolute values.  The Operator shall have the option to either "CANCEL" or "EXECUTE" the close operation in spite of the warning.  <p>If the Operator elects to issue the control request immediately, and bypasses the warning, an event message shall be logged to record the action.  <p>The SCADA/EMS shall procvide a "Load Pickup Check" function which is a pre-validation test for equipment violations or overloads based on connectivity.  The check shall be performed on any telemetered device "Close" supervisory control sequence.  Refer to Load Pickup Check in Section 9 - SCADA for more information.|

The basic ability to perform per-operation analysis is provided by SCADAInterface POA API.  The only parts of the requirements listed above that are covered by this document are

1. General OpenNET support for POA via the SCADAInterface POA API

2. OpenNET support for performing OpenNET specific POA analyses.


## Architecture and Design

### Overview

* A OpenNet license feature, POA will be added.  The new OpenNET POA processes will check this new license and terminate with an appropriate message if not licensed.

* New num_unack **what is this?** field will be added to OPENNET BREAKER objects and existing osi_rt_snap process will be modified to retrieve SCADA STATUS point num_unack field, via call to SCADAGetValue in SCADAApi.

* New header file poa.h will be created that defines temporary file names used for file locking and output of poa results.

* Existing OpenNET code will be modified to determine energized-grounded state of devices and set tp_status = ENERGIZED_GROUNDED when appropriate (includes adding ENERGIZED_GROUNDED state to st=115).  Existing grounding analysis code will be mostly replace.

* Existing osi_se will be modified so that if it runs successfully and it using the real time instance, then it will save a copy of the real time database to a file ("poa.08.SAV") stored in directory SAVECASEDIR\SYSTEM\opennet DBMS_copy call.  This copy will be for exclusive use by the POA process and is to avoid having POA tying to snapshot the OpenNET real time DB and having to wait for some other OpenNET process to finish using it.  osii_file_open and its file locking methods will be used to obtain exclusive access to the savecase file to prevent osi_onet_poa from reading the file while it is being modified.  File lock will be a temporary file in the temp directory.























