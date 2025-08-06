import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
patent_scouting = Transition(label='Patent Scouting')
technical_review = Transition(label='Technical Review')
legal_audit = Transition(label='Legal Audit')
market_analysis = Transition(label='Market Analysis')
valuation_modeling = Transition(label='Valuation Modeling')
risk_assessment = Transition(label='Risk Assessment')
license_targeting = Transition(label='License Targeting')
buyer_outreach = Transition(label='Buyer Outreach')
negotiation_phase = Transition(label='Negotiation Phase')
contract_drafting = Transition(label='Contract Drafting')
approval_process = Transition(label='Approval Process')
portfolio_tracking = Transition(label='Portfolio Tracking')
revenue_monitoring = Transition(label='Revenue Monitoring')
compliance_check = Transition(label='Compliance Check')
innovation_scan = Transition(label='Innovation Scan')
renewal_management = Transition(label='Renewal Management')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define operators for exclusive choice
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip1])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip2])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip3])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip4])

# Define operators for loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[license_targeting, buyer_outreach])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[negotiation_phase, contract_drafting])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[approval_process, portfolio_tracking])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[revenue_monitoring, compliance_check])

# Define operators for partial order
partial_order1 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[exclusive_choice1, exclusive_choice2])
partial_order2 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[exclusive_choice3, exclusive_choice4])
partial_order3 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[loop1, loop2])
partial_order4 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[loop3, loop4])
partial_order5 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[partial_order1, partial_order2])
partial_order6 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[partial_order3, partial_order4])
partial_order7 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[partial_order5, partial_order6])
partial_order8 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[partial_order7, innovation_scan])
partial_order9 = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[partial_order8, renewal_management])

# Define the root POWL model
root = StrictPartialOrder(nodes=[patent_scouting, technical_review, exclusive_choice1, exclusive_choice2, exclusive_choice3, exclusive_choice4, loop1, loop2, loop3, loop4, partial_order1, partial_order2, partial_order3, partial_order4, partial_order5, partial_order6, partial_order7, partial_order8, partial_order9])

# Define the dependencies between nodes
root.order.add_edge(patent_scouting, technical_review)
root.order.add_edge(technical_review, exclusive_choice1)
root.order.add_edge(technical_review, exclusive_choice2)
root.order.add_edge(exclusive_choice1, loop1)
root.order.add_edge(exclusive_choice1, exclusive_choice3)
root.order.add_edge(exclusive_choice2, loop2)
root.order.add_edge(exclusive_choice2, exclusive_choice4)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, partial_order1)
root.order.add_edge(loop4, partial_order2)
root.order.add_edge(partial_order1, partial_order3)
root.order.add_edge(partial_order2, partial_order4)
root.order.add_edge(partial_order3, partial_order5)
root.order.add_edge(partial_order4, partial_order6)
root.order.add_edge(partial_order5, partial_order7)
root.order.add_edge(partial_order6, partial_order8)
root.order.add_edge(partial_order7, partial_order9)

# Return the root POWL model
return root