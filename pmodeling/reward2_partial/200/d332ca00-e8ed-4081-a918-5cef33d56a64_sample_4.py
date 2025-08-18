from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    intake_doc, 
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

# Define the dependencies
root.order.add_edge(intake_doc, visual_inspect)
root.order.add_edge(intake_doc, imaging_scan)
root.order.add_edge(intake_doc, material_test)
root.order.add_edge(intake_doc, database_cross)
root.order.add_edge(intake_doc, provenance_check)
root.order.add_edge(intake_doc, expert_consult)
root.order.add_edge(imaging_scan, carbon_dating)
root.order.add_edge(material_test, carbon_dating)
root.order.add_edge(provenance_check, carbon_dating)
root.order.add_edge(expert_consult, carbon_dating)
root.order.add_edge(carbon_dating, anomaly_review)
root.order.add_edge(anomaly_review, forensic_analyze)
root.order.add_edge(anomaly_review, risk_assess)
root.order.add_edge(forensic_analyze, risk_assess)
root.order.add_edge(risk_assess, report_draft)
root.order.add_edge(report_draft, insurance_quote)
root.order.add_edge(insurance_quote, storage_plan)
root.order.add_edge(storage_plan, final_approval)