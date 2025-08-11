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

# Define loop for final review and catalog entry
loop = OperatorPOWL(operator=Operator.LOOP, children=[final_review, catalog_entry])

# Define XOR for digital archive, replica build, and transport prep
xor = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build, transport_prep])

# Define the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, material_testing, stylistic_review, expert_panel, legal_clearance, ethics_audit, insurance_quote, risk_assess, xor, loop])
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, stylistic_review)
root.order.add_edge(stylistic_review, expert_panel)
root.order.add_edge(expert_panel, legal_clearance)
root.order.add_edge(legal_clearance, ethics_audit)
root.order.add_edge(ethics_audit, insurance_quote)
root.order.add_edge(insurance_quote, risk_assess)
root.order.add_edge(risk_assess, xor)
root.order.add_edge(xor, loop)