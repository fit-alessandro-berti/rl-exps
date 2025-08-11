import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop node for imaging and material tests
loop_imaging_material = OperatorPOWL(operator=Operator.LOOP, children=[imaging_scan, material_test])

# Define choice for provenance check and expert consultation
choice_provenance_expert = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, expert_consult])

# Define choice for anomaly review and carbon dating
choice_anomaly_carbon = OperatorPOWL(operator=Operator.XOR, children=[anomaly_review, carbon_dating])

# Define choice for forensic analysis and risk assessment
choice_forensic_risk = OperatorPOWL(operator=Operator.XOR, children=[forensic_analyze, risk_assess])

# Define choice for insurance quote and storage plan
choice_insurance_storage = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, storage_plan])

# Define choice for final approval
choice_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_imaging_material, choice_provenance_expert, choice_anomaly_carbon, choice_forensic_risk, choice_insurance_storage, choice_final_approval])

# Define the order of transitions
root.order.add_edge(loop_imaging_material, choice_provenance_expert)
root.order.add_edge(choice_provenance_expert, choice_anomaly_carbon)
root.order.add_edge(choice_anomaly_carbon, choice_forensic_risk)
root.order.add_edge(choice_forensic_risk, choice_insurance_storage)
root.order.add_edge(choice_insurance_storage, choice_final_approval)

# Print the root POWL model
print(root)