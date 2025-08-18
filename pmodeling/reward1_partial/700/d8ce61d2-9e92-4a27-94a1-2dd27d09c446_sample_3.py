import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the process structure
initial_audit_to_artist_review = OperatorPOWL(operator=Operator.XOR, children=[initial_audit, artist_review])
artist_review_to_material_check = OperatorPOWL(operator=Operator.XOR, children=[artist_review, material_check])
material_check_to_condition_scan = OperatorPOWL(operator=Operator.XOR, children=[material_check, condition_scan])
condition_scan_to_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[condition_scan, ownership_verify])
ownership_verify_to_appraisal_update = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, appraisal_update])
appraisal_update_to_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[appraisal_update, restoration_plan])
restoration_plan_to_restoration_track = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, restoration_track])
restoration_track_to_logistics_book = OperatorPOWL(operator=Operator.XOR, children=[restoration_track, logistics_book])
logistics_book_to_shipping_monitor = OperatorPOWL(operator=Operator.XOR, children=[logistics_book, shipping_monitor])
shipping_monitor_to_customs_clear = OperatorPOWL(operator=Operator.XOR, children=[shipping_monitor, customs_clear])
customs_clear_to_legal_compliance = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, legal_compliance])
legal_compliance_to_ledger_update = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, ledger_update])
ledger_update_to_exhibition_setup = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, exhibition_setup])
exhibition_setup_to_public_showcase = OperatorPOWL(operator=Operator.XOR, children=[exhibition_setup, public_showcase])
public_showcase_to_archival_prep = OperatorPOWL(operator=Operator.XOR, children=[public_showcase, archival_prep])
archival_prep_to_final_report = OperatorPOWL(operator=Operator.XOR, children=[archival_prep, final_report])

# Define the partial order
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

# Define the dependencies
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

# Print the root model
print(root)