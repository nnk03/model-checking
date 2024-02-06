---------------------------- MODULE jugs_problem ----------------------------

EXTENDS Integers

VARIABLES small, big

TypeOK ==
    /\ small \in 0..3
    /\ big \in 0..3
   
Init == 
    /\ big = 0
    /\ small = 0

FillSmall == 
    /\ small' = 3
    /\ big' = big

FillBig == 
    /\ big' = 5
    /\ small' = small

EmptySmall ==
    /\ small' = 0
    /\ big' = big

EmptyBig == 
    /\ big' = 0
    /\ small' = small

SmallToBig == 
    IF big + small =< 5
        THEN /\ big' = big + small
             /\ small' = 0
        ELSE /\ small' = small - (5 - big)
             /\ big' = 5
        

BigToSmall == 
    IF big + small =< 3
        THEN /\ big' = 0
             /\ small' = big + small
        ELSE /\ big' = small - (3 - big)
             /\ small' = 3

Next ==
    \/ FillSmall
    \/ FillBig
    \/ EmptySmall
    \/ EmptyBig
    \/ SmallToBig
    \/ BigToSmall



=============================================================================
\* Modification History
\* Last modified Tue Jan 30 15:37:34 IST 2024 by neerajkrishnan
\* Created Tue Jan 30 14:47:17 IST 2024 by neerajkrishnan
