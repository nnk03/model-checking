--------------------------- MODULE petersons_algo ---------------------------

EXTENDS Integers

VARIABLES pc0, pc1, turn, intr0, intr1

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
\*/\ turn' = turn
\*/\ intr0' = intr0
\*/\ intr1' = intr1

L12 == 
/\ pc0 = 1
/\ pc0' = 2
/\ UNCHANGED << turn, intr0, intr1 >>
\*/\ turn' = turn
\*/\ intr0' = intr0
\*/\ intr1' = intr1

L23 ==
/\ pc0 = 2
/\ pc0' = 3
/\ intr0 = TRUE
/\ UNCHANGED << intr1, turn >>

L34 ==
/\ pc0 = 3
/\ pc0' = 4
/\ turn' = 1
/\ UNCHANGED << intr0, intr1 >>

L44 ==
/\ pc0 = 4
/\ pc0' = 4
/\ turn' = 1
/\ intr1' = TRUE
/\ UNCHANGED intr0

L45 ==
/\ pc0 = 4
/\ pc0' = 5
/\ (turn = 0 \/ intr1 = FALSE)
/\ UNCHANGED intr0

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
\*/\ turn' = turn
\*/\ intr0' = intr0
\*/\ intr1' = intr1

M12 == 
/\ pc1 = 1
/\ pc1' = 2
/\ UNCHANGED << turn, intr0, intr1 >>
\*/\ turn' = turn
\*/\ intr0' = intr0
\*/\ intr1' = intr1

M23 ==
/\ pc1 = 2
/\ pc1' = 3
/\ intr1 = TRUE
/\ UNCHANGED << intr0, turn >>

M34 ==
/\ pc1 = 3
/\ pc1' = 4
/\ turn' = 0
/\ UNCHANGED << intr0, intr1 >>

M44 ==
/\ pc1 = 4
/\ pc1' = 4
/\ turn' = 0
/\ intr0' = TRUE
/\ UNCHANGED intr1

M45 ==
/\ pc1 = 4
/\ pc1' = 5
/\ (turn = 1 \/ intr0 = FALSE)
/\ UNCHANGED intr1

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





=============================================================================
\* Modification History
\* Last modified Tue Jan 30 22:01:22 IST 2024 by neerajkrishnan
\* Created Tue Jan 30 17:52:27 IST 2024 by neerajkrishnan
