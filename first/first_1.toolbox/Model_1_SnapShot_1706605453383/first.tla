------------------------------- MODULE first -------------------------------


EXTENDS Integers

VARIABLES i, pc

Init == (pc = "start") /\ (i = 0)

Pick == \/  /\ pc = "start"
            /\ i' \in 0..1000
            /\ pc' = "middle"
Add1 == 
    \/  /\ pc = "middle"
        /\ i' = i + 1
        /\ pc' = "done"
        
Next == Pick \/ Add1



=============================================================================
\* Modification History
\* Last modified Tue Jan 30 14:30:51 IST 2024 by neerajkrishnan
\* Created Tue Jan 30 00:36:08 IST 2024 by neerajkrishnan



