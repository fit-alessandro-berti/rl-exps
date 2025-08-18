import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
# Each activity is represented as a Transition
audit = Transition(label='Brand Audit')
review = Transition(label='Equity Review')
analysis = Transition(label='Market Analysis')
clearance = Transition(label='Legal Clearance')
trademark = Transition(label='Trademark Check')
portfolio = Transition(label='Portfolio Merge')
customer_sync = Transition(label='Customer Sync')
cultural_align = Transition(label='Cultural Align')
internal_brief = Transition(label='Internal Brief')
campaign_design = Transition(label='Campaign Design')
resource_plan = Transition(label='Resource Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')
launch_prep = Transition(label='Launch Prep')
feedback_loop = Transition(label='Feedback Loop')
performance_track = Transition(label='Performance Track')

# Define the control flow
root = StrictPartialOrder(nodes=[
    audit, review, analysis, clearance, trademark, portfolio, customer_sync,
    cultural_align, internal_brief, campaign_design, resource_plan,
    stakeholder_meet, launch_prep, feedback_loop, performance_track
])

# Define the partial order of activities
root.order.add_edge(audit, review)
root.order.add_edge(review, analysis)
root.order.add_edge(analysis, clearance)
root.order.add_edge(clearance, trademark)
root.order.add_edge(trademark, portfolio)
root.order.add_edge(portfolio, customer_sync)
root.order.add_edge(customer_sync, cultural_align)
root.order.add_edge(cultural_align, internal_brief)
root.order.add_edge(internal_brief, campaign_design)
root.order.add_edge(campaign_design, resource_plan)
root.order.add_edge(resource_plan, stakeholder_meet)
root.order.add_edge(stakeholder_meet, launch_prep)
root.order.add_edge(launch_prep, feedback_loop)
root.order.add_edge(feedback_loop, performance_track)

# Print the POWL model
print(root)