import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define workflow elements
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, expert_review, legal_verify, risk_assess, insurance_quote, catalog_entry, digital_scan, condition_report, transport_plan, customs_clear])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[certification, exhibit_setup, owner_notify, final_audit])

# Create the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)

# Print the POWL model
print(root)