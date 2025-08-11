import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define loop nodes
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, restoration_track])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_book, shipping_monitor, customs_clear, legal_compliance])

# Define exclusive choices
ownership_exclusive = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
ledger_exclusive = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, skip])
exhibition_exclusive = OperatorPOWL(operator=Operator.XOR, children=[exhibition_setup, skip])
showcase_exclusive = OperatorPOWL(operator=Operator.XOR, children=[public_showcase, skip])
archival_exclusive = OperatorPOWL(operator=Operator.XOR, children=[archival_prep, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_audit, artist_review, material_check, condition_scan, ownership_exclusive, restoration_loop, shipping_loop, appraisal_update, ledger_exclusive, exhibition_exclusive, showcase_exclusive, archival_exclusive, final_report])
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(artist_review, material_check)
root.order.add_edge(material_check, condition_scan)
root.order.add_edge(condition_scan, ownership_exclusive)
root.order.add_edge(ownership_exclusive, restoration_loop)
root.order.add_edge(restoration_loop, shipping_loop)
root.order.add_edge(shipping_loop, appraisal_update)
root.order.add_edge(appraisal_update, ledger_exclusive)
root.order.add_edge(ledger_exclusive, exhibition_exclusive)
root.order.add_edge(exhibition_exclusive, showcase_exclusive)
root.order.add_edge(showcase_exclusive, archival_exclusive)
root.order.add_edge(archival_exclusive, final_report)