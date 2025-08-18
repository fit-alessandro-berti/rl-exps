from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define silent transitions
skip_audit = SilentTransition()
skip_review = SilentTransition()
skip_check = SilentTransition()
skip_scan = SilentTransition()
skip_verify = SilentTransition()
skip_update = SilentTransition()
skip_plan = SilentTransition()
skip_track = SilentTransition()
skip_book = SilentTransition()
skip_monitor = SilentTransition()
skip_clear = SilentTransition()
skip_compliance = SilentTransition()
skip_update_ledger = SilentTransition()
skip_setup = SilentTransition()
skip_showcase = SilentTransition()
skip_prep = SilentTransition()

# Define partial order
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

# Define dependencies
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

# Add silent transitions as needed
root.order.add_edge(initial_audit, skip_review)
root.order.add_edge(artist_review, skip_check)
root.order.add_edge(material_check, skip_scan)
root.order.add_edge(condition_scan, skip_verify)
root.order.add_edge(ownership_verify, skip_update)
root.order.add_edge(appraisal_update, skip_plan)
root.order.add_edge(restoration_plan, skip_track)
root.order.add_edge(restoration_track, skip_book)
root.order.add_edge(logistics_book, skip_monitor)
root.order.add_edge(shipping_monitor, skip_clear)
root.order.add_edge(customs_clear, skip_compliance)
root.order.add_edge(legal_compliance, skip_update_ledger)
root.order.add_edge(ledger_update, skip_setup)
root.order.add_edge(exhibition_setup, skip_showcase)
root.order.add_edge(public_showcase, skip_prep)