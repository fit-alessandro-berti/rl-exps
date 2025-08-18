import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Component_Check = Transition(label='Component Check')
Spec_Review = Transition(label='Spec Review')
Parts_Sorting = Transition(label='Parts Sorting')
Mechanical_Fit = Transition(label='Mechanical Fit')
Firmware_Load = Transition(label='Firmware Load')
Calibration_Run = Transition(label='Calibration Run')
Stress_Test = Transition(label='Stress Test')
Software_Patch = Transition(label='Software Patch')
Algorithm_Tune = Transition(label='Algorithm Tune')
Comms_Setup = Transition(label='Comms Setup')
Validation_Pass = Transition(label='Validation Pass')
Data_Link = Transition(label='Data Link')
Onsite_Deploy = Transition(label='Onsite Deploy')
Live_Monitor = Transition(label='Live Monitor')
Update_Push = Transition(label='Update Push')
Recovery_Plan = Transition(label='Recovery Plan')
Maintenance_Log = Transition(label='Maintenance Log')

# Define the partial order
root = StrictPartialOrder(nodes=[Component_Check, Spec_Review, Parts_Sorting, Mechanical_Fit, Firmware_Load, Calibration_Run, Stress_Test, Software_Patch, Algorithm_Tune, Comms_Setup, Validation_Pass, Data_Link, Onsite_Deploy, Live_Monitor, Update_Push, Recovery_Plan, Maintenance_Log])

# Define the partial order dependencies
root.order.add_edge(Component_Check, Spec_Review)
root.order.add_edge(Spec_Review, Parts_Sorting)
root.order.add_edge(Parts_Sorting, Mechanical_Fit)
root.order.add_edge(Mechanical_Fit, Firmware_Load)
root.order.add_edge(Firmware_Load, Calibration_Run)
root.order.add_edge(Calibration_Run, Stress_Test)
root.order.add_edge(Stress_Test, Software_Patch)
root.order.add_edge(Software_Patch, Algorithm_Tune)
root.order.add_edge(Algorithm_Tune, Comms_Setup)
root.order.add_edge(Comms_Setup, Validation_Pass)
root.order.add_edge(Validation_Pass, Data_Link)
root.order.add_edge(Data_Link, Onsite_Deploy)
root.order.add_edge(Onsite_Deploy, Live_Monitor)
root.order.add_edge(Live_Monitor, Update_Push)
root.order.add_edge(Update_Push, Recovery_Plan)
root.order.add_edge(Recovery_Plan, Maintenance_Log)

print(root)