import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop nodes
portfolio_loop = OperatorPOWL(operator=Operator.LOOP, children=[portfolio_tracking, revenue_monitoring, compliance_check])

innovation_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[innovation_scan])

# Define exclusive choice nodes
risk_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive choice nodes
contract_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_drafting, skip])

# Define exclusive choice nodes
approval_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[approval_process, skip])

# Define exclusive choice nodes
renewal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[renewal_management, skip])

# Define exclusive choice nodes
patent_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[patent_scouting, skip])

# Define exclusive choice nodes
technical_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[technical_review, skip])

# Define exclusive choice nodes
legal_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])

# Define exclusive choice nodes
market_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define exclusive choice nodes
valuation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_modeling, skip])

# Define exclusive choice nodes
buyer_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[buyer_outreach, skip])

# Define exclusive choice nodes
license_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[license_targeting, skip])

# Define exclusive choice nodes
negotiation_exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiation_phase, skip])

# Define exclusive