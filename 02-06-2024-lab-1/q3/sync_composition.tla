-------------------------- MODULE sync_composition --------------------------

(*
Initially
Light1 = Red
Light2 = Green
Counter = 20

Light i
0 : while(True){
1 :     if(counter == 0){
2 :         flip color of Light i
3 :         Set Counter to 20
4 :     }
5 :     else {
6 :         decrement counter
7 :     }

Check if light 1 has color green and light 2 has color green can ever occur in the synchronous
composition of these systems

In your model assume that if there is a slog (stutter), both lights stutter together
(By default, such a transition is assumed in TLA+)

*)

EXTENDS Integers
VARIABLES pc0, pc1, l1, l2, counter

(* 0 denotes red and 1 denotes green for lights *)

TypeOK == 
/\ l1 \in {0, 1}
/\ l2 \in {0, 1}
/\ counter \in 0..20


Init == 
/\ l1 = "red"
/\ l2 = "green"
/\ counter = 20

\*P01 == 
\*/\ pc0 = 0
\*/\ pc0' = 1
\*/\ IF counter = 0
\*    THEN /\ 





















=============================================================================
\* Modification History
\* Last modified Tue Feb 06 18:33:07 IST 2024 by neeraj
\* Created Tue Feb 06 18:18:16 IST 2024 by neeraj
