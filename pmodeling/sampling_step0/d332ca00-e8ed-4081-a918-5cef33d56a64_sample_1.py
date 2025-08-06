from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake = Transition(label='Intake Document')
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
root = StrictPartialOrder()

# Define the workflow structure
root.nodes.append(intake)
root.nodes.append(visual_inspect)
root.nodes.append(imaging_scan)
root.nodes.append(material_test)
root.nodes.append(database_cross)
root.nodes.append(provenance_check)
root.nodes.append(expert_consult)
root.nodes.append(carbon_dating)
root.nodes.append(forensic_analyze)
root.nodes.append(anomaly_review)
root.nodes.append(risk_assess)
root.nodes.append(report_draft)
root.nodes.append(insurance_quote)
root.nodes.append(storage_plan)
root.nodes.append(final_approval)

# Define the dependencies between nodes
root.order.add_edge(intake, visual_inspect)
root.order.add_edge(intake, imaging_scan)
root.order.add_edge(intake, material_test)
root.order.add_edge(intake, provenance_check)
root.order.add_edge(visual_inspect, database_cross)
root.order.add_edge(imaging_scan, database_cross)
root.order.add_edge(material_test, database_cross)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(expert_consult, carbon_dating)
root.order.add_edge(carbon_dating, forensic_analyze)
root.order.add_edge(forensic_analyze, anomaly_review)
root.order.add_edge(anomaly_review, risk_assess)
root.order.add_edge(risk_assess, report_draft)
root.order.add_edge(report_draft, insurance_quote)
root.order.add_edge(insurance_quote, storage_plan)
root.order.add_edge(storage_plan, final_approval)