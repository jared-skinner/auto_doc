---
title: Power Flow
---




## What is Power Flow?

In an electrical network with a SCADA system, not all values are known (what values?).  Power Flow is the process of solving for all values in order to see a complete picture of the electrical network.  The equations involved in performing powerflow are ugly and so numerical methods are employed to find a solution.

### See Also

[Wikipedia Article](https://en.wikipedia.org/wiki/Power-flow_study)



## The osi\_pf executable

### The osi\_pf help message

```
Usage: osi_pf [<options>]

Runs either Power Flow (default), Network Topology or Load Allocation.

Options:
  -?, -h                 Show this help information.
  -e                     Do not display SCADA warnings.
  -v                     Show version information.
  -N                     Run network topology.
  A=<ALLOCATION TYPE>    Run load allocation with allocation type <ALLOCATION TYPE>.
  E=<D,O,F,R,I>          The D O F R I of the value which needs to be allocated when running load
                         allocation.  <D,O,F,R,I> must be comma separated with no spaces before or after
						 each comma.
  I=<INST No>            The instance number.
  S=<SCREEN No>          A workspace identification number.
```

### Ways osi\_pf is used

* Topology - See [Network Topology](/EMS/topology.html)

* Power Flow

* Load Allocation


## The CONVERGE Variable


The CONVERGE variable is used throughout the power flow logic for a variety of reasons



## Newton's method


## Fast Decoupled Power Flow


## DC Power Flow



## Subroutines

### substitution\_solution

Apply MW/MVar substitution solution to a given vector and then apply any compensations.

### tap\_controls

### shunt\_control

### MW/MVAR Mismatch

