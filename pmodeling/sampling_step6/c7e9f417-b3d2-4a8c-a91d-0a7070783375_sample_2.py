from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
brand_audit = Transition(label='Brand Audit')
equity_review = Transition(label='Equity Review')
market_analysis = Transition(label='Market Analysis')
legal_clearance = Transition(label='Legal Clearance')
trademark_check = Transition(label='Trademark Check')
portfolio_merge = Transition(label='Portfolio Merge')
customer_sync = Transition(label='Customer Sync')
cultural_align = Transition(label='Cultural Align')
internal_brief = Transition(label='Internal Brief')
campaign_design = Transition(label='Campaign Design')
resource_plan = Transition(label='Resource Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')
launch_prep = Transition(label='Launch Prep')
feedback_loop = Transition(label='Feedback Loop')
performance_track = Transition(label='Performance Track')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    brand_audit, equity_review, market_analysis, legal_clearance,
    trademark_check, portfolio_merge, customer_sync, cultural_align,
    internal_brief, campaign_design, resource_plan, stakeholder_meet,
    launch_prep, feedback_loop, performance_track
])
# The root model is already fully defined and does not require any further dependencies or edges.

# Now 'root' contains the complete POWL model for the process described.