import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop node for patent scouting
loop_patent_scouting = OperatorPOWL(operator=Operator.LOOP, children=[patent_scouting, technical_review])

# Define the choice node for technical review and legal audit
choice_technical_review_and_legal_audit = OperatorPOWL(operator=Operator.XOR, children=[technical_review, legal_audit])

# Define the choice node for market analysis and valuation modeling
choice_market_analysis_and_valuation_modeling = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, valuation_modeling])

# Define the choice node for risk assessment and license targeting
choice_risk_assessment_and_license_targeting = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, license_targeting])

# Define the choice node for buyer outreach and negotiation phase
choice_buyer_outreach_and_negotiation_phase = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, negotiation_phase])

# Define the choice node for contract drafting and approval process
choice_contract_drafting_and_approval_process = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, approval_process])

# Define the choice node for portfolio tracking and revenue monitoring
choice_portfolio_tracking_and_revenue_monitoring = OperatorPOWL(operator=Operator.XOR, children=[portfolio_tracking, revenue_monitoring])

# Define the choice node for compliance check and innovation scan
choice_compliance_check_and_innovation_scan = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, innovation_scan])

# Define the loop node for renewal management
loop_renewal_management = OperatorPOWL(operator=Operator.LOOP, children=[renewal_management])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_patent_scouting, choice_technical_review_and_legal_audit, choice_market_analysis_and_valuation_modeling, choice_risk_assessment_and_license_targeting, choice_buyer_outreach_and_negotiation_phase, choice_contract_drafting_and_approval_process, choice_portfolio_tracking_and_revenue_monitoring, choice_compliance_check_and_innovation_scan, loop_renewal_management])

# Define the edges
root.order.add_edge(loop_patent_scouting, choice_technical_review_and_legal_audit)
root.order.add_edge(loop_patent_scouting, choice_market_analysis_and_valuation_modeling)
root.order.add_edge(choice_technical_review_and_legal_audit, choice_risk_assessment_and_license_targeting)
root.order.add_edge(choice_technical_review_and_legal_audit, choice_buyer_outreach_and_negotiation_phase)
root.order.add_edge(choice_market_analysis_and_valuation_modeling, choice_contract_drafting_and_approval_process)
root.order.add_edge(choice_market_analysis_and_valuation_modeling, choice_portfolio_tracking_and_revenue_monitoring)
root.order.add_edge(choice_risk_assessment_and_license_targeting, choice_compliance_check_and_innovation_scan)
root.order.add_edge(choice_buyer_outreach_and_negotiation_phase, choice_contract_drafting_and_approval_process)
root.order.add_edge(choice_contract_drafting_and_approval_process, choice_portfolio_tracking_and_revenue_monitoring)
root.order.add_edge(choice_portfolio_tracking_and_revenue_monitoring, choice_compliance_check_and_innovation_scan)
root.order.add_edge(choice_compliance_check_and_innovation_scan, loop_renewal_management)

# Print the root
print(root)