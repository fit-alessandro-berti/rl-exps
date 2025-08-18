from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        patent_scouting, technical_review, legal_audit, market_analysis, valuation_modeling,
        risk_assessment, license_targeting, buyer_outreach, negotiation_phase, contract_drafting,
        approval_process, portfolio_tracking, revenue_monitoring, compliance_check, innovation_scan,
        renewal_management
    ],
    order=[
        (patent_scouting, technical_review),
        (technical_review, legal_audit),
        (legal_audit, market_analysis),
        (market_analysis, valuation_modeling),
        (valuation_modeling, risk_assessment),
        (risk_assessment, license_targeting),
        (license_targeting, buyer_outreach),
        (buyer_outreach, negotiation_phase),
        (negotiation_phase, contract_drafting),
        (contract_drafting, approval_process),
        (approval_process, portfolio_tracking),
        (portfolio_tracking, revenue_monitoring),
        (revenue_monitoring, compliance_check),
        (compliance_check, innovation_scan),
        (innovation_scan, renewal_management)
    ]
)

# Print the POWL model
print(root)