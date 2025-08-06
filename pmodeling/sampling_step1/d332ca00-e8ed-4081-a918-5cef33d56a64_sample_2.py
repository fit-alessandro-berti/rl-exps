import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
choice = OperatorPOWL(operator=Operator.XOR, children=[intake_document, visual_inspect])
non_invasive = OperatorPOWL(operator=Operator.LOOP, children=[imaging_scan, material_test])
cross_check = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, expert_consult])
carbon = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating, forensic_analyze])
anomaly = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_review, risk_assess])
risk = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote])
storage = OperatorPOWL(operator=Operator.LOOP, children=[storage_plan, final_approval])

# Define root POWL model
root = StrictPartialOrder(nodes=[choice, non_invasive, cross_check, carbon, anomaly, risk, storage])
root.order.add_edge(choice, non_invasive)
root.order.add_edge(non_invasive, cross_check)
root.order.add_edge(cross_check, carbon)
root.order.add_edge(carbon, anomaly)
root.order.add_edge(anomaly, risk)
root.order.add_edge(risk, storage)