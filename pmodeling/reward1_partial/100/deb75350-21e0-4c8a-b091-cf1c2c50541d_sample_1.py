import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[intake_review, visual_inspect, material_test, provenance_check, archival_search, expert_consult, digital_scan, condition_report, forgeries_assess, legal_review, risk_analysis, acquisition_vote, catalog_entry, storage_prep, final_approval])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, final_approval])

root = StrictPartialOrder(nodes=[loop1, xor1])
root.order.add_edge(loop1, xor1)

# Print the root of the POWL model
print(root)