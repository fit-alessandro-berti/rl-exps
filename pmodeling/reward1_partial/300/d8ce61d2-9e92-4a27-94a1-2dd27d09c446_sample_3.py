from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_check, condition_scan, ownership_verify, appraisal_update, restoration_plan, restoration_track])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[logistics_book, shipping_monitor, customs_clear, legal_compliance, ledger_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[exhibition_setup, public_showcase, archival_prep, final_report])

root = StrictPartialOrder(nodes=[initial_audit, artist_review, xor1, xor2, xor3])
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(artist_review, xor1)
root.order.add_edge(artist_review, xor2)
root.order.add_edge(artist_review, xor3)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)