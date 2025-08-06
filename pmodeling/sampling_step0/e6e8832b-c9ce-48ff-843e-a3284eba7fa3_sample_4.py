import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the POWL operators for each activity
valuation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[valuation_check])
compliance_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_scan])
legal_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review])
remote_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[remote_audit])
auction_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_setup])
bid_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitoring])
fraud_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[fraud_detection])
ownership_transfer_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_transfer])
payment_clearing_loop = OperatorPOWL(operator=Operator.LOOP, children=[payment_clearing])
tax_calculation_loop = OperatorPOWL(operator=Operator.LOOP, children=[tax_calculation])
fund_allocation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fund_allocation])
dispute_handling_loop = OperatorPOWL(operator=Operator.LOOP, children=[dispute_handling])
report_generation_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_generation])
stakeholder_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_update])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[
    valuation_check_loop,
    compliance_scan_loop,
    legal_review_loop,
    remote_audit_loop,
    auction_setup_loop,
    bid_monitoring_loop,
    fraud_detection_loop,
    ownership_transfer_loop,
    payment_clearing_loop,
    tax_calculation_loop,
    fund_allocation_loop,
    dispute_handling_loop,
    report_generation_loop,
    stakeholder_update_loop,
    asset_listing
])

# Define the order of execution for each activity
root.order.add_edge(valuation_check_loop, compliance_scan_loop)
root.order.add_edge(compliance_scan_loop, legal_review_loop)
root.order.add_edge(legal_review_loop, remote_audit_loop)
root.order.add_edge(remote_audit_loop, auction_setup_loop)
root.order.add_edge(auction_setup_loop, bid_monitoring_loop)
root.order.add_edge(bid_monitoring_loop, fraud_detection_loop)
root.order.add_edge(fraud_detection_loop, ownership_transfer_loop)
root.order.add_edge(ownership_transfer_loop, payment_clearing_loop)
root.order.add_edge(payment_clearing_loop, tax_calculation_loop)
root.order.add_edge(tax_calculation_loop, fund_allocation_loop)
root.order.add_edge(fund_allocation_loop, dispute_handling_loop)
root.order.add_edge(dispute_handling_loop, report_generation_loop)
root.order.add_edge(report_generation_loop, stakeholder_update_loop)
root.order.add_edge(stakeholder_update_loop, asset_listing)

# Print the POWL model
print(root)