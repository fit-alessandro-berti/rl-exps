import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Workshop_Host = Transition(label='Workshop Host')
Concept_Filter = Transition(label='Concept Filter')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
Feasibility_Check = Transition(label='Feasibility Check')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Performance_Review = Transition(label='Performance Review')
Scale_Plan = Transition(label='Scale Plan')
Resource_Align = Transition(label='Resource Align')
Learn_Share = Transition(label='Learn Share')
Culture_Embed = Transition(label='Culture Embed')

skip = SilentTransition()

# Steps 1-4: Trend Scan, Idea Harvest, Workshop Host, Concept Filter
step_1_4 = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[Trend_Scan, Idea_Harvest, Workshop_Host, Concept_Filter])

# Step 5: Prototype Build
step_5 = Prototype_Build

# Step 6: Expert Review
step_6 = Expert_Review

# Step 7: Feasibility Check
step_7 = Feasibility_Check

# Step 8: Risk Assess
step_8 = Risk_Assess

# Step 9: Pilot Launch
step_9 = Pilot_Launch

# Step 10: Data Capture
step_10 = Data_Capture

# Step 11: Performance Review
step_11 = Performance_Review

# Step 12: Scale Plan
step_12 = Scale_Plan

# Step 13: Resource Align
step_13 = Resource_Align

# Step 14: Learn Share
step_14 = Learn_Share

# Step 15: Culture Embed
step_15 = Culture_Embed

root = StrictPartialOrder(nodes=[step_1_4, step_5, step_6, step_7, step_8, step_9, step_10, step_11, step_12, step_13, step_14, step_15])
root.order.add_edge(step_1_4, step_5)
root.order.add_edge(step_5, step_6)
root.order.add_edge(step_6, step_7)
root.order.add_edge(step_7, step_8)
root.order.add_edge(step_8, step_9)
root.order.add_edge(step_9, step_10)
root.order.add_edge(step_10, step_11)
root.order.add_edge(step_11, step_12)
root.order.add_edge(step_12, step_13)
root.order.add_edge(step_13, step_14)
root.order.add_edge(step_14, step_15)