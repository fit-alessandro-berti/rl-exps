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

# Provenance verification and material analysis
provenance_check_and_material_testing = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_testing])

# Expert consultation and digital archiving
expert_survey_and_archival_entry = OperatorPOWL(operator=Operator.XOR, children=[expert_survey, archival_entry])

# Legal compliance checks and risk assessment
legal_review_and_risk_analysis = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])

# Seller negotiation and documentation
seller_negotiation_and_documentation = OperatorPOWL(operator=Operator.XOR, children=[seller_negotiation, documentation])

# Committee review and final approval
committee_review_and_final_approval = OperatorPOWL(operator=Operator.XOR, children=[committee_review, final_approval])

# Acquirement setup and exhibit planning
acquisition_setup_and_exhibit_planning = OperatorPOWL(operator=Operator.XOR, children=[acquisition_setup, exhibit_planning])

# Overall workflow
root = StrictPartialOrder(nodes=[
    provenance_check_and_material_testing,
    expert_survey_and_archival_entry,
    legal_review_and_risk_analysis,
    seller_negotiation_and_documentation,
    committee_review_and_final_approval,
    acquisition_setup_and_exhibit_planning
])

root.order.add_edge(provenance_check_and_material_testing, expert_survey_and_archival_entry)
root.order.add_edge(provenance_check_and_material_testing, legal_review_and_risk_analysis)
root.order.add_edge(provenance_check_and_material_testing, seller_negotiation_and_documentation)
root.order.add_edge(provenance_check_and_material_testing, committee_review_and_final_approval)
root.order.add_edge(provenance_check_and_material_testing, acquisition_setup_and_exhibit_planning)

root.order.add_edge(expert_survey_and_archival_entry, legal_review_and_risk_analysis)
root.order.add_edge(expert_survey_and_archival_entry, seller_negotiation_and_documentation)
root.order.add_edge(expert_survey_and_archival_entry, committee_review_and_final_approval)
root.order.add_edge(expert_survey_and_archival_entry, acquisition_setup_and_exhibit_planning)

root.order.add_edge(legal_review_and_risk_analysis, seller_negotiation_and_documentation)
root.order.add_edge(legal_review_and_risk_analysis, committee_review_and_final_approval)
root.order.add_edge(legal_review_and_risk_analysis, acquisition_setup_and_exhibit_planning)

root.order.add_edge(seller_negotiation_and_documentation, committee_review_and_final_approval)
root.order.add_edge(seller_negotiation_and_documentation, acquisition_setup_and_exhibit_planning)

root.order.add_edge(committee_review_and_final_approval, acquisition_setup_and_exhibit_planning)

print(root)