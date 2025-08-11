import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
asset_listing = Transition(label='Asset Listing')
valuation_check = Transition(label='Valuation Check')
compliance_scan = Transition(label='Compliance Scan')
legal_review = Transition(label='Legal Review')
remote_audit = Transition(label='Remote Audit')
auction_setup = Transition(label='Auction Setup')
bid_monitoring = Transition(label='Bid Monitoring')
fraud_detection = Transition(label='Fraud Detection')
ownership_transfer = Transition(label='Ownership Transfer')
payment_clearing = Transition(label='Payment Clearing')
tax_calculation = Transition(label='Tax Calculation')
fund_allocation = Transition(label='Fund Allocation')
dispute_handling = Transition(label='Dispute Handling')
report_generation = Transition(label='Report Generation')
stakeholder_update = Transition(label='Stakeholder Update')

# Define the silent transition (skip)
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[auction_setup, bid_monitoring])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[fraud_detection, dispute_handling])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[tax_calculation, fund_allocation])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[report_generation, stakeholder_update])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[compliance_scan, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[remote_audit, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[ownership_transfer, payment_clearing])

root = StrictPartialOrder(nodes=[asset_listing, valuation_check, xor1, xor2, xor3, loop1, loop2, loop3, loop4, xor4])
root.order.add_edge(asset_listing, xor1)
root.order.add_edge(asset_listing, xor2)
root.order.add_edge(asset_listing, xor3)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor4)
root.order.add_edge(xor4, loop4)