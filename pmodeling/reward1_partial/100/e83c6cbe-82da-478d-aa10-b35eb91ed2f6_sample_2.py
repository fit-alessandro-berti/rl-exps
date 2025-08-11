import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define silent transitions (e.g., for loops or other control flow)
skip = SilentTransition()

# Define the loop nodes
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_prep, condition_report])

# Define the exclusive choice nodes
authenticity_checks = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, ethics_audit, insurance_quote, risk_assess])
legal_audit = OperatorPOWL(operator=Operator.XOR, children=[authenticity_checks, transport_loop])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, material_testing, stylistic_review, expert_panel, legal_audit, digital_archive, replica_build, final_review, catalog_entry, public_notice])

# Add dependencies between nodes
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, stylistic_review)
root.order.add_edge(stylistic_review, expert_panel)
root.order.add_edge(expert_panel, legal_audit)
root.order.add_edge(legal_audit, digital_archive)
root.order.add_edge(digital_archive, replica_build)
root.order.add_edge(replica_build, final_review)
root.order.add_edge(final_review, catalog_entry)
root.order.add_edge(catalog_entry, public_notice)

print(root)