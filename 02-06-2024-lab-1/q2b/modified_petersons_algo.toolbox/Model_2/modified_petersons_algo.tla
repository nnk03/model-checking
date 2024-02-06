---------------------- MODULE modified_petersons_algo ----------------------

EXTENDS Integers

VARIABLES pc0, pc1, turn, intr0, intr1

TypeOK == 
/\ pc0 \in 0..7
/\ pc1 \in 0..7
/\ turn \in {0, 1}
/\ intr0 \in {TRUE, FALSE}
/\ intr1 \in {TRUE, FALSE}


(*
Change the algo so that in P0, Replace turn = 1 by turn = 0
and in P1, replace turn = 0 by turn = 1
and again check for mutual exclusion principle


asynchronous system

for i = 0, 1

the algorithm is

0 : while(True){
1 :     // non critical section
2 :     intr[i] = True
3 :     turn = i // MODIFIED
4 :     while(turn == 1 and intr[1 - i] == 1) // wait
5 :     // critical section
6 :     intr[i] = 0
7 : }


*)

Init0 ==
/\ turn = 0
/\ intr0 = FALSE
/\ pc0 = 0

Init1 ==
/\ turn = 0
/\ intr1 = FALSE
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
/\ intr0' = TRUE
/\ UNCHANGED << intr1, turn >>

L34 ==
/\ pc0 = 3
/\ pc0' = 4
/\ turn' = 0
/\ UNCHANGED << intr0, intr1 >>

L44 ==
/\ pc0 = 4
/\ pc0' = 4
/\ turn = 1
\*/\ turn' = 1
/\ intr1 = TRUE
\*/\ intr1' = TRUE
/\ UNCHANGED intr0

L45 ==
/\ pc0 = 4
/\ pc0' = 5
/\ (turn = 0 \/ intr1 = FALSE)
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
/\ intr1' = TRUE
/\ UNCHANGED << intr0, turn >>

M34 ==
/\ pc1 = 3
/\ pc1' = 4
/\ turn' = 1
/\ UNCHANGED << intr0, intr1 >>

M44 ==
/\ pc1 = 4
/\ pc1' = 4
/\ turn = 0
\*/\ turn' = 0
/\ intr0 = TRUE
\*/\ intr0' = TRUE
/\ UNCHANGED intr1

M45 ==
/\ pc1 = 4
/\ pc1' = 5
/\ (turn = 1 \/ intr0 = FALSE)
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
J04 ==  ~((pc0 = 4) /\ ((turn = 0) \/ (intr1 = FALSE)))
J05 == pc0 # 5
J06 == pc0 # 6
J07 == pc0 # 7

\* for the process 1

J10 == pc1 # 0
J12 == pc1 # 2
J13 == pc1 # 3

J14 ==  ~((pc1 = 4) /\ ((turn = 0) \/ (intr0 = FALSE)))
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



=============================================================================
\* Modification History
\* Last modified Tue Feb 06 17:51:40 IST 2024 by neeraj
\* Created Tue Feb 06 17:27:29 IST 2024 by neeraj
