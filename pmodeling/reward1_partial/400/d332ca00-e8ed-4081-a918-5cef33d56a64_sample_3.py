from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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

# Define the POWL model
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
    order={
        (intake_document, visual_inspect),
        (intake_document, imaging_scan),
        (intake_document, material_test),
        (intake_document, database_cross),
        (intake_document, provenance_check),
        (intake_document, expert_consult),
        (intake_document, carbon_dating),
        (intake_document, forensic_analyze),
        (intake_document, anomaly_review),
        (intake_document, risk_assess),
        (intake_document, report_draft),
        (intake_document, insurance_quote),
        (intake_document, storage_plan),
        (intake_document, final_approval),
        (visual_inspect, imaging_scan),
        (visual_inspect, material_test),
        (visual_inspect, database_cross),
        (visual_inspect, provenance_check),
        (visual_inspect, expert_consult),
        (visual_inspect, carbon_dating),
        (visual_inspect, forensic_analyze),
        (visual_inspect, anomaly_review),
        (visual_inspect, risk_assess),
        (visual_inspect, report_draft),
        (visual_inspect, insurance_quote),
        (visual_inspect, storage_plan),
        (visual_inspect, final_approval),
        (imaging_scan, material_test),
        (imaging_scan, database_cross),
        (imaging_scan, provenance_check),
        (imaging_scan, expert_consult),
        (imaging_scan, carbon_dating),
        (imaging_scan, forensic_analyze),
        (imaging_scan, anomaly_review),
        (imaging_scan, risk_assess),
        (imaging_scan, report_draft),
        (imaging_scan, insurance_quote),
        (imaging_scan, storage_plan),
        (imaging_scan, final_approval),
        (material_test, database_cross),
        (material_test, provenance_check),
        (material_test, expert_consult),
        (material_test, carbon_dating),
        (material_test, forensic_analyze),
        (material_test, anomaly_review),
        (material_test, risk_assess),
        (material_test, report_draft),
        (material_test, insurance_quote),
        (material_test, storage_plan),
        (material_test, final_approval),
        (database_cross, provenance_check),
        (database_cross, expert_consult),
        (database_cross, carbon_dating),
        (database_cross, forensic_analyze),
        (database_cross, anomaly_review),
        (database_cross, risk_assess),
        (database_cross, report_draft),
        (database_cross, insurance_quote),
        (database_cross, storage_plan),
        (database_cross, final_approval),
        (provenance_check, expert_consult),
        (provenance_check, carbon_dating),
        (provenance_check, forensic_analyze),
        (provenance_check, anomaly_review),
        (provenance_check, risk_assess),
        (provenance_check, report_draft),
        (provenance_check, insurance_quote),
        (provenance_check, storage_plan),
        (provenance_check, final_approval),
        (expert_consult, carbon_dating),
        (expert_consult, forensic_analyze),
        (expert_consult, anomaly_review),
        (expert_consult, risk_assess),
        (expert_consult, report_draft),
        (expert_consult, insurance_quote),
        (expert_consult, storage_plan),
        (expert_consult, final_approval),
        (carbon_dating, forensic_analyze),
        (carbon_dating, anomaly_review),
        (carbon_dating, risk_assess),
        (carbon_dating, report_draft),
        (carbon_dating, insurance_quote),
        (carbon_dating, storage_plan),
        (carbon_dating, final_approval),
        (forensic_analyze, anomaly_review),
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
    }
)

# Print the root POWL model
print(root)