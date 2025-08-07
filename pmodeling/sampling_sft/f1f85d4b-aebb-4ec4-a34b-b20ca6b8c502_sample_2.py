import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial = Transition(label='Initial Review')
prov_check = Transition(label='Provenance Check')
material_test = Transition(label='Material Testing')
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

# Loop for repeated expert survey and risk analysis
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_survey, risk_analysis])

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial, prov_check, material_test,
    expert_loop, condition_report,
    legal_review, seller_negotiation,
    documentation, archival_entry,
    committee_review, final_approval,
    acquisition_setup, exhibit_planning
])

# Define the control-flow dependencies
root.order.add_edge(initial, prov_check)
root.order.add_edge(prov_check, material_test)
root.order.add_edge(material_test, expert_loop)
root.order.add_edge(expert_loop, condition_report)
root.order.add_edge(condition_report, legal_review)
root.order.add_edge(legal_review, seller_negotiation)
root.order.add_edge(seller_negotiation, documentation)
root.order.add_edge(documentation, archival_entry)
root.order.add_edge(archival_entry, committee_review)
root.order.add_edge(committee_review, final_approval)
root.order.add_edge(final_approval, acquisition_setup)
root.order.add_edge(acquisition_setup, exhibit_planning)