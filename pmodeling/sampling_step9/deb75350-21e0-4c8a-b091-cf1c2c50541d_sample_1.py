import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop for each activity
intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_review, visual_inspect, material_test])
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archival_search, expert_consult])
digital_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_scan, condition_report])
forgeries_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgeries_assess, legal_review, risk_analysis])
vote_loop = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_vote, catalog_entry, storage_prep, final_approval])

# Define XOR for each activity
intake_xor = OperatorPOWL(operator=Operator.XOR, children=[intake_loop, skip])
provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
digital_xor = OperatorPOWL(operator=Operator.XOR, children=[digital_loop, skip])
forgeries_xor = OperatorPOWL(operator=Operator.XOR, children=[forgeries_loop, skip])
vote_xor = OperatorPOWL(operator=Operator.XOR, children=[vote_loop, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[intake_xor, provenance_xor, digital_xor, forgeries_xor, vote_xor])
root.order.add_edge(intake_xor, provenance_xor)
root.order.add_edge(provenance_xor, digital_xor)
root.order.add_edge(digital_xor, forgeries_xor)
root.order.add_edge(forgeries_xor, vote_xor)

# Print the root POWL model
print(root)