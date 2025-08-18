import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
System_Assembly = Transition(label='System Assembly')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Prep = Transition(label='Nutrient Prep')
Water_Testing = Transition(label='Water Testing')
Climate_Setup = Transition(label='Climate Setup')
Data_Integration = Transition(label='Data Integration')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Waste_Sorting = Transition(label='Waste Sorting')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Pack = Transition(label='Produce Pack')
Energy_Audit = Transition(label='Energy Audit')
Community_Setup = Transition(label='Community Setup')

skip = SilentTransition()
Site_Survey_XOR = OperatorPOWL(operator=Operator.XOR, children=[Design_Layout, skip])
Design_Layout_XOR = OperatorPOWL(operator=Operator.XOR, children=[Material_Sourcing, skip])
Material_Sourcing_XOR = OperatorPOWL(operator=Operator.XOR, children=[System_Assembly, skip])
System_Assembly_XOR = OperatorPOWL(operator=Operator.XOR, children=[Sensor_Install, skip])
Sensor_Install_XOR = OperatorPOWL(operator=Operator.XOR, children=[Nutrient_Prep, skip])
Nutrient_Prep_XOR = OperatorPOWL(operator=Operator.XOR, children=[Water_Testing, skip])
Water_Testing_XOR = OperatorPOWL(operator=Operator.XOR, children=[Climate_Setup, skip])
Climate_Setup_XOR = OperatorPOWL(operator=Operator.XOR, children=[Data_Integration, skip])
Data_Integration_XOR = OperatorPOWL(operator=Operator.XOR, children=[Growth_Monitoring, skip])
Growth_Monitoring_XOR = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])
Pest_Control_XOR = OperatorPOWL(operator=Operator.XOR, children=[Waste_Sorting, skip])
Waste_Sorting_XOR = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, skip])
Harvest_Plan_XOR = OperatorPOWL(operator=Operator.XOR, children=[Produce_Pack, skip])
Produce_Pack_XOR = OperatorPOWL(operator=Operator.XOR, children=[Energy_Audit, skip])
Energy_Audit_XOR = OperatorPOWL(operator=Operator.XOR, children=[Community_Setup, skip])
Community_Setup_XOR = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])

root = StrictPartialOrder(nodes=[
    Site_Survey_XOR, 
    Design_Layout_XOR, 
    Material_Sourcing_XOR, 
    System_Assembly_XOR, 
    Sensor_Install_XOR, 
    Nutrient_Prep_XOR, 
    Water_Testing_XOR, 
    Climate_Setup_XOR, 
    Data_Integration_XOR, 
    Growth_Monitoring_XOR, 
    Pest_Control_XOR, 
    Waste_Sorting_XOR, 
    Harvest_Plan_XOR, 
    Produce_Pack_XOR, 
    Energy_Audit_XOR, 
    Community_Setup_XOR
])

root.order.add_edge(Site_Survey, Site_Survey_XOR)
root.order.add_edge(Design_Layout, Design_Layout_XOR)
root.order.add_edge(Material_Sourcing, Material_Sourcing_XOR)
root.order.add_edge(System_Assembly, System_Assembly_XOR)
root.order.add_edge(Sensor_Install, Sensor_Install_XOR)
root.order.add_edge(Nutrient_Prep, Nutrient_Prep_XOR)
root.order.add_edge(Water_Testing, Water_Testing_XOR)
root.order.add_edge(Climate_Setup, Climate_Setup_XOR)
root.order.add_edge(Data_Integration, Data_Integration_XOR)
root.order.add_edge(Growth_Monitoring, Growth_Monitoring_XOR)
root.order.add_edge(Pest_Control, Pest_Control_XOR)
root.order.add_edge(Waste_Sorting, Waste_Sorting_XOR)
root.order.add_edge(Harvest_Plan, Harvest_Plan_XOR)
root.order.add_edge(Produce_Pack, Produce_Pack_XOR)
root.order.add_edge(Energy_Audit, Energy_Audit_XOR)
root.order.add_edge(Community_Setup, Community_Setup_XOR)