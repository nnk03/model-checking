------------------------ MODULE sequential_circuits ------------------------
\* synchronous composition of sequential circuits

(*

for i = 0

r_i' = r_i /\ x_i

y_i' = x_i \/ ~(r_i)

for i = 1
r1' = x1 \/ r1
y1' = x1 /\ r1


Initially r0 = 0, r1 = 1, x0 \in {0, 1}, x1 \in {0, 1}


*)

EXTENDS Integers

VARIABLES r0, r1, x0, x1

Y0 == x0 \/ (~(r0))
Y1 == x1 /\ r1

Init0 ==
/\ r0 = FALSE
/\ (x0 = FALSE \/ x0 = TRUE)

Init1 ==
/\ r1 = TRUE
/\ (x1 = FALSE \/ x1 = TRUE)

Init == Init0 /\ Init1

Next0 ==
/\ (r0' = (r0 /\ x0))
/\ x0' \in {FALSE, TRUE}

Next1 ==
/\ (r1' = (x1 \/ r1))
/\ x1' \in {FALSE, TRUE}

SLOG_TOGETHER == UNCHANGED << r0, r1, x0, x1>>

Next == (Next0 /\ Next1) \/ SLOG_TOGETHER





















=============================================================================
\* Modification History
\* Last modified Tue Feb 13 19:04:21 IST 2024 by neeraj
\* Created Tue Feb 13 17:38:03 IST 2024 by neeraj
