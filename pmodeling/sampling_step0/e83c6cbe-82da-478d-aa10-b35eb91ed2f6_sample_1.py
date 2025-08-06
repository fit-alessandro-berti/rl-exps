from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Provenance Check')
B = Transition(label='Material Testing')
C = Transition(label='Stylistic Review')
D = Transition(label='Expert Panel')
E = Transition(label='Legal Clearance')
F = Transition(label='Ethics Audit')
G = Transition(label='Insurance Quote')
H = Transition(label='Risk Assess')
I = Transition(label='Digital Archive')
J = Transition(label='Replica Build')
K = Transition(label='Transport Prep')
L = Transition(label='Final Review')
M = Transition(label='Catalog Entry')
N = Transition(label='Public Notice')
O = Transition(label='Condition Report')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
provenance_check = StrictPartialOrder(nodes=[A], order={})
material_testing = StrictPartialOrder(nodes=[B], order={})
stylistic_review = StrictPartialOrder(nodes=[C], order={})
expert_panel = StrictPartialOrder(nodes=[D], order={})
legal_clearance = StrictPartialOrder(nodes=[E], order={})
ethics_audit = StrictPartialOrder(nodes=[F], order={})
insurance_quote = StrictPartialOrder(nodes=[G], order={})
risk_assess = StrictPartialOrder(nodes=[H], order={})
digital_archive = StrictPartialOrder(nodes=[I], order={})
replica_build = StrictPartialOrder(nodes=[J], order={})
transport_prep = StrictPartialOrder(nodes=[K], order={})
final_review = StrictPartialOrder(nodes=[L], order={})
catalog_entry = StrictPartialOrder(nodes=[M], order={})
public_notice = StrictPartialOrder(nodes=[N], order={})
condition_report = StrictPartialOrder(nodes=[O], order={})

# Define exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, insurance_quote])

# Define partial order for activities and sub-processes
root = StrictPartialOrder(nodes=[provenance_check, material_testing, stylistic_review, expert_panel, xor, final_review, catalog_entry, public_notice, condition_report])
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(material_testing, stylistic_review)
root.order.add_edge(stylistic_review, expert_panel)
root.order.add_edge(expert_panel, xor)
root.order.add_edge(xor, final_review)
root.order.add_edge(final_review, catalog_entry)
root.order.add_edge(catalog_entry, public_notice)
root.order.add_edge(public_notice, condition_report)

print(root)