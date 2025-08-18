import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Initial_Assess = Transition(label='Initial Assess')
Artifact_Scan = Transition(label='Artifact Scan')
Condition_Map = Transition(label='Condition Map')
Material_Test = Transition(label='Material Test')
Cleaning_Phase = Transition(label='Cleaning Phase')
Stability_Check = Transition(label='Stability Check')
Minor_Repair = Transition(label='Minor Repair')
Structural_Reinforce = Transition(label='Structural Reinforce')
Surface_Restore = Transition(label='Surface Restore')
Coating_Apply = Transition(label='Coating Apply')
Ethics_Review = Transition(label='Ethics Review')
Provenance_Verify = Transition(label='Provenance Verify')
Client_Update = Transition(label='Client Update')
Final_Report = Transition(label='Final Report')
Archive_Store = Transition(label='Archive Store')

# Define partial order
root = StrictPartialOrder(nodes=[Initial_Assess, Artifact_Scan, Condition_Map, Material_Test, Cleaning_Phase, Stability_Check, Minor_Repair, Structural_Reinforce, Surface_Restore, Coating_Apply, Ethics_Review, Provenance_Verify, Client_Update, Final_Report, Archive_Store])

# Define dependencies
root.order.add_edge(Initial_Assess, Artifact_Scan)
root.order.add_edge(Artifact_Scan, Condition_Map)
root.order.add_edge(Condition_Map, Material_Test)
root.order.add_edge(Material_Test, Cleaning_Phase)
root.order.add_edge(Cleaning_Phase, Stability_Check)
root.order.add_edge(Stability_Check, Minor_Repair)
root.order.add_edge(Minor_Repair, Structural_Reinforce)
root.order.add_edge(Structural_Reinforce, Surface_Restore)
root.order.add_edge(Surface_Restore, Coating_Apply)
root.order.add_edge(Coating_Apply, Ethics_Review)
root.order.add_edge(Ethics_Review, Provenance_Verify)
root.order.add_edge(Provenance_Verify, Client_Update)
root.order.add_edge(Client_Update, Final_Report)
root.order.add_edge(Final_Report, Archive_Store)

# Print the root
print(root)