-------------------------------- MODULE sema --------------------------------


(*

sema - available initially

for process 1 and 2

0 : while(true){
1 :     // Non-critical section
2 :     Request(sema)
3 :     // Critical section
4 :     Release(sema)
5 : }

Request(sema){
    while(True){
        if(sema == available){
            sema = busy;
            break;
        }
    }

// if statement till break is atomic

Release(sema){
    sema = available
}

*)

EXTENDS Integers
VARIABLES s0, s1, sema

Init0 ==
/\ sema = "available"
/\ s0 = 0

Init1 ==
/\ sema = "available"
/\ s1 = 1

Init == Init0 /\ Init1

P01 ==
/\ s0 = 0
/\ s0' = 1
/\ UNCHANGED sema

P12 ==
/\ s0 = 1
/\ s0' = 2
/\ UNCHANGED sema

P22 ==
/\ s0 = 2
/\ s0' = 2
/\ sema = "busy"
/\ sema' = "busy"

P23 ==
/\ s0 = 2
/\ s0' = 3
/\ sema = "available"
/\ sema = "busy"

P34 ==
/\ s0 = 3
/\ s0' = 4
/\ UNCHANGED sema

P45 ==
/\ s0 = 4
/\ s0' = 5
/\ sema' = "available"

P50 ==
/\ s0 = 5
/\ s0' = 5
/\ UNCHANGED sema

Next0 ==
\/ P01
\/ P12
\/ P22
\/ P23
\/ P34
\/ P45
\/ P50

Q01 ==
/\ s1 = 0
/\ s1' = 1
/\ UNCHANGED sema

Q12 ==
/\ s1 = 1
/\ s1' = 2
/\ UNCHANGED sema

Q22 ==
/\ s1 = 2
/\ s1' = 2
/\ sema = "busy"
/\ sema' = "busy"

Q23 ==
/\ s1 = 2
/\ s1' = 3
/\ sema = "available"
/\ sema = "busy"

Q34 ==
/\ s1 = 3
/\ s1' = 4
/\ UNCHANGED sema

Q45 ==
/\ s1 = 4
/\ s1' = 5
/\ sema' = "available"

Q50 ==
/\ s1 = 5
/\ s1' = 5
/\ UNCHANGED sema

Next1 ==
\/ Q01
\/ Q12
\/ Q22
\/ Q23
\/ Q34
\/ Q45
\/ Q50

SLOGP == UNCHANGED s0 
SLOGQ == UNCHANGED s1

Next == (Next0 /\ UNCHANGED s1) \/ (Next1 /\ UNCHANGED s0) \/ SLOGP \/ SLOGQ

\* Video 9 for Justice conditions
\* The terminology in the video is, Weak Fairness (in TLA+ world, not exactly Justice Conditions)

\* Justice conditions

J == 
/\ ~(s0 = 0)
/\ ~(s0 = 3)
/\ ~(s0 = 4)
/\ ~(s0 = 5)
/\ ~(s1 = 0)
/\ ~(s1 = 3)
/\ ~(s1 = 4)
/\ ~(s1 = 5)
/\ ~(s0 = 2 /\ sema = "available")
/\ ~(s1 = 2 /\ sema = "available")

\* but the problem with this is bounded weight need not be satisfied only with the first 10 justice conditions
\* ie, one process can starve even if we assume fair scheduler

\* hence we need compassion conditions


P0 == s0 = 2 /\ sema = "available"
Q0 == s0 # 2

P1 == s1 = 2 /\ sema = "available"
Q1 == s1 # 2

\* with this compassion condition, we can show no starvation occurs
\* i.e if P0 wants to enter critical section ( i.e it performs request(sema), then 
\* eventually, P0 will be allowed in critical section

\* Similarly for P1


















=============================================================================
\* Modification History
\* Last modified Mon Feb 05 11:40:10 IST 2024 by neerajkrishnan
\* Created Fri Feb 02 11:35:21 IST 2024 by neerajkrishnan
