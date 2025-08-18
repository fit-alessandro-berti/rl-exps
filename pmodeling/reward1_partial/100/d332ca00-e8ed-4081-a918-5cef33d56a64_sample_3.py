import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (intake_document, visual_inspect),
        (intake_document, imaging_scan),
        (intake_document, material_test),
        (intake_document, database_cross),
        (visual_inspect, provenance_check),
        (visual_inspect, expert_consult),
        (imaging_scan, material_test),
        (imaging_scan, database_cross),
        (material_test, provenance_check),
        (material_test, expert_consult),
        (database_cross, provenance_check),
        (database_cross, expert_consult),
        (provenance_check, risk_assess),
        (provenance_check, report_draft),
        (provenance_check, insurance_quote),
        (provenance_check, storage_plan),
        (provenance_check, final_approval),
        (expert_consult, risk_assess),
        (expert_consult, report_draft),
        (expert_consult, insurance_quote),
        (expert_consult, storage_plan),
        (expert_consult, final_approval),
        (carbon_dating, risk_assess),
        (carbon_dating, report_draft),
        (carbon_dating, insurance_quote),
        (carbon_dating, storage_plan),
        (carbon_dating, final_approval),
        (forensic_analyze, risk_assess),
        (forensic_analyze, report_draft),
        (forensic_analyze, insurance_quote),
        (forensic_analyze, storage_plan),
        (forensic_analyze, final_approval),
        (anomaly_review, risk_assess),
        (anomaly_review, report_draft),
        (anomaly_review, insurance_quote),
        (anomaly_review, storage_plan),
        (anomaly_review, final_approval),
        (risk_assess, report_draft),
        (risk_assess, insurance_quote),
        (risk_assess, storage_plan),
        (risk_assess, final_approval),
        (report_draft, insurance_quote),
        (report_draft, storage_plan),
        (report_draft, final_approval),
        (insurance_quote, storage_plan),
        (insurance_quote, final_approval),
        (storage_plan, final_approval)
    ]
)

# Add the order dependencies
root.order.add_edge(intake_document, visual_inspect)
root.order.add_edge(intake_document, imaging_scan)
root.order.add_edge(intake_document, material_test)
root.order.add_edge(intake_document, database_cross)
root.order.add_edge(visual_inspect, provenance_check)
root.order.add_edge(visual_inspect, expert_consult)
root.order.add_edge(imaging_scan, material_test)
root.order.add_edge(imaging_scan, database_cross)
root.order.add_edge(material_test, provenance_check)
root.order.add_edge(material_test, expert_consult)
root.order.add_edge(database_cross, provenance_check)
root.order.add_edge(database_cross, expert_consult)
root.order.add_edge(provenance_check, risk_assess)
root.order.add_edge(provenance_check, report_draft)
root.order.add_edge(provenance_check, insurance_quote)
root.order.add_edge(provenance_check, storage_plan)
root.order.add_edge(provenance_check, final_approval)
root.order.add_edge(expert_consult, risk_assess)
root.order.add_edge(expert_consult, report_draft)
root.order.add_edge(expert_consult, insurance_quote)
root.order.add_edge(expert_consult, storage_plan)
root.order.add_edge(expert_consult, final_approval)
root.order.add_edge(carbon_dating, risk_assess)
root.order.add_edge(carbon_dating, report_draft)
root.order.add_edge(carbon_dating, insurance_quote)
root.order.add_edge(carbon_dating, storage_plan)
root.order.add_edge(carbon_dating, final_approval)
root.order.add_edge(forensic_analyze, risk_assess)
root.order.add_edge(forensic_analyze, report_draft)
root.order.add_edge(forensic_analyze, insurance_quote)
root.order.add_edge(forensic_analyze, storage_plan)
root.order.add_edge(forensic_analyze, final_approval)
root.order.add_edge(anomaly_review, risk_assess)
root.order.add_edge(anomaly_review, report_draft)
root.order.add_edge(anomaly_review, insurance_quote)
root.order.add_edge(anomaly_review, storage_plan)
root.order.add_edge(anomaly_review, final_approval)
root.order.add_edge(risk_assess, report_draft)
root.order.add_edge(risk_assess, insurance_quote)
root.order.add_edge(risk_assess, storage_plan)
root.order.add_edge(risk_assess, final_approval)
root.order.add_edge(report_draft, insurance_quote)
root.order.add_edge(report_draft, storage_plan)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(insurance_quote, storage_plan)
root.order.add_edge(insurance_quote, final_approval)
root.order.add_edge(storage_plan, final_approval)