import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loop for the restoration process
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, restoration_track])

# Define the XOR for the logistics and legal compliance processes
logistics_legal_xor = OperatorPOWL(operator=Operator.XOR, children=[logistics_book, legal_compliance])

# Define the loop for the exhibition process
exhibition_loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibition_setup, public_showcase, archival_prep])

# Define the XOR for the final report and ledger update processes
final_report_ledger_xor = OperatorPOWL(operator=Operator.XOR, children=[final_report, ledger_update])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    initial_audit,
    artist_review,
    material_check,
    condition_scan,
    ownership_verify,
    appraisal_update,
    restoration_loop,
    logistics_legal_xor,
    exhibition_loop,
    final_report_ledger_xor
])

# Add edges to the root POWL model
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(artist_review, material_check)
root.order.add_edge(material_check, condition_scan)
root.order.add_edge(condition_scan, ownership_verify)
root.order.add_edge(ownership_verify, appraisal_update)
root.order.add_edge(appraisal_update, restoration_loop)
root.order.add_edge(restoration_loop, logistics_legal_xor)
root.order.add_edge(logistics_legal_xor, exhibition_loop)
root.order.add_edge(exhibition_loop, final_report_ledger_xor)
root.order.add_edge(final_report_ledger_xor, final_report)
root.order.add_edge(final_report_ledger_xor, ledger_update)

# Print the root POWL model
print(root)