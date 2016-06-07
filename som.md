---
ONET SOM Development
---

##Introduction

###Overview and Background
This document covers the design details of the OpenNet portion of the ONET\_SOM project.  OpenNet and SOM Planner integration is key for supporting EMS customers that will be use SOM Planner.  The goal is to add functionality to allow creating, simulating and executing Switch Orders with OpenNet devices.

### Scope and Limitations

#### Scope

The scope of this porject is:

* Create a new OpenNet

* Update the POA adapter to be a generic OpenNet adapter and add the following functionality:

	* Attempt to register to Messaging.

	* Provide an API that takes an OpenNet device URL and translate to the SCADA URL.

	* Provide an API that recieves a notification of a switch change and implements it in the OpenNet model if it is in a non-Real Time instance.


#### Limitations

This will not require Schema changes, configuration changes, or additional dependencies upon OpenNet.


### Definitions, Acronyms and Abbreviations

| Term | Definition |
|---|---|
| SOM | Switch Order Management |
| POA | Pre-Operation Analysis |


### References

1.	SOM\_ONET\_Project\_Code\_Request.pdf
2.	OpenNet%20and%20SOM%20Planner.docx

Published monarch System Requirements Specifications (SRS) document

1.	http://osiinet/QMS/SW\_Schema\_Design\_Guidelines\_R.pdf
2.	http://osiinet/QMS/SW\_Secure\_Coding\_Guidelines\_R.pdf
3.	http://osiinet/QMS/SW\_RDBMS\_Interaction\_Guidelines\_R.pdf


## Use cases

### Use Case 1

A device is added to a Switch Order request.  This addition is processed by SOM Planner and added to excel.  SOM Planner communicated with the OpenNet SOM Service via messaging to translate the device url to a SCADA url.

### Use Case 2

An Action from excel is executed via the SOM Planner.  SOM Planner sends the request to the SCADA Control Adapter.  On success SOM notifies OpenNet of success via the OpenNet SOM Service through messaging).

## Requirements

### Input Requirements

The requirement specified are:

* The SOM Service should make requests to OpenNet via a new interface, the OpenNet SOM Service, to do work.  SOM makes these requests via messaging.

* The OpenNet SOM Service can be its own messaging connected service or added to an existing one.

* SOM detects when this service is running in order to communicate with it.

* The OpenNet SOM service will take in a device URL and translate it into a SCADA url.

* SOM Planner will also be enhanced to send a notification when a control has been executed. It will send this notification in real time and study modes. The notification will provide what control was executed/simulated and the OpenNet SOM Service can determine what in its database needs to be updated and if any other processing should be run.

* We may need to license this new feature.

### System Requirements

#### Published System Requirements

None.

#### Proposed System Requirements

Unknown

### Product Requirements

Unknown

### Monarch Application Programming Standards


## Architecture and Design

### Overview

~ Image describing process ~

---

In the two diagrams shown, the SOM Service makes requests to OpenNet via a new interface, the OpenNET SOM Service, to do work. SOM makes these requests via messaging. The OpenNET SOM Service can be its own messaging connected service or added to an existing one. There is no dependency added to OpenNet to provide this support. SOM detects when this service is running in order to communicate with it.

The SOM Planner and eMap products have examples of the translation implementation. The translation takes a URL that has been broken down into its base components (database, object, field, record/key, and index) to gather various information about a device; name and control information.

SOM Planner will also be enhanced to send a notification when a control has been executed. It will send this notification in real time and study modes. The notification will provide what control was executed/simulated and the OpenNet SOM Service can determine what in its database needs to be updated and if any other processing should be run.

---

*	A gserver based OpenNet POA process, onet_messaging will be created which:
	*	Runs on the OpenNet servers and needs to be registeredin osii_mcp.xml.
	*	Uses mutexes to control access where needed, e.g. when adding or removing elements to POA request queue.
	*	The POA functionality will be moved from osii_onet_poa to osii_onet_messaging.xml.
	*	The POA helper functions will stay in their respecting functions.
	*	The process needs to be designed with extensibility in mind.  If OpenNet


	*	gserver_main is the main function used.  The following needs to happen before getting to the main loop:

		*	POA:
			*	For the most part this will be the same as the present logic

		*	For each service:

			*	A callback string will need to be defined with type GSERVER_CALLBACK_STR.  The naming convention will be \<service name\>_cbs.

			*	A handle will need to be defined with type GSERVER_PROPER_HANDLE.  The naming convention will be \<service name\>_prop.

			*	The service will be registered using gserver_prop_init().

			*	Callback functions will be registed using prop->add(prop, "command", callback, NULL).


	*	After initialization gserver_main will have an infinite loop that:

		*	POA:
			*	For the most part this will be the same as the present logic

		*	For each service:
			* Binds/unbinds services


		*	If OpenNet database is off-line

