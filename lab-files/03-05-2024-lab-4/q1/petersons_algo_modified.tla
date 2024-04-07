---------------------- MODULE petersons_algo_modified ----------------------

EXTENDS Integers

VARIABLES pc0, pc1, turn, intr0, intr1

TypeOK == 
/\ pc0 \in 0..7
/\ pc1 \in 0..7
/\ turn \in {0, 1}
/\ intr0 \in {0, 1}
/\ intr1 \in {0, 1}

(*
a) adding weak fairness constraints on steps where applicable and
b) check 
   i) whether all runs satisfy starvation freeness i.e a process requesting to enter CS at any instant will be allowed
   to enter CS at a future instant
   ii) whether all runs mandate strict sequencing between process 1 and process 2 in critical section
        show a trace where strict sequencing need not hold
        
   Ref pg 36 of handbook of model checking
*)


(*
asynchronous system

for i = 0, 1

the algorithm is

0 : while(True){
1 :     // non critical section
2 :     intr[i] = True
3 :     turn = 1 - i
4 :     while(turn == 1 and intr[1 - i] == 1) // wait
5 :     // critical section
6 :     intr[i] = 0
7 : }

weak fairness : 

*)

Init0 ==
/\ turn = 0
/\ intr0 = 0
/\ pc0 = 0

Init1 ==
/\ turn = 0
/\ intr1 = 0
/\ pc1 = 0

Init == Init0 /\ Init1

L01 == 
/\ pc0 = 0
/\ pc0' = 1
/\ UNCHANGED << turn, intr0, intr1 >>

L12 == 
/\ pc0 = 1
/\ pc0' = 2
/\ UNCHANGED << turn, intr0, intr1 >>


L23 ==
/\ pc0 = 2
/\ pc0' = 3
/\ intr0' = 1
/\ UNCHANGED << intr1, turn >>

L34 ==
/\ pc0 = 3
/\ pc0' = 4
/\ turn' = 1
/\ UNCHANGED << intr0, intr1 >>

L44 ==
/\ pc0 = 4
/\ pc0' = 4
/\ turn = 1
/\ intr1 = 1
/\ UNCHANGED << intr0, intr1, turn >>

L45 ==
/\ pc0 = 4
/\ pc0' = 5
/\ (turn = 0 \/ intr1 = 0)
/\ UNCHANGED << turn, intr0, intr1 >>

L56 ==
/\ pc0 = 5
/\ pc0' = 6
/\ UNCHANGED << intr0, intr1, turn >>

L67 ==
/\ pc0 = 6
/\ pc0' = 7
/\ intr0' = 0
/\ UNCHANGED <<intr1, turn>>

L70 ==
/\ pc0 = 7
/\ pc0' = 0
/\ UNCHANGED << turn, intr0, intr1 >>

SLOGP == UNCHANGED << pc0, intr0, intr1, turn >>

\* for the second system

M01 == 
/\ pc1 = 0
/\ pc1' = 1
/\ UNCHANGED << turn, intr0, intr1 >>

M12 == 
/\ pc1 = 1
/\ pc1' = 2
/\ UNCHANGED << turn, intr0, intr1 >>


M23 ==
/\ pc1 = 2
/\ pc1' = 3
/\ intr1' = 1
/\ UNCHANGED << intr0, turn >>

M34 ==
/\ pc1 = 3
/\ pc1' = 4
/\ turn' = 0
/\ UNCHANGED << intr0, intr1 >>

M44 ==
/\ pc1 = 4
/\ pc1' = 4
/\ turn = 0
/\ intr0 = 1
/\ UNCHANGED << intr0, intr1, turn >>

M45 ==
/\ pc1 = 4
/\ pc1' = 5
/\ (turn = 1 \/ intr0 = 0)
/\ UNCHANGED << turn, intr0, intr1 >>

M56 ==
/\ pc1 = 5
/\ pc1' = 6
/\ UNCHANGED << intr0, intr1, turn >>

M67 ==
/\ pc1 = 6
/\ pc1' = 7
/\ intr1' = 0
/\ UNCHANGED <<intr0, turn>>

M70 ==
/\ pc1 = 7
/\ pc1' = 0
/\ UNCHANGED << turn, intr0, intr1 >>


SLOGQ == UNCHANGED <<pc1, intr0, intr1, turn>>

Next_First == 
\/ L01
\/ L12
\/ L23
\/ L34
\/ L45
\/ L56
\/ L67
\/ L70
\/ SLOGP

Next_Second ==
\/ M01
\/ M12
\/ M23
\/ M34
\/ M45
\/ M56
\/ M67
\/ M70
\/ SLOGQ

Next == (Next_First /\ UNCHANGED pc1) \/ (Next_Second /\ UNCHANGED pc0)

Mutual_Exclusion == (pc0 # 5) \/ (pc1 # 5)

\* we need justice conditions, because here in this example, it can happen that
\* the scheduler never schedules one process
\* we want to avoid such runs ?????

\* justice conditions

J00 == pc0 # 0
J02 == pc0 # 2
J03 == pc0 # 3

\* we cannot write pc0 # 4, because that's not a requirement, it should be proven
J04 ==  ~((pc0 = 4) /\ ((turn = 0) \/ (intr1 = 0)))
J05 == pc0 # 5
J06 == pc0 # 6
J07 == pc0 # 7

\* for the process 1

J10 == pc1 # 0
J12 == pc1 # 2
J13 == pc1 # 3

J14 ==  ~((pc1 = 4) /\ ((turn = 0) \/ (intr0 = 0)))
J15 == pc1 # 5
J16 == pc1 # 6
J17 == pc1 # 7

\* the below justice conditions are to ensure that the scheduler is fair

J ==
/\ J00
/\ J02
/\ J03
/\ J04
/\ J05
/\ J06
/\ J07
/\ J10
/\ J12
/\ J13
/\ J14
/\ J15
/\ J16
/\ J17

(*
L45 should be added to weak fairness, the semantics of weak fairness
and justice conditions are different
L12 should not be added weak fairness since the process can remain
in non-critical section forever
*)


Fairness ==
/\ WF_pc0(L01)
/\ WF_pc0(L23)
/\ WF_pc0(L34)
/\ WF_pc0(L45)
/\ WF_pc0(L56)
/\ WF_pc0(L67)
/\ WF_pc0(L70)
/\ WF_pc1(M01)
/\ WF_pc1(M23)
/\ WF_pc1(M34)
/\ WF_pc1(M45)
/\ WF_pc1(M56)
/\ WF_pc1(M67)
/\ WF_pc1(M70)

vars == << pc0, pc1, turn, intr0, intr1 >> 
FairSpec ==
/\ Init
/\ [] [Next]_vars
/\ Fairness


MUTUAL_EXCLUSION == [] ~((pc0 = 5) /\ (pc1 = 5))

NOSTARVE_1 == [] ((pc0 = 4) => <> (pc0 = 5))
NOSTARVE_2 == [] ((pc1 = 4) => <> (pc1 = 5))

CRIT_0 == (pc0 = 5)
CRIT_1 == (pc1 = 5)

\* STRICT_SEQUENCING_1 = 
\* [] (CRIT_0 => (CRIT_0) W (~(CRIT_0 /\ (~CRIT_0 W CRIT_1))
\* TLA doesn't have until operator


=============================================================================
\* Modification History
\* Last modified Tue Mar 05 17:28:48 IST 2024 by neeraj
\* Created Tue Mar 05 17:17:01 IST 2024 by neeraj
