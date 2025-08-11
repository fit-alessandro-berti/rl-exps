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
loop = OperatorPOWL(operator=Operator.LOOP, children=[Trend_Scan, Idea_Harvest, Workshop_Host, Concept_Filter, Prototype_Build, Expert_Review, Feasibility_Check, Risk_Assess, Pilot_Launch, Data_Capture, Performance_Review, Scale_Plan, Resource_Align, Learn_Share, Culture_Embed])
xor = OperatorPOWL(operator=Operator.XOR, children=[Pilot_Launch, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)