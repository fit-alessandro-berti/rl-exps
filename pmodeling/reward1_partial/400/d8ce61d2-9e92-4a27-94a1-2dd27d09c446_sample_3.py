import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    initial_audit,
    artist_review,
    material_check,
    condition_scan,
    ownership_verify,
    appraisal_update,
    restoration_plan,
    restoration_track,
    logistics_book,
    shipping_monitor,
    customs_clear,
    legal_compliance,
    ledger_update,
    exhibition_setup,
    public_showcase,
    archival_prep,
    final_report
])

# Define the order of activities
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(artist_review, material_check)
root.order.add_edge(material_check, condition_scan)
root.order.add_edge(condition_scan, ownership_verify)
root.order.add_edge(ownership_verify, appraisal_update)
root.order.add_edge(appraisal_update, restoration_plan)
root.order.add_edge(restoration_plan, restoration_track)
root.order.add_edge(restoration_track, logistics_book)
root.order.add_edge(logistics_book, shipping_monitor)
root.order.add_edge(shipping_monitor, customs_clear)
root.order.add_edge(customs_clear, legal_compliance)
root.order.add_edge(legal_compliance, ledger_update)
root.order.add_edge(ledger_update, exhibition_setup)
root.order.add_edge(exhibition_setup, public_showcase)
root.order.add_edge(public_showcase, archival_prep)
root.order.add_edge(archival_prep, final_report)

print(root)