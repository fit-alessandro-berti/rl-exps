import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
customs_clearance = Transition(label='Customs Clear')
legal_compliance = Transition(label='Legal Compliance')
ledger_update = Transition(label='Ledger Update')
exhibition_setup = Transition(label='Exhibition Setup')
public_showcase = Transition(label='Public Showcase')
archival_prep = Transition(label='Archival Prep')
final_report = Transition(label='Final Report')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
audit_artist = OperatorPOWL(operator=Operator.XOR, children=[initial_audit, artist_review])
check_material = OperatorPOWL(operator=Operator.XOR, children=[material_check, condition_scan])
verify_ownership = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, appraisal_update])
plan_restoration = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, restoration_track])
book_logistics = OperatorPOWL(operator=Operator.XOR, children=[logistics_book, shipping_monitor])
clear_customs = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, legal_compliance])
update_ledger = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, exhibition_setup])
setup_exhibition = OperatorPOWL(operator=Operator.XOR, children=[exhibition_setup, public_showcase])
prep_archival = OperatorPOWL(operator=Operator.XOR, children=[archival_prep, final_report])

# Define loops
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, restoration_track])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_book, shipping_monitor])
clearance_loop = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance, legal_compliance])
ledger_loop = OperatorPOWL(operator=Operator.LOOP, children=[ledger_update, exhibition_setup])
exhibition_loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibition_setup, public_showcase])
archival_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_prep, final_report])

# Define partial order
root = StrictPartialOrder(nodes=[
    audit_artist,
    check_material,
    verify_ownership,
    plan_restoration,
    book_logistics,
    clear_customs,
    update_ledger,
    setup_exhibition,
    prep_archival,
    restoration_loop,
    shipping_loop,
    clearance_loop,
    ledger_loop,
    exhibition_loop,
    archival_loop
])

# Define order dependencies
root.order.add_edge(audit_artist, check_material)
root.order.add_edge(check_material, verify_ownership)
root.order.add_edge(verify_ownership, plan_restoration)
root.order.add_edge(plan_restoration, book_logistics)
root.order.add_edge(book_logistics, clear_customs)
root.order.add_edge(clear_customs, update_ledger)
root.order.add_edge(update_ledger, setup_exhibition)
root.order.add_edge(setup_exhibition, prep_archival)
root.order.add_edge(restoration_loop, shipping_loop)
root.order.add_edge(shipping_loop, clearance_loop)
root.order.add_edge(clearance_loop, ledger_loop)
root.order.add_edge(ledger_loop, exhibition_loop)
root.order.add_edge(exhibition_loop, archival_loop)
root.order.add_edge(archival_loop, final_report)

# Print the root model
print(root)