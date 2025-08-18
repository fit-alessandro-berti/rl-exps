from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
seed_selection = Transition(label='Seed Selection')
nutrient_setup = Transition(label='Nutrient Setup')
growth_monitoring = Transition(label='Growth Monitoring')
climate_adjust = Transition(label='Climate Adjust')
pest_control = Transition(label='Pest Control')
water_recirculate = Transition(label='Water Recirculate')
light_calibration = Transition(label='Light Calibration')
robotic_harvest = Transition(label='Robotic Harvest')
quality_inspect = Transition(label='Quality Inspect')
waste_process = Transition(label='Waste Process')
energy_reuse = Transition(label='Energy Reuse')
inventory_update = Transition(label='Inventory Update')
demand_forecast = Transition(label='Demand Forecast')
order_dispatch = Transition(label='Order Dispatch')
community_event = Transition(label='Community Event')
feedback_collect = Transition(label='Feedback Collect')
data_analyze = Transition(label='Data Analyze')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        seed_selection,
        nutrient_setup,
        growth_monitoring,
        climate_adjust,
        pest_control,
        water_recirculate,
        light_calibration,
        robotic_harvest,
        quality_inspect,
        waste_process,
        energy_reuse,
        inventory_update,
        demand_forecast,
        order_dispatch,
        community_event,
        feedback_collect,
        data_analyze
    ],
    order=[
        (seed_selection, nutrient_setup),
        (nutrient_setup, growth_monitoring),
        (growth_monitoring, climate_adjust),
        (climate_adjust, pest_control),
        (pest_control, water_recirculate),
        (water_recirculate, light_calibration),
        (light_calibration, robotic_harvest),
        (robotic_harvest, quality_inspect),
        (quality_inspect, waste_process),
        (waste_process, energy_reuse),
        (energy_reuse, inventory_update),
        (inventory_update, demand_forecast),
        (demand_forecast, order_dispatch),
        (order_dispatch, community_event),
        (community_event, feedback_collect),
        (feedback_collect, data_analyze)
    ]
)