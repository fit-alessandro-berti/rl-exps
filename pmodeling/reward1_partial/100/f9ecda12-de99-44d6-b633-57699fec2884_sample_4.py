import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Concept_Approve = Transition(label='Concept Approve')
Budget_Align = Transition(label='Budget Align')
Design_Review = Transition(label='Design Review')
Structure_Simulate = Transition(label='Structure Simulate')
Material_Procure = Transition(label='Material Procure')
Vendor_Select = Transition(label='Vendor Select')
Permit_Apply = Transition(label='Permit Apply')
Safety_Check = Transition(label='Safety Check')
Site_Prep = Transition(label='Site Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Fabricate_Parts = Transition(label='Fabricate Parts')
Assemble_Onsite = Transition(label='Assemble Onsite')
Quality_Inspect = Transition(label='Quality Inspect')
Weather_Monitor = Transition(label='Weather Monitor')
Public_Unveil = Transition(label='Public Unveil')
Maintenance_Plan = Transition(label='Maintenance Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

# Define exclusive choices and loops
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[Design_Review, Structure_Simulate])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[Material_Procure, Vendor_Select])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[Permit_Apply, Safety_Check])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[Site_Prep, Logistics_Plan])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[Fabricate_Parts, Assemble_Onsite])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[Quality_Inspect, Weather_Monitor])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[Public_Unveil, Maintenance_Plan])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Meet])

# Define the main partial order
root = StrictPartialOrder(nodes=[
    Concept_Approve, Budget_Align, exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4,
    exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8
])

# Define dependencies between activities
root.order.add_edge(Concept_Approve, Budget_Align)
root.order.add_edge(Budget_Align, exclusive_choice_1)
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, Public_Unveil)
root.order.add_edge(Public_Unveil, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Stakeholder_Meet)

print(root)