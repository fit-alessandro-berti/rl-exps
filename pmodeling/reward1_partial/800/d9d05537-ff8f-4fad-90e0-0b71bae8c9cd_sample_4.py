import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
Alert_Verify = Transition(label='Alert Verify')
Impact_Assess = Transition(label='Impact Assess')
Team_Assemble = Transition(label='Team Assemble')
Resource_Allocate = Transition(label='Resource Allocate')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Legal_Review = Transition(label='Legal Review')
Media_Brief = Transition(label='Media Brief')
Response_Deploy = Transition(label='Response Deploy')
Situation_Monitor = Transition(label='Situation Monitor')
Data_Collect = Transition(label='Data Collect')
Risk_Mitigate = Transition(label='Risk Mitigate')
Recovery_Plan = Transition(label='Recovery Plan')
External_Consult = Transition(label='External Consult')
Status_Update = Transition(label='Status Update')
Post_Review = Transition(label='Post Review')

# Define silent transition
skip = SilentTransition()

# Define partial order structure
root = StrictPartialOrder(nodes=[
    Alert_Verify,
    Impact_Assess,
    Team_Assemble,
    Resource_Allocate,
    Stakeholder_Notify,
    Legal_Review,
    Media_Brief,
    Response_Deploy,
    Situation_Monitor,
    Data_Collect,
    Risk_Mitigate,
    Recovery_Plan,
    External_Consult,
    Status_Update,
    Post_Review
])

# Define dependencies between nodes
root.order.add_edge(Alert_Verify, Impact_Assess)
root.order.add_edge(Impact_Assess, Team_Assemble)
root.order.add_edge(Team_Assemble, Resource_Allocate)
root.order.add_edge(Resource_Allocate, Stakeholder_Notify)
root.order.add_edge(Stakeholder_Notify, Legal_Review)
root.order.add_edge(Legal_Review, Media_Brief)
root.order.add_edge(Media_Brief, Response_Deploy)
root.order.add_edge(Response_Deploy, Situation_Monitor)
root.order.add_edge(Situation_Monitor, Data_Collect)
root.order.add_edge(Data_Collect, Risk_Mitigate)
root.order.add_edge(Risk_Mitigate, Recovery_Plan)
root.order.add_edge(Recovery_Plan, External_Consult)
root.order.add_edge(External_Consult, Status_Update)
root.order.add_edge(Status_Update, Post_Review)