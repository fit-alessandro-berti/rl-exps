import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
initial_review      = Transition(label='Initial Review')
provenance_check    = Transition(label='Provenance Check')
material_testing    = Transition(label='Material Testing')
expert_survey       = Transition(label='Expert Survey')
digital_scan        = Transition(label='Digital Scan')
condition_report    = Transition(label='Condition Report')
legal_review        = Transition(label='Legal Review')
risk_analysis       = Transition(label='Risk Analysis')
seller_negotiation  = Transition(label='Seller Negotiation')
documentation       = Transition(label='Documentation')
archival_entry      = Transition(label='Archival Entry')
committee_review    = Transition(label='Committee Review')
final_approval      = Transition(label='Final Approval')
acquisition_setup   = Transition(label='Acquisition Setup')
exhibit_planning    = Transition(label='Exhibit Planning')

# Build the loop body: Seller Negotiation -> Risk Analysis -> Legal Review
loop_body = StrictPartialOrder(nodes=[seller_negotiation, risk_analysis, legal_review])
loop_body.order.add_edge(seller_negotiation, risk_analysis)
loop_body.order.add_edge(risk_analysis, legal_review)

# Define the loop: repeat Seller Negotiation -> Risk Analysis -> Legal Review until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_review, loop_body])

# Build the main workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    loop,
    provenance_check,
    material_testing,
    expert_survey,
    digital_scan,
    condition_report,
    archival_entry,
    documentation,
    committee_review,
    final_approval,
    acquisition_setup,
    exhibit_planning
])

# Add the control-flow dependencies
root.order.add_edge(loop, provenance_check)
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(provenance_check, expert_survey)
root.order.add_edge(material_testing, digital_scan)
root.order.add_edge(expert_survey, digital_scan)
root.order.add_edge(digital_scan, condition_report)
root.order.add_edge(condition_report, archival_entry)
root.order.add_edge(archival_entry, documentation)
root.order.add_edge(documentation, committee_review)
root.order.add_edge(committee_review, final_approval)
root.order.add_edge(final_approval, acquisition_setup)
root.order.add_edge(acquisition_setup, exhibit_planning)