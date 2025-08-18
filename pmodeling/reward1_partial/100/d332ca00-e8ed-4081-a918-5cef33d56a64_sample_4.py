import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
intake_document = Transition(label='Intake Document')
visual_inspect = Transition(label='Visual Inspect')
imaging_scan = Transition(label='Imaging Scan')
material_test = Transition(label='Material Test')
database_cross = Transition(label='Database Cross')
provenance_check = Transition(label='Provenance Check')
expert_consult = Transition(label='Expert Consult')
carbon_dating = Transition(label='Carbon Dating')
forensic_analyze = Transition(label='Forensic Analyze')
anomaly_review = Transition(label='Anomaly Review')
risk_assess = Transition(label='Risk Assess')
report_draft = Transition(label='Report Draft')
insurance_quote = Transition(label='Insurance Quote')
storage_plan = Transition(label='Storage Plan')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[visual_inspect, imaging_scan, material_test, database_cross, provenance_check, expert_consult])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating, forensic_analyze, anomaly_review])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, storage_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Connect the nodes
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop2, xor3)

# Print the root
print(root)