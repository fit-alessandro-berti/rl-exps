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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, restoration_track])
ownership_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_verify, appraisal_update])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_book, shipping_monitor, customs_clear])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_compliance])
ledger_loop = OperatorPOWL(operator=Operator.LOOP, children=[ledger_update])
exhibition_loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibition_setup, public_showcase, archival_prep])

# Construct the POWL model
root = StrictPartialOrder(
    nodes=[
        initial_audit,
        artist_review,
        material_check,
        condition_scan,
        ownership_loop,
        restoration_loop,
        shipping_loop,
        legal_loop,
        ledger_loop,
        exhibition_loop,
        final_report
    ],
    order={
        (initial_audit, artist_review),
        (initial_audit, material_check),
        (initial_audit, condition_scan),
        (artist_review, ownership_loop),
        (material_check, ownership_loop),
        (condition_scan, ownership_loop),
        (ownership_loop, restoration_loop),
        (restoration_loop, shipping_loop),
        (shipping_loop, legal_loop),
        (legal_loop, ledger_loop),
        (ledger_loop, exhibition_loop),
        (exhibition_loop, final_report)
    }
)