-------------------------- MODULE sync_composition --------------------------

(*
Initially
Light0 = Red
Light1 = Green
Counter = 20

Light i
0 : while(True){
1 :     if(counter == 0){
1 :         flip color of Light i
1 :         Set Counter to 20
1 :     }
2 :     else {
2 :         decrement counter
2 :     }
3 : }
Check if light 0 has color green and light 1 has color green can ever occur in the synchronous
composition of these systems

In your model assume that if there is a slog (stutter), both lights stutter together
(By default, such a transition is assumed in TLA+)

*)

EXTENDS Integers
VARIABLES pc0, pc1, l0, l1, counter

(* 
0 denotes red and 1 denotes green for lights 
*)
(* 
variables for LIGHT 0 is pc0, l1, counter
variables for LIGHT 1 is pc1, l2, counter
*)


TypeOK == 
/\ pc0 \in 0..3
/\ pc1 \in 0..3
/\ l0 \in {0, 1}
/\ l1 \in {0, 1}
/\ counter \in 0..20


Init == 
/\ pc0 = 0
/\ pc1 = 0
/\ l0 = 0
/\ l1 = 1
/\ counter = 20

P01 == 
/\ pc0 = 0
/\ pc0' = 1
/\ UNCHANGED << l0, counter >>

P12 ==
/\ IF counter = 0
    THEN /\ l0' = 1 - l0
         /\ counter' = 20
    ELSE /\ counter' = counter - 1
         /\ UNCHANGED l0
/\ pc0 = 1
/\ pc0' = 2

P23 ==
/\ pc0 = 2
/\ pc0' = 3
/\ UNCHANGED << counter, l0 >>

P30 ==
/\ pc0 = 3
/\ pc0 =  0
/\ UNCHANGED << counter, l0 >>

Next0 ==
\/ P01
\/ P12
\/ P23
\/ P30

Q01 == 
/\ pc1 = 0
/\ pc1' = 1
/\ UNCHANGED << l1, counter >>

Q12 ==
/\ IF counter = 0
    THEN /\ l1' = 1 - l1
         /\ counter' = 20
    ELSE /\ counter' = counter - 1
         /\ UNCHANGED l1
/\ pc1 = 1
/\ pc1' = 2

Q23 ==
/\ pc1 = 2
/\ pc1' = 3
/\ UNCHANGED << counter, l1 >>

Q30 ==
/\ pc1 = 3
/\ pc1 =  0
/\ UNCHANGED << counter, l1 >>

Next1 ==
\/ Q01
\/ Q12
\/ Q23
\/ Q30

SLOG_TOGETHER == UNCHANGED << pc0, pc1, l0, l1, counter >>

\* since it's synchronous composition
Next == (Next0 /\ Next1) \/ SLOG_TOGETHER

Both_Not_Green == ~(l0 = 1 /\ l1 = 1)




















=============================================================================
\* Modification History
\* Last modified Tue Feb 06 19:18:14 IST 2024 by neeraj
\* Created Tue Feb 06 18:18:16 IST 2024 by neeraj
