import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names as provided in the description
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forgery_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    intake_review, visual_inspect, material_test, provenance_check, archival_search, expert_consult,
    digital_scan, condition_report, forgery_assess, legal_review, risk_analysis, acquisition_vote,
    catalog_entry, storage_prep, final_approval
])

# Since there are no explicit dependencies or loops in the description, we don't need to add any order edges here.
# However, if there were dependencies, they would be added like this:
# root.order.add_edge(...)

# The 'root' variable now holds the complete POWL model for the described process.