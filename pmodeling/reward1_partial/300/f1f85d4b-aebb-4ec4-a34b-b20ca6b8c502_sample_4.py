import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, seller_negotiation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[committee_review, final_approval])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_planning, acquisition_setup])

# Define the root node
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_testing,
    expert_survey,
    digital_scan,
    condition_report,
    xor,
    xor2,
    xor3,
    xor4
])
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, expert_survey)
root.order.add_edge(expert_survey, digital_scan)
root.order.add_edge(digital_scan, condition_report)
root.order.add_edge(condition_report, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, archival_entry)
root.order.add_edge(archival_entry, committee_review)
root.order.add_edge(committee_review, final_approval)
root.order.add_edge(final_approval, acquisition_setup)
root.order.add_edge(acquisition_setup, exhibit_planning)