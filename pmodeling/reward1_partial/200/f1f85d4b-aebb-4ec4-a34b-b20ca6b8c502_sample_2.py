import pm4py
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

# Define the process flow
provenance_check_node = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
material_testing_node = OperatorPOWL(operator=Operator.XOR, children=[material_testing, skip])
expert_survey_node = OperatorPOWL(operator=Operator.XOR, children=[expert_survey, skip])
digital_scan_node = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, skip])
condition_report_node = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
legal_review_node = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
risk_analysis_node = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, skip])
seller_negotiation_node = OperatorPOWL(operator=Operator.XOR, children=[seller_negotiation, skip])
documentation_node = OperatorPOWL(operator=Operator.XOR, children=[documentation, skip])
archival_entry_node = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, skip])
committee_review_node = OperatorPOWL(operator=Operator.XOR, children=[committee_review, skip])
final_approval_node = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
acquisition_setup_node = OperatorPOWL(operator=Operator.XOR, children=[acquisition_setup, skip])
exhibit_planning_node = OperatorPOWL(operator=Operator.XOR, children=[exhibit_planning, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check_node,
    material_testing_node,
    expert_survey_node,
    digital_scan_node,
    condition_report_node,
    legal_review_node,
    risk_analysis_node,
    seller_negotiation_node,
    documentation_node,
    archival_entry_node,
    committee_review_node,
    final_approval_node,
    acquisition_setup_node,
    exhibit_planning_node
])

# Define the dependencies
root.order.add_edge(initial_review, provenance_check_node)
root.order.add_edge(provenance_check_node, material_testing_node)
root.order.add_edge(material_testing_node, expert_survey_node)
root.order.add_edge(expert_survey_node, digital_scan_node)
root.order.add_edge(digital_scan_node, condition_report_node)
root.order.add_edge(condition_report_node, legal_review_node)
root.order.add_edge(legal_review_node, risk_analysis_node)
root.order.add_edge(risk_analysis_node, seller_negotiation_node)
root.order.add_edge(seller_negotiation_node, documentation_node)
root.order.add_edge(documentation_node, archival_entry_node)
root.order.add_edge(archival_entry_node, committee_review_node)
root.order.add_edge(committee_review_node, final_approval_node)
root.order.add_edge(final_approval_node, acquisition_setup_node)
root.order.add_edge(acquisition_setup_node, exhibit_planning_node)