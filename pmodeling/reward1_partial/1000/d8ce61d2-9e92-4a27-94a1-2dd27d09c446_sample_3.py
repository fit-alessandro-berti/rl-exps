import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor_initial_audit = OperatorPOWL(operator=Operator.XOR, children=[initial_audit, artist_review])
xor_material_check = OperatorPOWL(operator=Operator.XOR, children=[material_check, condition_scan])
xor_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, appraisal_update])
xor_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, restoration_track])
xor_logistics_book = OperatorPOWL(operator=Operator.XOR, children=[logistics_book, shipping_monitor])
xor_customs_clearance = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, legal_compliance])
xor_ledger_update = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, exhibition_setup])
xor_public_showcase = OperatorPOWL(operator=Operator.XOR, children=[public_showcase, archival_prep])
xor_final_report = OperatorPOWL(operator=Operator.XOR, children=[final_report])

# Define the partial order
root = StrictPartialOrder(nodes=[xor_initial_audit, xor_material_check, xor_ownership_verify, xor_restoration_plan, xor_logistics_book, xor_customs_clearance, xor_ledger_update, xor_public_showcase, xor_final_report])
root.order.add_edge(xor_initial_audit, xor_material_check)
root.order.add_edge(xor_material_check, xor_ownership_verify)
root.order.add_edge(xor_ownership_verify, xor_restoration_plan)
root.order.add_edge(xor_restoration_plan, xor_logistics_book)
root.order.add_edge(xor_logistics_book, xor_customs_clearance)
root.order.add_edge(xor_customs_clearance, xor_ledger_update)
root.order.add_edge(xor_ledger_update, xor_public_showcase)
root.order.add_edge(xor_public_showcase, xor_final_report)