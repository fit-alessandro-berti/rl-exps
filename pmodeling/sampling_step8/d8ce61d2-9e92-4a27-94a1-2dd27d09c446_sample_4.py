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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[restoration_track, logistics_book])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[shipping_monitor, customs_clear])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, ledger_update])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[exhibition_setup, public_showcase])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[archival_prep, final_report])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[final_report, SilentTransition()])

# Construct the POWL model
root = StrictPartialOrder(nodes=[initial_audit, artist_review, material_check, condition_scan, ownership_verify,
                                  appraisal_update, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(initial_audit, artist_review)
root.order.add_edge(artist_review, material_check)
root.order.add_edge(material_check, condition_scan)
root.order.add_edge(condition_scan, ownership_verify)
root.order.add_edge(ownership_verify, appraisal_update)
root.order.add_edge(appraisal_update, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, final_report)

# Print the POWL model
print(root)