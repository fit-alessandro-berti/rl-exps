from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Design_Layout = Transition(label='Design Layout')
IoT_Install = Transition(label='IoT Install')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Sowing = Transition(label='Seed Sowing')
Climate_Control = Transition(label='Climate Control')
Data_Monitor = Transition(label='Data Monitor')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Plan = Transition(label='Energy Plan')
Maintenance_Plan = Transition(label='Maintenance Plan')
Harvest_Preparation = Transition(label='Harvest Prep')
Supply_Dispatch = Transition(label='Supply Dispatch')
Market_Launch = Transition(label='Market Launch')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Site_Survey, Permit_Filing, Stakeholder_Meet, Design_Layout,
    IoT_Install, Sensor_Calibrate, Hydroponic_Setup, Nutrient_Mix, Seed_Sowing,
    Climate_Control, Data_Monitor, Yield_Forecast, Energy_Plan, Maintenance_Plan,
    Harvest_Preparation, Supply_Dispatch, Market_Launch
])

# Define the dependencies
root.order.add_edge(Site_Survey, Permit_Filing)
root.order.add_edge(Permit_Filing, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Design_Layout)
root.order.add_edge(Design_Layout, IoT_Install)
root.order.add_edge(IoT_Install, Sensor_Calibrate)
root.order.add_edge(Sensor_Calibrate, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Sowing)
root.order.add_edge(Seed_Sowing, Climate_Control)
root.order.add_edge(Climate_Control, Data_Monitor)
root.order.add_edge(Data_Monitor, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Energy_Plan)
root.order.add_edge(Energy_Plan, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Harvest_Preparation)
root.order.add_edge(Harvest_Preparation, Supply_Dispatch)
root.order.add_edge(Supply_Dispatch, Market_Launch)

print(root)