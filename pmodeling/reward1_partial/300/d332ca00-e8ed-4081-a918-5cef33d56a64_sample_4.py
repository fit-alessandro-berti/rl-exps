import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
intake_doc = Transition(label='Intake Document')
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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[visual_inspect, imaging_scan, material_test, provenance_check, expert_consult, carbon_dating, forensic_analyze])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_review, risk_assess])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, insurance_quote, storage_plan, final_approval])

root = StrictPartialOrder(nodes=[intake_doc, loop1, loop2, xor])
root.order.add_edge(intake_doc, loop1)
root.order.add_edge(intake_doc, loop2)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)

return root