from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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
skip = SilentTransition()

# Define sub-processes
due_diligence = StrictPartialOrder(nodes=[technical_review, legal_audit, market_analysis, valuation_modeling, risk_assessment])
targeting = StrictPartialOrder(nodes=[license_targeting, buyer_outreach, negotiation_phase, contract_drafting, approval_process])
portfolio = StrictPartialOrder(nodes=[portfolio_tracking, revenue_monitoring, compliance_check])
innovation = StrictPartialOrder(nodes=[innovation_scan, renewal_management])

# Define root process
root = StrictPartialOrder(nodes=[patent_scouting, due_diligence, targeting, portfolio, innovation])

# Define dependencies
root.order.add_edge(patent_scouting, due_diligence)
root.order.add_edge(due_diligence, targeting)
root.order.add_edge(targeting, portfolio)
root.order.add_edge(portfolio, innovation)

print(root)