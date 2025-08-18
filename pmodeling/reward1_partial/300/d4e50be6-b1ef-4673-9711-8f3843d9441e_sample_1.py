from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
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

skip = SilentTransition()

# Define the POWL operators for the process
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, technical_review])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, valuation_modeling])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, license_targeting])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, negotiation_phase])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, approval_process])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[portfolio_tracking, revenue_monitoring])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, innovation_scan])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[patent_scouting, exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8])
root.order.add_edge(patent_scouting, exclusive_choice_1)
root.order.add_edge(patent_scouting, exclusive_choice_2)
root.order.add_edge(patent_scouting, exclusive_choice_3)
root.order.add_edge(patent_scouting, exclusive_choice_4)
root.order.add_edge(patent_scouting, exclusive_choice_5)
root.order.add_edge(patent_scouting, exclusive_choice_6)
root.order.add_edge(patent_scouting, exclusive_choice_7)
root.order.add_edge(patent_scouting, exclusive_choice_8)