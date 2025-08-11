from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Workflow steps
provenance_and_material = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_testing])
expert_and_condition = OperatorPOWL(operator=Operator.XOR, children=[expert_survey, condition_report])
legal_and_risk = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])
seller_and_documentation = OperatorPOWL(operator=Operator.XOR, children=[seller_negotiation, documentation])
archival_and_committee = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, committee_review])
final_and_setup = OperatorPOWL(operator=Operator.XOR, children=[final_approval, acquisition_setup])
exhibit_and_planning = OperatorPOWL(operator=Operator.XOR, children=[final_approval, exhibit_planning])

# Workflow structure
root = StrictPartialOrder(nodes=[initial_review, provenance_and_material, expert_and_condition, legal_and_risk, seller_and_documentation, archival_and_committee, final_and_setup, exhibit_and_planning])
root.order.add_edge(initial_review, provenance_and_material)
root.order.add_edge(initial_review, expert_and_condition)
root.order.add_edge(initial_review, legal_and_risk)
root.order.add_edge(initial_review, seller_and_documentation)
root.order.add_edge(initial_review, archival_and_committee)
root.order.add_edge(initial_review, final_and_setup)
root.order.add_edge(initial_review, exhibit_and_planning)