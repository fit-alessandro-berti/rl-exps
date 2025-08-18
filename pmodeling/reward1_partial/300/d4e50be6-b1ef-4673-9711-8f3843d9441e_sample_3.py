import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

patent_scouting_to_technical_review = OperatorPOWL(operator=Operator.LOOP, children=[patent_scouting, technical_review])
technical_review_to_legal_audit = OperatorPOWL(operator=Operator.LOOP, children=[technical_review, legal_audit])
legal_audit_to_market_analysis = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit, market_analysis])
market_analysis_to_valuation_modeling = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis, valuation_modeling])
valuation_modeling_to_risk_assessment = OperatorPOWL(operator=Operator.LOOP, children=[valuation_modeling, risk_assessment])
risk_assessment_to_license_targeting = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment, license_targeting])
license_targeting_to_buyer_outreach = OperatorPOWL(operator=Operator.LOOP, children=[license_targeting, buyer_outreach])
buyer_outreach_to_negotiation_phase = OperatorPOWL(operator=Operator.LOOP, children=[buyer_outreach, negotiation_phase])
negotiation_phase_to_contract_drafting = OperatorPOWL(operator=Operator.LOOP, children=[negotiation_phase, contract_drafting])
contract_drafting_to_approval_process = OperatorPOWL(operator=Operator.LOOP, children=[contract_drafting, approval_process])
approval_process_to_portfolio_tracking = OperatorPOWL(operator=Operator.LOOP, children=[approval_process, portfolio_tracking])
portfolio_tracking_to_revenue_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[portfolio_tracking, revenue_monitoring])
revenue_monitoring_to_compliance_check = OperatorPOWL(operator=Operator.LOOP, children=[revenue_monitoring, compliance_check])
compliance_check_to_innovation_scan = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, innovation_scan])
innovation_scan_to_renewal_management = OperatorPOWL(operator=Operator.LOOP, children=[innovation_scan, renewal_management])

root = StrictPartialOrder(nodes=[
    patent_scouting_to_technical_review,
    technical_review_to_legal_audit,
    legal_audit_to_market_analysis,
    market_analysis_to_valuation_modeling,
    valuation_modeling_to_risk_assessment,
    risk_assessment_to_license_targeting,
    license_targeting_to_buyer_outreach,
    buyer_outreach_to_negotiation_phase,
    negotiation_phase_to_contract_drafting,
    contract_drafting_to_approval_process,
    approval_process_to_portfolio_tracking,
    portfolio_tracking_to_revenue_monitoring,
    revenue_monitoring_to_compliance_check,
    compliance_check_to_innovation_scan,
    innovation_scan_to_renewal_management
])

root.order.add_edge(patent_scouting_to_technical_review, technical_review_to_legal_audit)
root.order.add_edge(technical_review_to_legal_audit, legal_audit_to_market_analysis)
root.order.add_edge(legal_audit_to_market_analysis, market_analysis_to_valuation_modeling)
root.order.add_edge(market_analysis_to_valuation_modeling, valuation_modeling_to_risk_assessment)
root.order.add_edge(valuation_modeling_to_risk_assessment, risk_assessment_to_license_targeting)
root.order.add_edge(risk_assessment_to_license_targeting, license_targeting_to_buyer_outreach)
root.order.add_edge(license_targeting_to_buyer_outreach, buyer_outreach_to_negotiation_phase)
root.order.add_edge(buyer_outreach_to_negotiation_phase, negotiation_phase_to_contract_drafting)
root.order.add_edge(negotiation_phase_to_contract_drafting, contract_drafting_to_approval_process)
root.order.add_edge(contract_drafting_to_approval_process, approval_process_to_portfolio_tracking)
root.order.add_edge(approval_process_to_portfolio_tracking, portfolio_tracking_to_revenue_monitoring)
root.order.add_edge(portfolio_tracking_to_revenue_monitoring, revenue_monitoring_to_compliance_check)
root.order.add_edge(revenue_monitoring_to_compliance_check, compliance_check_to_innovation_scan)
root.order.add_edge(compliance_check_to_innovation_scan, innovation_scan_to_renewal_management)