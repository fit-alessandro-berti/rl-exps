import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    brand_audit,
    equity_review,
    market_analysis,
    legal_clearance,
    trademark_check,
    portfolio_merge,
    customer_sync,
    cultural_align,
    internal_brief,
    campaign_design,
    resource_plan,
    stakeholder_meet,
    launch_prep,
    feedback_loop,
    performance_track
])

# Define the dependencies
root.order.add_edge(brand_audit, equity_review)
root.order.add_edge(brand_audit, market_analysis)
root.order.add_edge(brand_audit, legal_clearance)
root.order.add_edge(brand_audit, trademark_check)
root.order.add_edge(brand_audit, portfolio_merge)
root.order.add_edge(brand_audit, customer_sync)
root.order.add_edge(brand_audit, cultural_align)
root.order.add_edge(brand_audit, internal_brief)
root.order.add_edge(brand_audit, campaign_design)
root.order.add_edge(brand_audit, resource_plan)
root.order.add_edge(brand_audit, stakeholder_meet)
root.order.add_edge(brand_audit, launch_prep)
root.order.add_edge(brand_audit, feedback_loop)
root.order.add_edge(brand_audit, performance_track)

# Print the root model
print(root)