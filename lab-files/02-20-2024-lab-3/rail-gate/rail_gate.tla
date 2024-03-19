----------------------------- MODULE rail_gate -----------------------------

EXTENDS Integers

VARIABLES gate, train, controller

(*

Gate_<transition> {gate}
Train_<transition> {train}
Controller_<transition> {controller}



*)

TypeOK ==
/\ gate \in {"up", "down"}
/\ train \in {"far", "near", "in"}
/\ controller \in {0..3}

Init_gate == gate = "up"

Init_train == train = "far"

Init_controller == controller = 0

Init == Init_gate /\ Init_train /\ Init_controller

Gate_Lower == 
/\ gate = "up"
/\ gate' = "down"
\*Gate_Lower ==
\*IF gate = "up" THEN gate' = "down"
\*ELSE UNCHANGED << gate >>

Gate_Raise ==
/\ gate = "down"
/\ gate' = "up"
\*Gate_Raise ==
\*IF gate = "down" THEN gate' = "up"
\*ELSE UNCHANGED << gate >>

Train_Approach ==
/\ train = "far"
/\ train' = "near"
\*Train_Approach ==
\*IF train = "far" THEN train' = "near"
\*ELSE UNCHANGED train

Train_Enter ==
/\ train = "near"
/\ train' = "in"
\*Train_Enter ==
\*IF train = "near" THEN train' = "in"
\*ELSE UNCHANGED train

Train_Exit ==
/\ train = "in"
/\ train' = "far"
\*Train_Exit ==
\*IF train = "in" THEN train' = "far"
\*ELSE UNCHANGED train

Controller_Approach ==
/\ controller = 0
/\ controller' = 1
\*Controller_Approach ==
\*IF controller = 0 THEN controller' = 1
\*ELSE UNCHANGED controller

Controller_Lower ==
/\ controller = 1
/\ controller' = 2
\*Controller_Lower ==
\*IF controller = 1 THEN controller' = 2
\*ELSE UNCHANGED controller

Controller_Exit ==
/\ controller = 2
/\ controller' = 3
\*Controller_Exit ==
\*IF controller = 2 THEN controller' = 3
\*ELSE UNCHANGED controller

Controller_Raise ==
/\ controller = 3
/\ controller' = 0
\*Controller_Raise ==
\*IF controller = 3 THEN controller' = 0
\*ELSE UNCHANGED controller

Next_Lower ==
/\ Gate_Lower
/\ Controller_Lower
/\ UNCHANGED train

Next_Raise ==
/\ Gate_Raise
/\ Controller_Raise
/\ UNCHANGED train

Next_Exit ==
/\ Train_Exit
/\ Controller_Exit
/\ UNCHANGED gate

Next_Enter ==
/\ Train_Enter
/\ UNCHANGED << gate, controller >>

Next_Approach ==
/\ Train_Approach
/\ Controller_Approach
/\ UNCHANGED << gate >> 

Next ==
\/ Next_Lower
\/ Next_Raise
\/ Next_Enter
\/ Next_Exit
\/ Next_Approach


Check_Collision ==
~(train = "in" /\ gate = "up")

Check_Reachable ==
~(train = "far" /\ controller = 2 /\ gate = "down")












=============================================================================
\* Modification History
\* Last modified Tue Mar 05 17:21:43 IST 2024 by neeraj
\* Created Tue Feb 20 17:26:17 IST 2024 by neeraj
