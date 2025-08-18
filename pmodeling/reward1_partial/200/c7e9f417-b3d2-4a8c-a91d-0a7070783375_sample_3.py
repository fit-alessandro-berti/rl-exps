from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) in the process
Brand_Audit = Transition(label='Brand Audit')
Equity_Review = Transition(label='Equity Review')
Market_Analysis = Transition(label='Market Analysis')
Legal_Clearance = Transition(label='Legal Clearance')
Trademark_Check = Transition(label='Trademark Check')
Portfolio_Merge = Transition(label='Portfolio Merge')
Customer_Sync = Transition(label='Customer Sync')
Cultural_Align = Transition(label='Cultural Align')
Internal_Brief = Transition(label='Internal Brief')
Campaign_Design = Transition(label='Campaign Design')
Resource_Plan = Transition(label='Resource Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Launch_Preparation = Transition(label='Launch Prep')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Track = Transition(label='Performance Track')

# Define the silent transitions (no action)
skip = SilentTransition()

# Define the partial order model
root = StrictPartialOrder(nodes=[
    Brand_Audit,
    Equity_Review,
    Market_Analysis,
    Legal_Clearance,
    Trademark_Check,
    Portfolio_Merge,
    Customer_Sync,
    Cultural_Align,
    Internal_Brief,
    Campaign_Design,
    Resource_Plan,
    Stakeholder_Meet,
    Launch_Preparation,
    Feedback_Loop,
    Performance_Track
])

# Define the partial order relationships
root.order.add_edge(Brand_Audit, Equity_Review)
root.order.add_edge(Equity_Review, Market_Analysis)
root.order.add_edge(Market_Analysis, Legal_Clearance)
root.order.add_edge(Legal_Clearance, Trademark_Check)
root.order.add_edge(Trademark_Check, Portfolio_Merge)
root.order.add_edge(Portfolio_Merge, Customer_Sync)
root.order.add_edge(Customer_Sync, Cultural_Align)
root.order.add_edge(Cultural_Align, Internal_Brief)
root.order.add_edge(Internal_Brief, Campaign_Design)
root.order.add_edge(Campaign_Design, Resource_Plan)
root.order.add_edge(Resource_Plan, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Launch_Preparation)
root.order.add_edge(Launch_Preparation, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Performance_Track)

print(root)