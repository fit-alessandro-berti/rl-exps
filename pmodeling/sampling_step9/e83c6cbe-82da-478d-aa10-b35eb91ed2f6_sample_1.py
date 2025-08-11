import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop for digital archive, replica build, and transport prep
loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_archive, replica_build, transport_prep])

# Define xor for legal clearance, ethics audit, insurance quote, and risk assess
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, ethics_audit, insurance_quote, risk_assess])

# Define root
root = StrictPartialOrder(nodes=[provenance_check, material_testing, stylistic_review, expert_panel, loop, xor, final_review, catalog_entry, public_notice, condition_report])
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, stylistic_review)
root.order.add_edge(stylistic_review, expert_panel)
root.order.add_edge(expert_panel, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, final_review)
root.order.add_edge(final_review, catalog_entry)
root.order.add_edge(catalog_entry, public_notice)
root.order.add_edge(public_notice, condition_report)

print(root)