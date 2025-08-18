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
loop_imaging = OperatorPOWL(operator=Operator.LOOP, children=[imaging_scan])
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_test])
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
loop_expert = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult])
loop_forensic = OperatorPOWL(operator=Operator.LOOP, children=[forensic_analyze])
loop_anomaly = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_review])
loop_risk = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess])
loop_report = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
loop_insurance = OperatorPOWL(operator=Operator.LOOP, children=[insurance_quote])
loop_storage = OperatorPOWL(operator=Operator.LOOP, children=[storage_plan])
loop_final = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])

root = StrictPartialOrder(nodes=[
    intake_document,
    visual_inspect,
    loop_imaging,
    loop_material,
    loop_provenance,
    loop_expert,
    loop_forensic,
    loop_anomaly,
    loop_risk,
    loop_report,
    loop_insurance,
    loop_storage,
    loop_final
])

# Define the order of execution
root.order.add_edge(intake_document, visual_inspect)
root.order.add_edge(visual_inspect, loop_imaging)
root.order.add_edge(loop_imaging, loop_material)
root.order.add_edge(loop_material, loop_provenance)
root.order.add_edge(loop_provenance, loop_expert)
root.order.add_edge(loop_expert, loop_forensic)
root.order.add_edge(loop_forensic, loop_anomaly)
root.order.add_edge(loop_anomaly, loop_risk)
root.order.add_edge(loop_risk, loop_report)
root.order.add_edge(loop_report, loop_insurance)
root.order.add_edge(loop_insurance, loop_storage)
root.order.add_edge(loop_storage, loop_final)
root.order.add_edge(loop_final, final_approval)

print(root)