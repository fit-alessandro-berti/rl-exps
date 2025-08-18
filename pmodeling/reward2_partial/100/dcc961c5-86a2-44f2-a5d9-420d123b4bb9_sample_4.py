from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permit_Acquire = Transition(label='Permit Acquire')
Modular_Build = Transition(label='Modular Build')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Pest_Control = Transition(label='Pest Control')
Energy_Audit = Transition(label='Energy Audit')
Sensor_Install = Transition(label='Sensor Install')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Process = Transition(label='Waste Process')
Data_Analysis = Transition(label='Data Analysis')
Staff_Train = Transition(label='Staff Train')
Community_Link = Transition(label='Community Link')
Yield_Report = Transition(label='Yield Report')

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Layout, Permit_Acquire, Modular_Build, Climate_Setup, Nutrient_Mix,
    Seed_Automation, Pest_Control, Energy_Audit, Sensor_Install, Growth_Monitor, Waste_Process,
    Data_Analysis, Staff_Train, Community_Link, Yield_Report
])

# Define the dependencies
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Permit_Acquire)
root.order.add_edge(Permit_Acquire, Modular_Build)
root.order.add_edge(Modular_Build, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Automation)
root.order.add_edge(Seed_Automation, Pest_Control)
root.order.add_edge(Pest_Control, Energy_Audit)
root.order.add_edge(Energy_Audit, Sensor_Install)
root.order.add_edge(Sensor_Install, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Waste_Process)
root.order.add_edge(Waste_Process, Data_Analysis)
root.order.add_edge(Data_Analysis, Staff_Train)
root.order.add_edge(Staff_Train, Community_Link)
root.order.add_edge(Community_Link, Yield_Report)

print(root)