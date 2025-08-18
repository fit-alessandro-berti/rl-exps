from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
initial_audit = Transition(label='Initial Audit')
artist_review = Transition(label='Artist Review')
material_check = Transition(label='Material Check')
condition_scan = Transition(label='Condition Scan')
ownership_verify = Transition(label='Ownership Verify')
appraisal_update = Transition(label='Appraisal Update')
restoration_plan = Transition(label='Restoration Plan')
restoration_track = Transition(label='Restoration Track')
logistics_book = Transition(label='Logistics Book')
shipping_monitor = Transition(label='Shipping Monitor')
customs_clear = Transition(label='Customs Clear')
legal_compliance = Transition(label='Legal Compliance')
ledger_update = Transition(label='Ledger Update')
exhibition_setup = Transition(label='Exhibition Setup')
public_showcase = Transition(label='Public Showcase')
archival_prep = Transition(label='Archival Prep')
final_report = Transition(label='Final Report')

# Define the POWL operators
xor_operator = OperatorPOWL(operator=Operator.XOR, children=[
    material_check, 
    artist_review
])
xor_operator2 = OperatorPOWL(operator=Operator.XOR, children=[
    condition_scan, 
    ownership_verify
])
xor_operator3 = OperatorPOWL(operator=Operator.XOR, children=[
    restoration_plan, 
    restoration_track
])
xor_operator4 = OperatorPOWL(operator=Operator.XOR, children=[
    logistics_book, 
    shipping_monitor
])
xor_operator5 = OperatorPOWL(operator=Operator.XOR, children=[
    customs_clear, 
    legal_compliance
])
xor_operator6 = OperatorPOWL(operator=Operator.XOR, children=[
    ledger_update, 
    exhibition_setup
])
xor_operator7 = OperatorPOWL(operator=Operator.XOR, children=[
    public_showcase, 
    archival_prep
])
xor_operator8 = OperatorPOWL(operator=Operator.XOR, children=[
    final_report, 
    SilentTransition()
])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[
    initial_audit, 
    xor_operator, 
    xor_operator2, 
    xor_operator3, 
    xor_operator4, 
    xor_operator5, 
    xor_operator6, 
    xor_operator7, 
    xor_operator8
])

# Define the POWL dependencies
root.order.add_edge(initial_audit, xor_operator)
root.order.add_edge(xor_operator, xor_operator2)
root.order.add_edge(xor_operator2, xor_operator3)
root.order.add_edge(xor_operator3, xor_operator4)
root.order.add_edge(xor_operator4, xor_operator5)
root.order.add_edge(xor_operator5, xor_operator6)
root.order.add_edge(xor_operator6, xor_operator7)
root.order.add_edge(xor_operator7, xor_operator8)

print(root)