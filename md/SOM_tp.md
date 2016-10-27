---
title: SOM test procedures
---

# OpenNet Noncritical Service Test Procedures

**Purpose**
The purpose of this section is to check that the functions of the OpenNet noncritical service are performing properly.

	Note: To run this test SOM Planner must be installed and configured (see the SOM Planner configuration guide), OpenSCADA must be installed and configured (see the OpenSCADA configuration guide) and the OpenNet Non-critical Service must be configured (see the OpenNet configuration guide).

**Preparation**

1. Start *osii_onet_service*, *osii_som_planner*, and *osii_scada_som_service*

1. In `$OSI/msoffice` make a copy of `SwitchOrderTemplate.xlsx` to `SwitchOrderTemplate_test.xlsx`

1. Open `SwitchOrderTemplate_test.xlsx`

1. In **OpenViewNet** right click on the widget panel and select `Create Widget`

1. In the Widget Toolbox select `Action Button`

1. Right click on the newly created action button and select `Edit Command`

1. In the Command Editor find and select the command `Add to Switch Order`.  Click `Next`.

1. In the data grid find the row labeled *Data Link URL*.  Modify the *Data* field to read *@AURL*

1. Click `Ok`

1. Right click on the action button and uncheck `movable`.



### Adding a single breaker record to a Switch Order

1. Find a breaker with a SCADA key belonging to a valid SCADA record.

1. Click on one of the fields for this record.

1. Click the widget button created during preparation. (A window should come up asking if you wish to add these fields to SwitchOrderTemplate_test.xlsx.  If this does not happed, something is misconfigured.)

1. Verify that the breaker record was successfully added to `SwitchOrderTemplate_test.xlsx`.


### Adding several breaker records to a Switch Order

1. Repeat the previous test, but select a field for several records.

1. Verify that the breaker records were successfully added to `SwitchOrderTemplate_test.xlsx`.


### Adding invalid records

1. Select a breaker record which is not linked to a valid SCADA record

1. Click the widget button created during preparation.

1. Verify that nothing is added to the switch order.

1. Select some non-breaker record.

1. Click the widget button created during preparation.

1. Verify that nothing is added to the switch order.

1. Select a breaker record whose record field is set to 0.

1. Click the widget button created during preparation.

1. Verify that nothing is added to the switch order.




### Applying switch change

The SOM ribbon in the excel spreadsheet has two buttons labeled Real-Time and Study. These buttons represent the different instances where the switch order should be applied.

The Operation type under Operation should either be manual or operation.

Next to this is the action which should take place this should either be "Open" or "Close".


#### Study:

Click the Study button.

1. Select an order with Operation type "Manual" and name "Breaker <number>".

1. Click Execute.

1. Verify no message is sent to OpenNet.

1. Select an order with Operation type "Operation" and name "Breaker <number>".

1. Click Execute.

1. Verify OpenNet translates a SCADA point with the correct breaker number.

1. Verify SOM sends a message with the SCADA point to be applied, the operation type "operation" and the state to apply (0 for open 1 for closed).

1. Select a breaker switch order.

1. Manually change the record field for this breaker to 0, in the database.

1. Click Execute.

1. Verify that OpenNet did not apply the operation.

1. Select a breaker switch order.

1. If necessary modify the switch order so the action is the same as the current state of the breaker.

1. Click Execute. 

1. Verify that OpenNet displays a message stating that there is nothing to apply.


#### Real Time:

Click "Cancel" to exit out of "Study".  Click "Real-Time"

1. Try executing a Breaker record of type manual. OpenNet should not receive a message.

2. Try executing a Breaker record of type Operation. OpenNet should display a message that Switch Orders can only be applied on study instances.
