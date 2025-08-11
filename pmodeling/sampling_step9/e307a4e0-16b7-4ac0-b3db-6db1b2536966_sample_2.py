import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Initial_Assess, Artifact_Scan, Condition_Map, Material_Test, Cleaning_Phase, Stability_Check, Minor_Repair, Structural_Reinforce, Surface_Restore, Coating_Apply, Ethics_Review, Provenance_Verify, Client_Update, Final_Report, Archive_Store])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)