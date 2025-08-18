import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the process flow
# Start with external trend scanning and internal ideation sprints
root = StrictPartialOrder(nodes=[Trend_Scan, Idea_Sprint])

# Add other activities sequentially
root.nodes.append(Feasibility_Check)
root.nodes.append(Risk_Review)
root.nodes.append(Tech_Prototype)
root.nodes.append(Market_Simulate)
root.nodes.append(Stakeholder_Align)
root.nodes.append(Budget_Adjust)
root.nodes.append(Talent_Source)
root.nodes.append(Pilot_Launch)
root.nodes.append(Data_Refine)
root.nodes.append(Scale_Analysis)
root.nodes.append(Integration_Plan)
root.nodes.append(Change_Manage)
root.nodes.append(Knowledge_Transfer)

# Define the order of execution
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