from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Intake_Document = Transition(label='Intake Document')
Visual_Inspect = Transition(label='Visual Inspect')
Imaging_Scan = Transition(label='Imaging Scan')
Material_Test = Transition(label='Material Test')
Database_Cross = Transition(label='Database Cross')
Provenance_Check = Transition(label='Provenance Check')
Expert_Consult = Transition(label='Expert Consult')
Carbon_Dating = Transition(label='Carbon Dating')
Forensic_Analyze = Transition(label='Forensic Analyze')
Anomaly_Review = Transition(label='Anomaly Review')
Risk_Assess = Transition(label='Risk Assess')
Report_Draft = Transition(label='Report Draft')
Insurance_Quote = Transition(label='Insurance Quote')
Storage_Plan = Transition(label='Storage Plan')
Final_Approval = Transition(label='Final Approval')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define partial order for the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Visual_Inspect, Imaging_Scan, Material_Test])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Database_Cross, Provenance_Check, Expert_Consult])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Carbon_Dating, Forensic_Analyze])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Anomaly_Review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Report_Draft, Insurance_Quote])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Storage_Plan, Final_Approval])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)