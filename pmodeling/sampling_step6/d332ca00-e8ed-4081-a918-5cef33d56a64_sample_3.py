import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
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

# Define the process as a strict partial order
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
# No explicit dependencies are defined in this process, so no edges are added

# The 'root' variable now contains the POWL model for the described process.