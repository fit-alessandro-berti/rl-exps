import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
intake = Transition(label='Intake Document')
inspect = Transition(label='Visual Inspect')
image_scan = Transition(label='Imaging Scan')
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

# Define the loop for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, expert_consult])

# Define the exclusive choice for the process
xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[intake, inspect, image_scan, material_test, database_cross, loop, xor, carbon_dating, forensic_analyze, anomaly_review, risk_assess, report_draft, insurance_quote, storage_plan, final_approval])
root.order.add_edge(intake, inspect)
root.order.add_edge(inspect, image_scan)
root.order.add_edge(image_scan, material_test)
root.order.add_edge(material_test, database_cross)
root.order.add_edge(database_cross, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, risk_assess)
root.order.add_edge(risk_assess, report_draft)
root.order.add_edge(report_draft, insurance_quote)
root.order.add_edge(insurance_quote, storage_plan)
root.order.add_edge(storage_plan, final_approval)

print(root)