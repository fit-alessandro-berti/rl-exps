import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define the POWL model
root = StrictPartialOrder()

# Define the process flow
root.add_transition(initial_audit)
root.add_transition(artist_review)
root.add_transition(material_check)
root.add_transition(condition_scan)
root.add_transition(ownership_verify)
root.add_transition(appraisal_update)
root.add_transition(restoration_plan)
root.add_transition(restoration_track)
root.add_transition(logistics_book)
root.add_transition(shipping_monitor)
root.add_transition(customs_clearance)
root.add_transition(legal_compliance)
root.add_transition(ledger_update)
root.add_transition(exhibition_setup)
root.add_transition(public_showcase)
root.add_transition(archival_prep)
root.add_transition(final_report)

# Define the dependencies (partial order)
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(artist_review, material_check)
root.order.add_edge(material_check, condition_scan)
root.order.add_edge(condition_scan, ownership_verify)
root.order.add_edge(ownership_verify, appraisal_update)
root.order.add_edge(appraisal_update, restoration_plan)
root.order.add_edge(restoration_plan, restoration_track)
root.order.add_edge(restoration_track, logistics_book)
root.order.add_edge(logistics_book, shipping_monitor)
root.order.add_edge(shipping_monitor, customs_clearance)
root.order.add_edge(customs_clearance, legal_compliance)
root.order.add_edge(legal_compliance, ledger_update)
root.order.add_edge(ledger_update, exhibition_setup)
root.order.add_edge(exhibition_setup, public_showcase)
root.order.add_edge(public_showcase, archival_prep)
root.order.add_edge(archival_prep, final_report)

# Print the root POWL model
print(root)