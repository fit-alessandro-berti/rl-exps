from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
loop_workshop = OperatorPOWL(operator=Operator.LOOP, children=[Workshop_Host, Concept_Filter])
parallel_feasibility = OperatorPOWL(operator=Operator.XOR, children=[Expert_Review, skip])
data_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Capture, Performance_Review])
risk_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Assess, skip])
resource_align_loop = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Align, skip])
learn_share_loop = OperatorPOWL(operator=Operator.LOOP, children=[Learn_Share, skip])

root = StrictPartialOrder(nodes=[
    Trend_Scan,
    Idea_Harvest,
    loop_workshop,
    parallel_feasibility,
    Feasibility_Check,
    Pilot_Launch,
    data_capture_loop,
    Performance_Review,
    Scale_Plan,
    risk_assessment_loop,
    resource_align_loop,
    learn_share_loop,
    Culture_Embed
])

root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Idea_Harvest, loop_workshop)
root.order.add_edge(loop_workshop, parallel_feasibility)
root.order.add_edge(parallel_feasibility, Feasibility_Check)
root.order.add_edge(Feasibility_Check, Pilot_Launch)
root.order.add_edge(Pilot_Launch, data_capture_loop)
root.order.add_edge(data_capture_loop, Performance_Review)
root.order.add_edge(Performance_Review, Scale_Plan)
root.order.add_edge(Scale_Plan, risk_assessment_loop)
root.order.add_edge(risk_assessment_loop, resource_align_loop)
root.order.add_edge(resource_align_loop, learn_share_loop)
root.order.add_edge(learn_share_loop, Culture_Embed)

print(root)