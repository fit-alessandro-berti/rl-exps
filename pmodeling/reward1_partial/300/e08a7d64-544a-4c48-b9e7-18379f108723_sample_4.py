from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
expert_review = Transition(label='Expert Review')
legal_verify = Transition(label='Legal Verify')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
catalog_entry = Transition(label='Catalog Entry')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
transport_plan = Transition(label='Transport Plan')
customs_clear = Transition(label='Customs Clear')
certification = Transition(label='Certification')
exhibit_setup = Transition(label='Exhibit Setup')
owner_notify = Transition(label='Owner Notify')
final_audit = Transition(label='Final Audit')

# Define the workflow
root = StrictPartialOrder(
    nodes=[provenance_check, material_testing, expert_review, legal_verify, risk_assess, insurance_quote,
           catalog_entry, digital_scan, condition_report, transport_plan, customs_clear, certification, exhibit_setup,
           owner_notify, final_audit]
)

# Define the dependencies between activities
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, expert_review)
root.order.add_edge(expert_review, legal_verify)
root.order.add_edge(legal_verify, risk_assess)
root.order.add_edge(risk_assess, insurance_quote)
root.order.add_edge(insurance_quote, catalog_entry)
root.order.add_edge(catalog_entry, digital_scan)
root.order.add_edge(digital_scan, condition_report)
root.order.add_edge(condition_report, transport_plan)
root.order.add_edge(transport_plan, customs_clear)
root.order.add_edge(customs_clear, certification)
root.order.add_edge(certification, exhibit_setup)
root.order.add_edge(exhibit_setup, owner_notify)
root.order.add_edge(owner_notify, final_audit)

# Print the root model
print(root)