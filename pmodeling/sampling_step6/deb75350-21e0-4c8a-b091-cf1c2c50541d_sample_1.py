import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forgeries_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[intake_review, visual_inspect, material_test, provenance_check, archival_search, expert_consult, digital_scan, condition_report, forgeries_assess, legal_review, risk_analysis, acquisition_vote, catalog_entry, storage_prep, final_approval])

# Add dependencies if any (if not, dependencies will be inferred from the order of transitions)
# root.order.add_edge(intake_review, visual_inspect)
# root.order.add_edge(intake_review, material_test)
# root.order.add_edge(intake_review, provenance_check)
# root.order.add_edge(intake_review, archival_search)
# root.order.add_edge(intake_review, expert_consult)
# root.order.add_edge(intake_review, digital_scan)
# root.order.add_edge(intake_review, condition_report)
# root.order.add_edge(intake_review, forgeries_assess)
# root.order.add_edge(intake_review, legal_review)
# root.order.add_edge(intake_review, risk_analysis)
# root.order.add_edge(intake_review, acquisition_vote)
# root.order.add_edge(intake_review, catalog_entry)
# root.order.add_edge(intake_review, storage_prep)
# root.order.add_edge(intake_review, final_approval)

# Print the root to see the complete POWL model
print(root)