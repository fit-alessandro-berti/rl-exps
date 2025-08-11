import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, expert_consult])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[imaging_scan, material_test])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[forensic_analyze, xor1])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_review, xor2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, insurance_quote])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[storage_plan, final_approval])

# Create the root POWL model
root = StrictPartialOrder(nodes=[intake_document, visual_inspect, loop1, loop2, xor3, loop3, xor4, loop4])
root.order.add_edge(intake_document, loop1)
root.order.add_edge(intake_document, loop2)
root.order.add_edge(loop1, provenance_check)
root.order.add_edge(loop1, expert_consult)
root.order.add_edge(loop2, imaging_scan)
root.order.add_edge(loop2, material_test)
root.order.add_edge(xor3, risk_assess)
root.order.add_edge(xor3, skip)
root.order.add_edge(loop3, anomaly_review)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor2, carbon_dating)
root.order.add_edge(xor2, skip)
root.order.add_edge(xor4, report_draft)
root.order.add_edge(xor4, insurance_quote)
root.order.add_edge(loop4, storage_plan)
root.order.add_edge(loop4, final_approval)

# Print the root POWL model
print(root)