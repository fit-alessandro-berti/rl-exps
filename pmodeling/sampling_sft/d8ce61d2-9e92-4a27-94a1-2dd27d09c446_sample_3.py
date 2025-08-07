import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
initial_audit      = Transition(label='Initial Audit')
artist_review      = Transition(label='Artist Review')
material_check     = Transition(label='Material Check')
condition_scan     = Transition(label='Condition Scan')
ownership_verify   = Transition(label='Ownership Verify')
appraisal_update   = Transition(label='Appraisal Update')
restoration_plan   = Transition(label='Restoration Plan')
restoration_track  = Transition(label='Restoration Track')
logistics_book     = Transition(label='Logistics Book')
shipping_monitor   = Transition(label='Shipping Monitor')
customs_clear      = Transition(label='Customs Clear')
legal_compliance   = Transition(label='Legal Compliance')
ledger_update      = Transition(label='Ledger Update')
exhibition_setup   = Transition(label='Exhibition Setup')
public_showcase    = Transition(label='Public Showcase')
archival_prep      = Transition(label='Archival Prep')
final_report       = Transition(label='Final Report')

# Silent transition for loop exit
skip = SilentTransition()

# Loop body: Restoration Track -> Logistics Book -> Shipping Monitor -> Customs Clear -> Legal Compliance -> Ledger Update
body = StrictPartialOrder(nodes=[restoration_track, logistics_book, shipping_monitor, customs_clear, legal_compliance, ledger_update])
body.order.add_edge(restoration_track, logistics_book)
body.order.add_edge(logistics_book, shipping_monitor)
body.order.add_edge(shipping_monitor, customs_clear)
body.order.add_edge(customs_clear, legal_compliance)
body.order.add_edge(legal_compliance, ledger_update)

# Loop: Initial Audit -> Artist Review -> Material Check -> Condition Scan -> Ownership Verify -> Appraisal Update
#       then either exit or execute the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_audit,
                                                      artist_review,
                                                      material_check,
                                                      condition_scan,
                                                      ownership_verify,
                                                      appraisal_update,
                                                      body,
                                                      skip])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[loop,
                                 exhibition_setup,
                                 public_showcase,
                                 archival_prep,
                                 final_report])

# Add the control-flow edges
root.order.add_edge(loop, exhibition_setup)
root.order.add_edge(exhibition_setup, public_showcase)
root.order.add_edge(public_showcase, archival_prep)
root.order.add_edge(archival_prep, final_report)