from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Create the process
root = StrictPartialOrder(nodes=[
    intake_document,
    visual_inspect,
    imaging_scan,
    material_test,
    database_cross,
    provenance_check,
    expert_consult,
    carbon_dating,
    forensic_analyze,
    anomaly_review,
    risk_assess,
    report_draft,
    insurance_quote,
    storage_plan,
    final_approval
])

# Define the order of execution
root.order.add_edge(intake_document, visual_inspect)
root.order.add_edge(intake_document, imaging_scan)
root.order.add_edge(intake_document, material_test)
root.order.add_edge(intake_document, database_cross)
root.order.add_edge(intake_document, provenance_check)
root.order.add_edge(intake_document, expert_consult)
root.order.add_edge(intake_document, carbon_dating)
root.order.add_edge(intake_document, forensic_analyze)
root.order.add_edge(intake_document, anomaly_review)
root.order.add_edge(intake_document, risk_assess)
root.order.add_edge(intake_document, report_draft)
root.order.add_edge(intake_document, insurance_quote)
root.order.add_edge(intake_document, storage_plan)
root.order.add_edge(intake_document, final_approval)

print(root)