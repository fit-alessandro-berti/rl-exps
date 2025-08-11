import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop transitions
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, restoration_track])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[shipping_monitor, customs_clear])
ledger_loop = OperatorPOWL(operator=Operator.LOOP, children=[ledger_update, legal_compliance])

# Define exclusive choice transitions
ownership_choice = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
ledger_choice = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, skip])

# Define partial order
root = StrictPartialOrder(nodes=[initial_audit, artist_review, material_check, condition_scan, ownership_choice, restoration_loop, shipping_loop, ledger_loop, exhibition_setup, public_showcase, archival_prep, final_report])
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(initial_audit, material_check)
root.order.add_edge(artist_review, condition_scan)
root.order.add_edge(material_check, condition_scan)
root.order.add_edge(condition_scan, ownership_choice)
root.order.add_edge(ownership_choice, restoration_loop)
root.order.add_edge(ownership_choice, shipping_loop)
root.order.add_edge(ownership_choice, ledger_loop)
root.order.add_edge(restoration_loop, exhibition_setup)
root.order.add_edge(shipping_loop, exhibition_setup)
root.order.add_edge(ledger_loop, exhibition_setup)
root.order.add_edge(exhibition_setup, public_showcase)
root.order.add_edge(public_showcase, archival_prep)
root.order.add_edge(archival_prep, final_report)