--------------------- MODULE three_process_asynchronous ---------------------

(*
Initially x = 0

3 process P_i i \in {0, 1, 2}


for process Pi

0 : for k_i = 1; k_i <= 10; ++k_i {
1 :     r_i <- x
2 :     r_i <- r_i + 1
3 :     x <- r_i
4 : }
5 : DONE


Check if it is possible that after all three programs have exited the loop,
value of x is 2

*)


EXTENDS Integers

VARIABLE k0, k1, k2, pc0, pc1, pc2, r0, r1, r2, x

Init0 ==
/\ k0 = 1
/\ pc0 = 0
/\ r0 = 0

Init1 ==
/\ k1 = 1
/\ pc1 = 0
/\ r1 = 0

Init2 ==
/\ k2 = 1
/\ pc2 = 0
/\ r2 = 0

Init == Init0 /\ Init1 /\ Init2 /\ (x = 0)

A01 ==
/\ k0 =< 5
/\ pc0 = 0
/\ pc0' = 1
/\ UNCHANGED << k0, r0, x >>

A12 ==
/\ pc0 = 1
/\ pc0' = 2
/\ r0' = x
/\ UNCHANGED << k0, x >>

A23 == 
/\ pc0 = 2
/\ pc0' = 3
/\ r0' = r0 + 1
/\ UNCHANGED << k0, x >>

A34 ==
/\ pc0 = 3
/\ pc0' = 4
/\ x' = r0
/\ UNCHANGED << r0, k0 >>

A40 ==
/\ k0 # 5
/\ pc0 = 4
/\ pc0' = 0
/\ k0' = k0 + 1
/\ UNCHANGED << r0, x >>

A45 == 
/\ k0 = 5
/\ k0' = 6
/\ pc0 = 4
/\ pc0' = 5
/\ UNCHANGED << r0, x >>

SLOG_A == UNCHANGED << r0, pc0, k0, x >>


B01 ==
/\ k1 =< 5
/\ pc1 = 0
/\ pc1' = 1
/\ UNCHANGED << k1, r1, x >>

B12 ==
/\ pc1 = 1
/\ pc1' = 2
/\ r1' = x
/\ UNCHANGED << k1, x >>

B23 == 
/\ pc1 = 2
/\ pc1' = 3
/\ r1' = r1 + 1
/\ UNCHANGED << k1, x >>

B34 ==
/\ pc1 = 3
/\ pc1' = 4
/\ x' = r1
/\ UNCHANGED << r1, k1 >>

B40 ==
/\ k1 # 5
/\ pc1 = 4
/\ pc1' = 0
/\ k1' = k1 + 1
/\ UNCHANGED << r1, x >>

B45 == 
/\ k1 = 5
/\ k1' = 6
/\ pc1 = 4
/\ pc1' = 5
/\ UNCHANGED << r1, x >>

SLOG_B == UNCHANGED << r1, pc1, k1, x >>


C01 ==
/\ k2 =< 5
/\ pc2 = 0
/\ pc2' = 1
/\ UNCHANGED << k2, r2, x >>

C12 ==
/\ pc2 = 1
/\ pc2' = 2
/\ r2' = x
/\ UNCHANGED << k2, x >>

C23 == 
/\ pc2 = 2
/\ pc2' = 3
/\ r2' = r2 + 1
/\ UNCHANGED << k2, x >>

C34 ==
/\ pc2 = 3
/\ pc2' = 4
/\ x' = r2
/\ UNCHANGED << r2, k2 >>

C40 ==
/\ k2 # 5
/\ pc2 = 4
/\ pc2' = 0
/\ k2' = k2 + 1
/\ UNCHANGED << r2, x >>

C45 == 
/\ k2 = 5
/\ k2' = 6
/\ pc2 = 4
/\ pc2' = 5
/\ UNCHANGED << r2, x >>

SLOG_C == UNCHANGED << r2, pc2, k2, x >>

NextA ==
\/ A01
\/ A12
\/ A23
\/ A34
\/ A40
\/ A45
\*\/ SLOG_A

NextB ==
\/ B01
\/ B12
\/ B23
\/ B34
\/ B40
\/ B45
\*\/ SLOG_B


NextC ==
\/ C01
\/ C12
\/ C23
\/ C34
\/ C40
\/ C45
\*\/ SLOG_C

Next == 
\/ (NextA /\ UNCHANGED << pc1, pc2, k1, k2, r1, r2 >>)
\/ (NextB /\ UNCHANGED << pc0, pc2, k0, k2, r0, r2 >>)
\/ (NextC /\ UNCHANGED << pc0, pc1, k0, k1, r0, r1 >>)





CHECK ==
<>(k0 = 6
/\ k1 = 6
/\ k2 = 6
/\ x = 2)























=============================================================================
\* Modification History
\* Last modified Tue Feb 13 19:24:32 IST 2024 by neeraj
\* Created Tue Feb 13 17:43:15 IST 2024 by neeraj
