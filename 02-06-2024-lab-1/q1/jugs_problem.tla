---------------------------- MODULE jugs_problem ----------------------------

EXTENDS Integers

VARIABLES small, big

TypeOK ==
    /\ small \in 0..3
    /\ big \in 0..5
   
Init == 
    /\ big = 0
    /\ small = 0

FillSmall == 
    /\ small' = 5
    /\ big' = big

FillBig == 
    /\ big' = 7
    /\ small' = small

EmptySmall ==
    /\ small' = 0
    /\ big' = big

EmptyBig == 
    /\ big' = 0
    /\ small' = small

SmallToBig == 
    IF big + small =< 7
        THEN /\ big' = big + small
             /\ small' = 0
        ELSE /\ small' = small - (7 - big)
             /\ big' = 7
        

BigToSmall == 
    IF big + small =< 5
        THEN /\ big' = 0
             /\ small' = big + small
        ELSE /\ big' = small - (5 - big)
             /\ small' = 5

Next ==
    \/ FillSmall
    \/ FillBig
    \/ EmptySmall
    \/ EmptyBig
    \/ SmallToBig
    \/ BigToSmall

\* We need 6 gallons in one jug, is it possible
NegReq == big # 6



=============================================================================
\* Modification History
\* Last modified Tue Feb 06 17:15:32 IST 2024 by neeraj
\* Last modified Tue Jan 30 15:38:12 IST 2024 by neerajkrishnan
\* Created Tue Jan 30 14:47:17 IST 2024 by neerajkrishnan
