import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Env_Analysis = Transition(label='Env Analysis')
Modular_Install = Transition(label='Modular Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Selection = Transition(label='Crop Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Calibrate = Transition(label='Lighting Calibrate')
Pest_Monitor = Transition(label='Pest Monitor')
Staff_Training = Transition(label='Staff Training')
Energy_Integrate = Transition(label='Energy Integrate')
Data_Analytics = Transition(label='Data Analytics')
Waste_Recycle = Transition(label='Waste Recycle')
Market_Develop = Transition(label='Market Develop')
Yield_Optimize = Transition(label='Yield Optimize')
Climate_Simulate = Transition(label='Climate Simulate')

skip = SilentTransition()

# Site Assess -> Env Analysis -> Modular Install -> Irrigation Setup
site_env = OperatorPOWL(operator=Operator.XOR, children=[Site_Assess, Env_Analysis])
modular_irrigation = OperatorPOWL(operator=Operator.XOR, children=[Modular_Install, Irrigation_Setup])

# Irrigation Setup -> Nutrient Mix -> Lighting Calibrate -> Pest Monitor
irrigation_nutrient = OperatorPOWL(operator=Operator.XOR, children=[Irrigation_Setup, Nutrient_Mix])
lighting_pest = OperatorPOWL(operator=Operator.XOR, children=[Lighting_Calibrate, Pest_Monitor])

# Pest Monitor -> Staff Training -> Energy Integrate
pest_staff = OperatorPOWL(operator=Operator.XOR, children=[Pest_Monitor, Staff_Training])
energy_integration = OperatorPOWL(operator=Operator.XOR, children=[Energy_Integrate, skip])

# Staff Training -> Data Analytics -> Waste Recycle
staff_data = OperatorPOWL(operator=Operator.XOR, children=[Staff_Training, Data_Analytics])
waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[Waste_Recycle, skip])

# Data Analytics -> Market Develop -> Yield Optimize
data_market = OperatorPOWL(operator=Operator.XOR, children=[Data_Analytics, Market_Develop])
yield_optimize = OperatorPOWL(operator=Operator.XOR, children=[Yield_Optimize, skip])

# Market Develop -> Climate Simulate
market_climate = OperatorPOWL(operator=Operator.XOR, children=[Market_Develop, Climate_Simulate])

# Site Assess -> Irrigation Setup -> Nutrient Mix -> Lighting Calibrate -> Pest Monitor -> Staff Training -> Energy Integrate -> Data Analytics -> Waste Recycle -> Market Develop -> Yield Optimize -> Climate Simulate
root = StrictPartialOrder(nodes=[site_env, modular_irrigation, irrigation_nutrient, lighting_pest, pest_staff, energy_integration, staff_data, waste_recycle, data_market, yield_optimize, market_climate])
root.order.add_edge(site_env, modular_irrigation)
root.order.add_edge(modular_irrigation, irrigation_nutrient)
root.order.add_edge(irrigation_nutrient, lighting_pest)
root.order.add_edge(lighting_pest, pest_staff)
root.order.add_edge(pest_staff, energy_integration)
root.order.add_edge(energy_integration, staff_data)
root.order.add_edge(staff_data, waste_recycle)
root.order.add_edge(waste_recycle, data_market)
root.order.add_edge(data_market, yield_optimize)
root.order.add_edge(yield_optimize, market_climate)