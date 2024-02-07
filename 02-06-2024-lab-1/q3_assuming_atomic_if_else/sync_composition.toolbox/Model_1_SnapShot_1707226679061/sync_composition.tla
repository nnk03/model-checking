-------------------------- MODULE sync_composition --------------------------

(*
Initially
Light1 = Red
Light2 = Green
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
Check if light 1 has color green and light 2 has color green can ever occur in the synchronous
composition of these systems

In your model assume that if there is a slog (stutter), both lights stutter together
(By default, such a transition is assumed in TLA+)

*)

EXTENDS Integers
VARIABLES pc0, pc1, l1, l2, counter

(* 0 denotes red and 1 denotes green for lights *)
(* 
variables for LIGHT 1 is pc0, l1, counter
variables for LIGHT 2 is pc1, l2, counter
*)


TypeOK == 
/\ l1 \in {0, 1}
/\ l2 \in {0, 1}
/\ counter \in 0..20


Init == 
/\ l1 = 0
/\ l2 = 1
/\ counter = 20

P01 == 
/\ pc0 = 0
/\ pc0' = 1
/\ UNCHANGED << l1, counter >>

P12 ==
/\ IF counter = 0
    THEN /\ l1' = 1 - l1
         /\ counter' = 20
    ELSE /\ counter' = counter - 1
         /\ UNCHANGED l1
/\ pc0 = 1
/\ pc0' = 2

P23 ==
/\ pc0 = 2
/\ pc0' = 3
/\ UNCHANGED << counter, l2 >>

Next1 ==
\/ P01
\/ P12
\/ P23

Q01 == 
/\ pc1 = 0
/\ pc1' = 1
/\ UNCHANGED << l2, counter >>

Q12 ==
/\ IF counter = 0
    THEN /\ l2' = 1 - l2
         /\ counter' = 20
    ELSE /\ counter' = counter - 1
         /\ UNCHANGED l2
/\ pc1 = 1
/\ pc1' = 2

Q23 ==
/\ pc1 = 2
/\ pc1' = 3
/\ UNCHANGED << counter, l2 >>

Next2 ==
\/ Q01
\/ Q12
\/ Q23

SLOG_TOGETHER == UNCHANGED << pc0, pc1, l1, l2, counter >>

\* since it's synchronous composition
Next == (Next1 /\ Next2) \/ SLOG_TOGETHER

Both_Green == 
/\ l1 = 1
/\ l2 = 1




















=============================================================================
\* Modification History
\* Last modified Tue Feb 06 19:07:48 IST 2024 by neeraj
\* Created Tue Feb 06 18:18:16 IST 2024 by neeraj
