import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Site_Acquisition = Transition(label='Site Acquisition')
Impact_Assess = Transition(label='Impact Assess')
Modular_Setup = Transition(label='Modular Setup')
Crop_Planting = Transition(label='Crop Planting')
Nutrient_Control = Transition(label='Nutrient Control')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Community_Engage = Transition(label='Community Engage')
Yield_Forecast = Transition(label='Yield Forecast')
Supply_Coordinate = Transition(label='Supply Coordinate')
Compliance_Check = Transition(label='Compliance Check')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Market_Strategy = Transition(label='Market Strategy')
Performance_Review = Transition(label='Performance Review')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Acquisition, Impact_Assess, Modular_Setup, Crop_Planting, Nutrient_Control, Pest_Control, Growth_Monitor, Community_Engage,
    Yield_Forecast, Supply_Coordinate, Compliance_Check, Waste_Recycle, Energy_Optimize, Market_Strategy, Performance_Review
])

# Define the partial order edges
root.order.add_edge(Site_Acquisition, Impact_Assess)
root.order.add_edge(Impact_Assess, Modular_Setup)
root.order.add_edge(Modular_Setup, Crop_Planting)
root.order.add_edge(Crop_Planting, Nutrient_Control)
root.order.add_edge(Nutrient_Control, Pest_Control)
root.order.add_edge(Pest_Control, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Community_Engage)
root.order.add_edge(Community_Engage, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Supply_Coordinate)
root.order.add_edge(Supply_Coordinate, Compliance_Check)
root.order.add_edge(Compliance_Check, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Energy_Optimize)
root.order.add_edge(Energy_Optimize, Market_Strategy)
root.order.add_edge(Market_Strategy, Performance_Review)