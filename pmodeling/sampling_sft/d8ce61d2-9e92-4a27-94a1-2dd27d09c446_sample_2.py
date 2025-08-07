import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
initial_audit    = Transition(label='Initial Audit')
artist_review    = Transition(label='Artist Review')
material_check   = Transition(label='Material Check')
condition_scan   = Transition(label='Condition Scan')
ownership_verify = Transition(label='Ownership Verify')
appraisal_update = Transition(label='Appraisal Update')
restoration_plan = Transition(label='Restoration Plan')
restoration_track= Transition(label='Restoration Track')
logistics_book   = Transition(label='Logistics Book')
shipping_monitor = Transition(label='Shipping Monitor')
customs_clear    = Transition(label='Customs Clear')
legal_compliance = Transition(label='Legal Compliance')
ledger_update    = Transition(label='Ledger Update')
exhibition_setup = Transition(label='Exhibition Setup')
public_showcase  = Transition(label='Public Showcase')
archival_prep    = Transition(label='Archival Prep')
final_report     = Transition(label='Final Report')

# Build the loop body: restoration track, ledger update, exhibition setup, public showcase, archival prep
body = StrictPartialOrder(nodes=[restoration_track, ledger_update, exhibition_setup, public_showcase, archival_prep])
body.order.add_edge(restoration_track, ledger_update)
body.order.add_edge(ledger_update, exhibition_setup)
body.order.add_edge(exhibition_setup, public_showcase)
body.order.add_edge(public_showcase, archival_prep)

# Loop operator: do the initial activities, then either exit or do the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_audit, artist_review, material_check, condition_scan, ownership_verify, appraisal_update, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[loop, final_report])
root.order.add_edge(loop, final_report)