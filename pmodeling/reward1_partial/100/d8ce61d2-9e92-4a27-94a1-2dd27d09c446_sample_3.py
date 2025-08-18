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

# Define the loop for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[
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
    archival_prep
])

# Define the exclusive choice for the process
xor = OperatorPOWL(operator=Operator.XOR, children=[final_report, SilentTransition()])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)