import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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
loop_check_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, expert_consult])
xor_database = OperatorPOWL(operator=Operator.XOR, children=[database_cross, skip])
xor_anomaly = OperatorPOWL(operator=Operator.XOR, children=[anomaly_review, skip])
xor_insurance = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, skip])
xor_storage = OperatorPOWL(operator=Operator.XOR, children=[storage_plan, skip])
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[intake_document, visual_inspect, imaging_scan, material_test, loop_check_provenance, xor_database, xor_anomaly, xor_insurance, xor_storage, xor_final])
root.order.add_edge(intake_document, visual_inspect)
root.order.add_edge(visual_inspect, imaging_scan)
root.order.add_edge(imaging_scan, material_test)
root.order.add_edge(material_test, provenance_check)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(expert_consult, carbon_dating)
root.order.add_edge(carbon_dating, forensic_analyze)
root.order.add_edge(forensic_analyze, anomaly_review)
root.order.add_edge(anomaly_review, insurance_quote)
root.order.add_edge(insurance_quote, storage_plan)
root.order.add_edge(storage_plan, final_approval)
root.order.add_edge(final_approval, report_draft)

# Print the POWL model
print(root)