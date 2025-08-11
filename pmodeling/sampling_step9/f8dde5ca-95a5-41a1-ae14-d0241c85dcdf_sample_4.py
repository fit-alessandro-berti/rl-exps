import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon_test = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
database_query = Transition(label='Database Query')
blockchain_prep = Transition(label='Blockchain Prep')
legal_review = Transition(label='Legal Review')
ownership_audit = Transition(label='Ownership Audit')
conservation_plan = Transition(label='Conservation Plan')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
client_review = Transition(label='Client Review')
authority_submit = Transition(label='Authority Submit')
exhibit_setup = Transition(label='Exhibit Setup')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

# Provenance Check
# Material Scan
# Radiocarbon Test
# Style Compare
# Database Query
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, radiocarbon_test, style_compare, database_query])

# Blockchain Prep
# Legal Review
# Ownership Audit
# Conservation Plan
xor2 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_prep, legal_review, ownership_audit, conservation_plan])

# Expert Panel
# Report Draft
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, report_draft])

# Client Review
# Authority Submit
xor4 = OperatorPOWL(operator=Operator.XOR, children=[client_review, authority_submit])

# Exhibit Setup
# Final Approval
xor5 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, final_approval])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5])

root = StrictPartialOrder(nodes=[loop1])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)