import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
patent_scouting      = Transition(label='Patent Scouting')
technical_review     = Transition(label='Technical Review')
legal_audit          = Transition(label='Legal Audit')
market_analysis      = Transition(label='Market Analysis')
valuation_modeling   = Transition(label='Valuation Modeling')
risk_assessment      = Transition(label='Risk Assessment')
license_targeting    = Transition(label='License Targeting')
buyer_outreach       = Transition(label='Buyer Outreach')
negotiation_phase    = Transition(label='Negotiation Phase')
contract_drafting    = Transition(label='Contract Drafting')
approval_process     = Transition(label='Approval Process')
portfolio_tracking   = Transition(label='Portfolio Tracking')
revenue_monitoring   = Transition(label='Revenue Monitoring')
compliance_check     = Transition(label='Compliance Check')
innovation_scan      = Transition(label='Innovation Scan')
renewal_management   = Transition(label='Renewal Management')

# Build the core sequential workflow
core_workflow = StrictPartialOrder(nodes=[
    patent_scouting, technical_review, legal_audit,
    market_analysis, valuation_modeling, risk_assessment,
    license_targeting, buyer_outreach, negotiation_phase,
    contract_drafting, approval_process, portfolio_tracking,
    revenue_monitoring, compliance_check
])
core_order = core_workflow.order
core_order.add_edge(patent_scouting,     technical_review)
core_order.add_edge(technical_review,    legal_audit)
core_order.add_edge(legal_audit,         market_analysis)
core_order.add_edge(market_analysis,     valuation_modeling)
core_order.add_edge(valuation_modeling,  risk_assessment)
core_order.add_edge(risk_assessment,     license_targeting)
core_order.add_edge(license_targeting,   buyer_outreach)
core_order.add_edge(buyer_outreach,      negotiation_phase)
core_order.add_edge(negotiation_phase,   contract_drafting)
core_order.add_edge(contract_drafting,   approval_process)
core_order.add_edge(approval_process,    portfolio_tracking)
core_order.add_edge(portfolio_tracking,  revenue_monitoring)
core_order.add_edge(revenue_monitoring,  compliance_check)

# Loop for continuous innovation monitoring
innovation_loop = OperatorPOWL(operator=Operator.LOOP, children=[innovation_scan, renewal_management])

# Assemble the final partial order
root = StrictPartialOrder(nodes=[
    core_workflow,
    innovation_loop
])
root.order.add_edge(core_workflow, innovation_loop)