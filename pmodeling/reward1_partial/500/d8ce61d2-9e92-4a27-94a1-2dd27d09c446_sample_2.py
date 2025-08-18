import pm4py

# Define the activities
initial_audit = pm4py.objects.powl.obj.Transition(label='Initial Audit')
artist_review = pm4py.objects.powl.obj.Transition(label='Artist Review')
material_check = pm4py.objects.powl.obj.Transition(label='Material Check')
condition_scan = pm4py.objects.powl.obj.Transition(label='Condition Scan')
ownership_verify = pm4py.objects.powl.obj.Transition(label='Ownership Verify')
appraisal_update = pm4py.objects.powl.obj.Transition(label='Appraisal Update')
restoration_plan = pm4py.objects.powl.obj.Transition(label='Restoration Plan')
restoration_track = pm4py.objects.powl.obj.Transition(label='Restoration Track')
logistics_book = pm4py.objects.powl.obj.Transition(label='Logistics Book')
shipping_monitor = pm4py.objects.powl.obj.Transition(label='Shipping Monitor')
customs_clearance = pm4py.objects.powl.obj.Transition(label='Customs Clear')
legal_compliance = pm4py.objects.powl.obj.Transition(label='Legal Compliance')
ledger_update = pm4py.objects.powl.obj.Transition(label='Ledger Update')
exhibition_setup = pm4py.objects.powl.obj.Transition(label='Exhibition Setup')
public_showcase = pm4py.objects.powl.obj.Transition(label='Public Showcase')
archival_prep = pm4py.objects.powl.obj.Transition(label='Archival Prep')
final_report = pm4py.objects.powl.obj.Transition(label='Final Report')

# Define the partial order structure
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[
    initial_audit, artist_review, material_check, condition_scan,
    ownership_verify, appraisal_update, restoration_plan,
    restoration_track, logistics_book, shipping_monitor, customs_clearance,
    legal_compliance, ledger_update, exhibition_setup, public_showcase,
    archival_prep, final_report
])

# Define the dependencies between activities
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

print(root)