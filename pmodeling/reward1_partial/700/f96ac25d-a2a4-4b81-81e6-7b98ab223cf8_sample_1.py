import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
Client_Brief = Transition(label='Client Brief')
Concept_Sketch = Transition(label='Concept Sketch')
Design_Review = Transition(label='Design Review')
Material_Sourcing = Transition(label='Material Sourcing')
Prototype_Build = Transition(label='Prototype Build')
Vendor_Coordination = Transition(label='Vendor Coordination')
Quality_Check = Transition(label='Quality Check')
Client_Approval = Transition(label='Client Approval')
Packaging_Prep = Transition(label='Packaging Prep')
Shipping_Arrange = Transition(label='Shipping Arrange')
Feedback_Collect = Transition(label='Feedback Collect')
Portfolio_Update = Transition(label='Portfolio Update')
Contract_Sign = Transition(label='Contract Sign')
IP_Management = Transition(label='IP Management')
Future_Schedule = Transition(label='Future Schedule')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Client_Brief,
    Concept_Sketch,
    Design_Review,
    Material_Sourcing,
    Prototype_Build,
    Vendor_Coordination,
    Quality_Check,
    Client_Approval,
    Packaging_Prep,
    Shipping_Arrange,
    Feedback_Collect,
    Portfolio_Update,
    Contract_Sign,
    IP_Management,
    Future_Schedule,
    Maintenance_Plan
])

# Define the edges (dependencies) in the partial order
root.order.add_edge(Client_Brief, Concept_Sketch)
root.order.add_edge(Concept_Sketch, Design_Review)
root.order.add_edge(Design_Review, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Prototype_Build)
root.order.add_edge(Prototype_Build, Vendor_Coordination)
root.order.add_edge(Vendor_Coordination, Quality_Check)
root.order.add_edge(Quality_Check, Client_Approval)
root.order.add_edge(Client_Approval, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Shipping_Arrange)
root.order.add_edge(Shipping_Arrange, Feedback_Collect)
root.order.add_edge(Feedback_Collect, Portfolio_Update)
root.order.add_edge(Portfolio_Update, Contract_Sign)
root.order.add_edge(Contract_Sign, IP_Management)
root.order.add_edge(IP_Management, Future_Schedule)
root.order.add_edge(Future_Schedule, Maintenance_Plan)