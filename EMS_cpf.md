---
Continuation Power Flow
---

The power flow equations are parameterized by a factor, say L which represents the variation of load demand.  

The purpose of continuation power flow is to trace thee solutions as the parameter L varies.  There are essentially two phases in the CPF computation: Predictor and Corrector

## Predictor - Tangent Method

This step is to find a next point (what do they mean by next point?) starting from an initial point.  


## Corrector - Newton's Method

The predictor step leads to the next point which is generally not on the PV curve.  It however serves as the initial values for the computation of the power flow solution.  Since the power flow equations have been parameterized, we have the two equations involving three unknowns.  Newton's method is a natural choice for finding the solution.

Parameterize the power flow model with L.

Predictor - Find a next point starting from an initial point.  Use the tangent method.

Corrector - (the predictor step leads to the next point which is generally not on the PV curve.  In the corrector step use Newton's Method to find the next point on the PV curve.

### References:

http://www.eecs.wsu.edu/~ee521/Material/20121030/Continuation%20Power%20Flow%20Example.pdf


## What we do


	cpf loop


		if nose found
			
			exit

		if psi_cpf == 0 and contiouation param == 0 

			exit

		


		i'm pretty sure this is the predictor step
		solve_cpf(1)

		i'm pretty sure this is the corrector step
		solve_cpf(0)




	while (converged < CONVERGED)
	{
	
		if pf_cd == ON
			dbsolve();

		newton_iter = 0;
		
		while(converge < CONVERGED)
		{

			converge = 0;
			newton_iter++;

			Loop through loads

			Loop through gens

			Check deadband stuff

			If continuation_param != 0
				Set continuation bus to type pv


			build_jacobian_cpf();

			
				
	}



The continuation parameter is used to...


The predict parameter is used to...


What is the deal with patterns?

What are steps?  Why are we saving them?
