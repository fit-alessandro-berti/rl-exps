import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_testing, expert_survey, digital_scan, condition_report, legal_review, risk_analysis, seller_negotiation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_setup, exhibit_planning])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, committee_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the root
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)

# Save the final result in the variable 'root'
root