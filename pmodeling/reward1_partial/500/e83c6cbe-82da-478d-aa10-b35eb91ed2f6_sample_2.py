import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_testing,
    stylistic_review,
    expert_panel,
    legal_clearance,
    ethics_audit,
    insurance_quote,
    risk_assess,
    digital_archive,
    replica_build,
    transport_prep,
    final_review,
    catalog_entry,
    public_notice,
    condition_report
])

# Define the partial order dependencies
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(provenance_check, stylistic_review)
root.order.add_edge(provenance_check, expert_panel)
root.order.add_edge(material_testing, digital_archive)
root.order.add_edge(material_testing, transport_prep)
root.order.add_edge(stylistic_review, digital_archive)
root.order.add_edge(stylistic_review, transport_prep)
root.order.add_edge(expert_panel, digital_archive)
root.order.add_edge(expert_panel, transport_prep)
root.order.add_edge(legal_clearance, insurance_quote)
root.order.add_edge(legal_clearance, risk_assess)
root.order.add_edge(ethics_audit, risk_assess)
root.order.add_edge(digital_archive, replica_build)
root.order.add_edge(digital_archive, final_review)
root.order.add_edge(digital_archive, catalog_entry)
root.order.add_edge(digital_archive, public_notice)
root.order.add_edge(digital_archive, condition_report)
root.order.add_edge(transport_prep, final_review)
root.order.add_edge(transport_prep, catalog_entry)
root.order.add_edge(transport_prep, public_notice)
root.order.add_edge(transport_prep, condition_report)
root.order.add_edge(final_review, catalog_entry)
root.order.add_edge(final_review, public_notice)
root.order.add_edge(final_review, condition_report)
root.order.add_edge(catalog_entry, public_notice)
root.order.add_edge(catalog_entry, condition_report)
root.order.add_edge(public_notice, condition_report)

# Print the root of the POWL model
print(root)