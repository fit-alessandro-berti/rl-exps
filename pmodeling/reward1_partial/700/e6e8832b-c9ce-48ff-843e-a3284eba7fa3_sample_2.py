import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
remote_valuation = OperatorPOWL(operator=Operator.LOOP, children=[valuation_check, compliance_scan, legal_review, remote_audit])
compliance_verification = OperatorPOWL(operator=Operator.LOOP, children=[compliance_scan, legal_review, remote_audit])
auction_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_setup, bid_monitoring, fraud_detection, ownership_transfer])
tax_calculation_loop = OperatorPOWL(operator=Operator.LOOP, children=[tax_calculation, fund_allocation, dispute_handling, report_generation])
stakeholder_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_update])

# Define the root model
root = StrictPartialOrder(nodes=[
    asset_listing,
    remote_valuation,
    compliance_verification,
    auction_setup_loop,
    tax_calculation_loop,
    stakeholder_update_loop
])
root.order.add_edge(remote_valuation, compliance_verification)
root.order.add_edge(compliance_verification, auction_setup_loop)
root.order.add_edge(auction_setup_loop, tax_calculation_loop)
root.order.add_edge(tax_calculation_loop, stakeholder_update_loop)

# Print the root model
print(root)