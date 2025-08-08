from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Trend_Scan = Transition(label='Trend Scan')
Idea_Sprint = Transition(label='Idea Sprint')
Feasibility_Check = Transition(label='Feasibility Check')
Risk_Review = Transition(label='Risk Review')
Tech_Prototype = Transition(label='Tech Prototype')
Market_Simulate = Transition(label='Market Simulate')
Stakeholder_Align = Transition(label='Stakeholder Align')
Budget_Adjust = Transition(label='Budget Adjust')
Talent_Source = Transition(label='Talent Source')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Refine = Transition(label='Data Refine')
Scale_Analysis = Transition(label='Scale Analysis')
Integration_Plan = Transition(label='Integration Plan')
Change_Manage = Transition(label='Change Manage')
Knowledge_Transfer = Transition(label='Knowledge Transfer')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Trend_Scan, Idea_Sprint, Feasibility_Check, Risk_Review, Tech_Prototype, Market_Simulate,
    Stakeholder_Align, Budget_Adjust, Talent_Source, Pilot_Launch, Data_Refine, Scale_Analysis,
    Integration_Plan, Change_Manage, Knowledge_Transfer
])

# Define dependencies
root.order.add_edge(Trend_Scan, Idea_Sprint)
root.order.add_edge(Idea_Sprint, Feasibility_Check)
root.order.add_edge(Feasibility_Check, Risk_Review)
root.order.add_edge(Risk_Review, Tech_Prototype)
root.order.add_edge(Tech_Prototype, Market_Simulate)
root.order.add_edge(Market_Simulate, Stakeholder_Align)
root.order.add_edge(Stakeholder_Align, Budget_Adjust)
root.order.add_edge(Budget_Adjust, Talent_Source)
root.order.add_edge(Talent_Source, Pilot_Launch)
root.order.add_edge(Pilot_Launch, Data_Refine)
root.order.add_edge(Data_Refine, Scale_Analysis)
root.order.add_edge(Scale_Analysis, Integration_Plan)
root.order.add_edge(Integration_Plan, Change_Manage)
root.order.add_edge(Change_Manage, Knowledge_Transfer)