---
title: Breaker Flow
---

## Summary

> Breaker flow is a licensable feature that enables the PF calculation of flows through individual breakers in the system.  


Breaker flow starts by removing all branches in the system and replacing each end of the branch with a generator of the same (same what?).  It them changes all breakers to branches.  As a result all nodes are treated as Dbuses and all Dbuses are treated as islands.  Power flow is then run using the new network topology, allowing for the powerflow through individual breakers to be calculated.


## Process

This is not meant to be an exhaustive guide to the breaker flow process (for that see the code) but rather a general outline of what breaker flow is doing for a coding perspective.


### main()


Breaker Flow starts by parsing arguments.  

Arrays are allocated and initialized for Power Flow and Topology

Sizings are initialized

Then `cal_breaker_flow()` is called


### cal\_breaker\_flow()

`save_sbus_voltages()` is called

`na_input(PF+Brk_Flow)` is called

`topology(0)` is called

Dbus voltages are assigned using the saved sbus voltages.

`fdpf()` is called

`output_brk_flow()` is called
