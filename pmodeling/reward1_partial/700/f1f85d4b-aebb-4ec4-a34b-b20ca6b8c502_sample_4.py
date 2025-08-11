import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_survey, digital_scan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, legal_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, seller_negotiation])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[documentation, archival_entry])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[committee_review, final_approval])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[acquisition_setup, exhibit_planning])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    initial_review,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7
])
root.order.add_edge(initial_review, xor1)
root.order.add_edge(initial_review, xor2)
root.order.add_edge(initial_review, xor3)
root.order.add_edge(initial_review, xor4)
root.order.add_edge(initial_review, xor5)
root.order.add_edge(initial_review, xor6)
root.order.add_edge(initial_review, xor7)