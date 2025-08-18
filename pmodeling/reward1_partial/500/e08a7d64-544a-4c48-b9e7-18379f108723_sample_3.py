import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Initial provenance check
initial_workflow = StrictPartialOrder(nodes=[provenance_check, material_testing, expert_review, legal_verify, risk_assess, insurance_quote, catalog_entry, digital_scan, condition_report, transport_plan, customs_clear, certification, exhibit_setup, owner_notify, final_audit])

# Define the partial order dependencies
initial_workflow.order.add_edge(provenance_check, material_testing)
initial_workflow.order.add_edge(material_testing, expert_review)
initial_workflow.order.add_edge(expert_review, legal_verify)
initial_workflow.order.add_edge(legal_verify, risk_assess)
initial_workflow.order.add_edge(risk_assess, insurance_quote)
initial_workflow.order.add_edge(insurance_quote, catalog_entry)
initial_workflow.order.add_edge(catalog_entry, digital_scan)
initial_workflow.order.add_edge(digital_scan, condition_report)
initial_workflow.order.add_edge(condition_report, transport_plan)
initial_workflow.order.add_edge(transport_plan, customs_clear)
initial_workflow.order.add_edge(customs_clear, certification)
initial_workflow.order.add_edge(certification, exhibit_setup)
initial_workflow.order.add_edge(exhibit_setup, owner_notify)
initial_workflow.order.add_edge(owner_notify, final_audit)

root = initial_workflow