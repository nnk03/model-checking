----------------------------- MODULE semaphores -----------------------------


(*
Ref pg 36 handbook of model checking

model the semaphore solution solution with only weak fairness constraints on relevant steps

a) Check mutual exclusion property (for all runs)

b) check starvation freeness (for all runs)
	(will be violated)

Var x : boolean
initially x = 1

0 : while(True){
1 :		Non-Critical;
2 :		request(x);
3 :		Critical;
4 :		release(x);
5 :	}

*)

EXTENDS Integers

VARIABLES  x, pc0, pc1

Init0 ==
/\ pc0 = 0

Init1 ==
/\ pc1 = 0

Init == Init0 /\ Init1 /\ (x = 1)

L01 ==
/\ pc0 = 0
/\ pc0' = 1
/\ UNCHANGED << x >>

L12 ==
/\ pc0 = 1
/\ pc0' = 2
/\ UNCHANGED << x >>

L23 == 
/\ pc0 = 2
/\ pc0' = 3
/\ x = 1
/\ x' = 0

L22 ==
/\ pc0 = 2
/\ pc0' = 2
/\ x = 0
/\ x' = 0

L34 ==
/\ pc0 = 3
/\ pc0' = 4
/\ UNCHANGED << x >>

L45 == 
/\ pc0 = 4
/\ pc0' = 5
/\ x' = 1

L50 ==
/\ pc0 = 5
/\ pc0' = 0
/\ UNCHANGED << x >>


M01 ==
/\ pc1 = 0
/\ pc1' = 1
/\ UNCHANGED << x >>

M12 ==
/\ pc1 = 1
/\ pc1' = 2
/\ UNCHANGED << x >>

M23 == 
/\ pc1 = 2
/\ pc1' = 3
/\ x = 1
/\ x' = 0

M22 ==
/\ pc1 = 2
/\ pc1' = 2
/\ x = 0
/\ x' = 0

M34 ==
/\ pc1 = 3
/\ pc1' = 4
/\ UNCHANGED << x >>

M45 == 
/\ pc1 = 4
/\ pc1' = 5
/\ x' = 1

M50 ==
/\ pc1 = 5
/\ pc1' = 0
/\ UNCHANGED << x >>

vars == << x, pc0, pc1 >>

Next0 ==
\/ L01
\/ L12
\/ L23
\/ L34
\/ L45
\/ L50

Next1 ==
\/ M01
\/ M12
\/ M23
\/ M34
\/ M45
\/ M50

Next == 
\/ (Next0 /\ UNCHANGED << pc1 >>)
\/ (Next1 /\ UNCHANGED << pc0 >>)


Fairness ==
/\ WF_pc0(L01)
/\ WF_pc0(L34)
/\ WF_pc0(L45)
/\ WF_pc0(L50)
/\ WF_pc1(M01)
/\ WF_pc1(M34)
/\ WF_pc1(M45)
/\ WF_pc1(M50)

Compassion == 
/\ SF_pc0(L23)
/\ SF_pc1(M23)

\* FairSpec only assumes weak fairness condition

FairSpec ==
/\ Init
/\ [] [Next]_vars
/\ Fairness

\* StrongFairSpec assumes weak fairness along with strong fairness corresponding to compassion constraints

StrongFairSpec ==
/\ Init
/\ [] [Next]_vars
/\ Fairness
/\ Compassion


MUTUAL_EXCLUSION ==
[] (~(pc0 = 3 /\ pc1 = 3))

NOSTARVE_0 == 
[] ((pc0 = 2) => <>(pc0 = 3))
(* This will be violated *)

NOSTARVE_1 == 
[] ((pc1 = 2) => <>(pc1 = 3))




=============================================================================
\* Modification History
\* Last modified Tue Mar 05 18:53:55 IST 2024 by neeraj
\* Created Tue Mar 05 17:31:22 IST 2024 by neeraj
