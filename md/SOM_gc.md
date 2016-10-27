---
title: SOM configuration
---

# OpenNet Non-Critical Service Configuration

## Introduction

This chapter describes the procedure to configure **OpenNet's** Non-critical service.

The **OpenNet** non-critical service provides **OpenNet** integration with **SOM Planner** through the following two functions:

* Translation services from the **OpenNet** database to the **SCADA** database.  This allows **SOM Planner** to support switch orders on **OpenNet** devices, namely on breakers.

* Apply switch orders to a non real-time instance of the **OpenNet** database.  Upon successful execution of a switch order for an **OpenNet** breaker on a non real-time instance, **OpenNet** will make the corresponding change to the specified instance.

The *osii_onet_service* executable is an adapter that handles **OpenNet-**related SOM requests from **SOM Planner**.  The heartbeat of *osii_onet_service* is monitored through the process monitor in order to supervise its online activity.  The process monitor initiates auto restart if necessary.

	Note: osii_onet_service will only retrieve or write to a non real-time instance.

## Supported SOM Functions

All functionality supported in the OpenNet non-critical service is exposed through **SOM Planner**.  Please see the **SOM Planner** user's guide for more details.

## Configuring Process Monitor

To monitor the heartbeat of the OpenNet non-critical service adapter, the executable program *osii_onet_service* must be configured as one of the processes monitored by the process monitor. **OpenNet** database number eight should be provided in the DB#. Timeout sets the inactive time, in seconds, for the process to be deemed as dead. If the Alarm flag is ON for action taken after timeout, an alarm is issued in the case that the scheduling program is dead. If Restart is ON, the process will restart after timeout.

## Configuring the OpenNet non-critical service

To configure the **OpenNet** non-critical service:

1. Ensure that the appropriate version of **SOM Planner** is installed and configured (see the **SOM Planner** configuration guide).

	a. You will need version >= 2.0.12.0 in order to send messages to OpenNet stating that Switch Orders have successfully been executed.

1. Verify that *osii_onet_service* is included in `$OSI/profiles/<domain>/config/osii_mcp.xml`.

