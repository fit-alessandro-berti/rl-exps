from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
stylistic_review = Transition(label='Stylistic Review')
expert_panel = Transition(label='Expert Panel')
legal_clearance = Transition(label='Legal Clearance')
ethics_audit = Transition(label='Ethics Audit')
insurance_quote = Transition(label='Insurance Quote')
risk_assess = Transition(label='Risk Assess')
digital_archive = Transition(label='Digital Archive')
replica_build = Transition(label='Replica Build')
transport_prep = Transition(label='Transport Prep')
final_review = Transition(label='Final Review')
catalog_entry = Transition(label='Catalog Entry')
public_notice = Transition(label='Public Notice')
condition_report = Transition(label='Condition Report')

# Define the silent transition for skipping steps
skip = SilentTransition()

# Define the loop for the final review meeting
final_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_review, skip])

# Define the exclusive choice for digital archive and replica build
digital_archive_choice = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build])

# Define the exclusive choice for transport prep and public notice
transport_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, public_notice])

# Define the exclusive choice for catalog entry and condition report
catalog_entry_choice = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, condition_report])

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check, material_testing, stylistic_review, expert_panel, legal_clearance, ethics_audit, insurance_quote,
    risk_assess, digital_archive_choice, transport_prep_choice, catalog_entry_choice, final_review_loop
])

# Add the order between nodes
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, stylistic_review)
root.order.add_edge(stylistic_review, expert_panel)
root.order.add_edge(expert_panel, legal_clearance)
root.order.add_edge(legal_clearance, ethics_audit)
root.order.add_edge(ethics_audit, insurance_quote)
root.order.add_edge(insurance_quote, risk_assess)
root.order.add_edge(risk_assess, digital_archive_choice)
root.order.add_edge(digital_archive_choice, transport_prep_choice)
root.order.add_edge(transport_prep_choice, catalog_entry_choice)
root.order.add_edge(catalog_entry_choice, final_review_loop)

# Add the order within the final review loop
root.order.add_edge(final_review_loop, final_review_loop)