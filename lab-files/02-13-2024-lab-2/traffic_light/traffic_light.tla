--------------------------- MODULE traffic_light ---------------------------

(*
Initially
Light0 = Red
Light1 = Green
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
8 : }
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
variables for LIGHT 0 is pc0, l1, counter ;
variables for LIGHT 1 is pc1, l2, counter
*)

(*
possible transitions
01
12
16
23
38
68
80
*)

Init0 == (pc0 = 0) /\ (l0 = 0)
Init1 == (pc1 = 0) /\ (l1 = 1)

Init == Init0 /\ Init1 /\ (counter = 20)

L01 == 
/\ pc0 = 0
/\ pc0' = 1
/\ UNCHANGED << l0, counter >>

L12 ==
/\ pc0 = 1
/\ pc0' = 2
/\ counter = 0
/\ UNCHANGED << l0, counter >>

L16 ==
/\ pc0 = 1
/\ pc0' = 6
/\ counter # 0
/\ UNCHANGED << l0, counter >>

L23 ==
/\ pc0 = 2
/\ pc0' = 3
/\ l0' = 1 - l0
/\ UNCHANGED << counter >>

L38 ==
/\ pc0 = 3
/\ pc0' = 8
/\ counter' = 20
/\ UNCHANGED << l0 >>

L68 ==
/\ pc0 = 6
/\ pc0' = 8
/\ counter' = counter - 1
/\ UNCHANGED << l0 >>

L80 ==
/\ pc0 = 8
/\ pc0' = 0
/\ UNCHANGED << l0, counter >>

Next0 ==
\/ L01
\/ L12
\/ L16
\/ L23
\/ L38
\/ L68
\/ L80

M01 == 
/\ pc1 = 0
/\ pc1' = 1
/\ UNCHANGED << l1, counter >>

M12 ==
/\ pc1 = 1
/\ pc1' = 2
/\ counter = 0
/\ UNCHANGED << l1, counter >>

M16 ==
/\ pc1 = 1
/\ pc1' = 6
/\ counter # 0
/\ UNCHANGED << l1, counter >>

M23 ==
/\ pc1 = 2
/\ pc1' = 3
/\ l1' = 1 - l1
/\ UNCHANGED << counter >>

M38 ==
/\ pc1 = 3
/\ pc1' = 8
/\ counter' = 20
/\ UNCHANGED << l1 >>

M68 ==
/\ pc1 = 6
/\ pc1' = 8
/\ counter' = counter - 1
/\ UNCHANGED << l1 >>

M80 ==
/\ pc1 = 8
/\ pc1' = 0
/\ UNCHANGED << l1, counter >>

Next1 ==
\/ M01
\/ M12
\/ M16
\/ M23
\/ M38
\/ M68
\/ M80


SLOG_TOGETHER == UNCHANGED << pc0, pc1, l0, l1, counter >>

Next == (Next0 /\ Next1) \/ SLOG_TOGETHER

Both_Not_Green == ~((l0 = 1) /\ (l1 = 1))














=============================================================================
\* Modification History
\* Last modified Tue Feb 13 18:14:31 IST 2024 by neeraj
\* Created Tue Feb 13 17:11:41 IST 2024 by neeraj
