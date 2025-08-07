import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
asset_listing    = Transition(label='Asset Listing')
valuation_check  = Transition(label='Valuation Check')
compliance_scan   = Transition(label='Compliance Scan')
legal_review     = Transition(label='Legal Review')
remote_audit     = Transition(label='Remote Audit')
auction_setup    = Transition(label='Auction Setup')
bid_monitoring   = Transition(label='Bid Monitoring')
fraud_detection  = Transition(label='Fraud Detection')
ownership_transfer=Transition(label='Ownership Transfer')
payment_clearing = Transition(label='Payment Clearing')
tax_calculation  = Transition(label='Tax Calculation')
fund_allocation  = Transition(label='Fund Allocation')
dispute_handling = Transition(label='Dispute Handling')
report_generation=Transition(label='Report Generation')
stakeholder_update=Transition(label='Stakeholder Update')

# Build the loop body: Auction Setup -> Bid Monitoring -> Fraud Detection -> Ownership Transfer
body = StrictPartialOrder(nodes=[auction_setup, bid_monitoring, fraud_detection, ownership_transfer])
body.order.add_edge(auction_setup, bid_monitoring)
body.order.add_edge(bid_monitoring, fraud_detection)
body.order.add_edge(fraud_detection, ownership_transfer)

# Define the loop: do the body, then either exit or repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    asset_listing,
    valuation_check,
    compliance_scan,
    legal_review,
    remote_audit,
    loop,
    payment_clearing,
    tax_calculation,
    fund_allocation,
    dispute_handling,
    report_generation,
    stakeholder_update
])

# Define the control-flow dependencies
root.order.add_edge(asset_listing, valuation_check)
root.order.add_edge(valuation_check, compliance_scan)
root.order.add_edge(compliance_scan, legal_review)
root.order.add_edge(legal_review, remote_audit)
root.order.add_edge(remote_audit, loop)
root.order.add_edge(loop, payment_clearing)
root.order.add_edge(payment_clearing, tax_calculation)
root.order.add_edge(tax_calculation, fund_allocation)
root.order.add_edge(fund_allocation, dispute_handling)
root.order.add_edge(dispute_handling, report_generation)
root.order.add_edge(report_generation, stakeholder_update)