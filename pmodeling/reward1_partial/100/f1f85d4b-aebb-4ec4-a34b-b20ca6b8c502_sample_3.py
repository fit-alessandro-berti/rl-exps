import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
expert_survey = Transition(label='Expert Survey')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
seller_negotiation = Transition(label='Seller Negotiation')
documentation = Transition(label='Documentation')
archival_entry = Transition(label='Archival Entry')
committee_review = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')
acquisition_setup = Transition(label='Acquisition Setup')
exhibit_planning = Transition(label='Exhibit Planning')

# Define silent transitions (if any)
skip = SilentTransition()

# Define the workflow model
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, expert_survey])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_testing, skip])
xor_risk = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, skip])
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor_documentation = OperatorPOWL(operator=Operator.XOR, children=[documentation, skip])
xor_archival = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, skip])
xor_committee = OperatorPOWL(operator=Operator.XOR, children=[committee_review, skip])
xor_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[initial_review, loop_provenance, xor_material, xor_risk, xor_legal, xor_documentation, xor_archival, xor_committee, xor_final_approval, acquisition_setup, exhibit_planning])
root.order.add_edge(initial_review, loop_provenance)
root.order.add_edge(loop_provenance, xor_material)
root.order.add_edge(xor_material, xor_risk)
root.order.add_edge(xor_risk, xor_legal)
root.order.add_edge(xor_legal, xor_documentation)
root.order.add_edge(xor_documentation, xor_archival)
root.order.add_edge(xor_archival, xor_committee)
root.order.add_edge(xor_committee, xor_final_approval)
root.order.add_edge(xor_final_approval, acquisition_setup)
root.order.add_edge(acquisition_setup, exhibit_planning)

print(root)