*	A new OpenNet SOM process will be written that:
	*	Provide an API to takes an OpenNet device URL and translates it into a SCADA URL.
	*	Provide an API that receives a notification of a switch change and implements it in the OpenNet model if it is in a non-Real Time instance.
	*	An OpenNet license feature **may** need to be added for OpenNet SOM Service.
	*	A service will be registered with gserver to provide these new functions as callbacks to SOM Planner.

### External Interfaces

#### SOM API

The SOM API will consist of two functions:

*	The first function will accept a device url


#### OpenNet Messaging Interface

A new generic messaging adaptor will be written using gserver.  It will take the place of the current messaging interface for POA and will allow for new services to be added as well.  The SOM API will be exposed through a service running on this adaptor.

### Process Components

#### Modifications to existing OpenNET code




#### New OpenNet osi_onet_messaging processs

```c
/*******************************************************************************
* Some note about what needs to be done in order to add a new process          *
*******************************************************************************/
void gserver_main()
{
	char * som_commands[], * poa_commands[];
	GSERVER_DATA_CALLBACK som_callbacks[], poa_callbacks[];
	OSI_BOOL msg_online = false;

	//initialize callback strings
	GSERVER_CALLBACK_STR som_cbs = {0};

	//initialize handlers
	GSERVER_PROPER_HANDLE som_prop = NULL;

	// initialize opennet database


	/***************************************************************************
	* POA initialization                                                       *
	***************************************************************************/
	// program login to messaging???

	// license check

	// load ca client functions

	/***************************************************************************
	* Services initialization                                                  *
	***************************************************************************/
	// for each service there will be a separate function to do all the
	// registeration stuff for the service
	som_prop = gserver_prop_init("command", gserver_def_callback, NULL);

	// set the data callback to use the properties hash

	// register callbacks

	// it would be really nice if we could create a couple arrays for each
	// service to register callbacks.  The first array would have all the
	// command names and the second would have all the callbacks.  Then we could
	// just iterate over the arrays for each service.
	register_callbacks("som");

	//main loop, do failover checks and heartbeating here
	while (true)
	{
		// heartbeat every cycle
		gserver_heartbeat();

		// check that messaging is online
		msg_online = osii_msg_server_online(egbl.msgc)

		// check that the OpenNet DB is online


		/***********************************************************************
		* POA portion of loop                                                  *
		***********************************************************************/

		if (!prog_running)
			prog_start;
		else
			prog_main();

		//this stuff is going to need it's own thread!


		/***********************************************************************
		* services portion of loop                                             *
		***********************************************************************/
		// if we are online, always attempt to rebind, avoids bad failover
		// conditions (bind services)
		if (msg_online)
			bind_services();
		else
			unbind_services();
	}
}

void bind_services()
{
	gserver_bind("som", &som_cbs);
}

void unbind_services()
{
	gserver_unbind("som");
}

void register_callbacks()
{
	som_prop->add(som_prop, "command1", callback1, NULL);
	som_prop->add(som_prop, "command2", callback2, NULL);
}

void gserver_process_argv(int argc, char * argv[])
{
	// Set the number of threads in the thread pool


	// in here is where the service name is set up if we want to use the global
	// name


	// process global args
}

```
#### New OpenNet som libaray

### Data Design

When OpenNet receives a notification from SOM Planner of a switch change, it will implement it into the OpenNet model if it is in a non-Real time instance.

### User Interface

None.

### Dependencies

There is no dependency added to OpenNet to provide this support.

### Assumptions and Constraints

Ask about this!


## Test Plan

### Testing Notes

*	The same requirements for testing GISA_PAC1_OPENNET_POA will need to be met for this project

*	SOM will need to be running

### New External Test Procedures

Ask about this!

### New Internal Test Procedures

Ask about this!

### Quality Engineer

Someone from the EMS team who is familar with this project can act as a quality engineer to test this project.

### Test Setup

Proper installation of M40 (and/or M44) including OpenNET and Advanced Tabulars is needed.

To test the POA functionality SCADA, SCADAInterface, and Messaging must be installed.  Also, SCADAInterface POA must be configured and the OpenNet POA process running.
