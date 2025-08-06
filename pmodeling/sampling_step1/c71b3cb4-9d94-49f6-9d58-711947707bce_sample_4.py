import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
seedling_transplant = Transition(label='Seedling Transplant')
nutrient_mix = Transition(label='Nutrient Mix')
water_delivery = Transition(label='Water Delivery')
light_adjustment = Transition(label='Light Adjustment')
climate_control = Transition(label='Climate Control')
sensor_monitoring = Transition(label='Sensor Monitoring')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
harvest_planning = Transition(label='Harvest Planning')
crop_harvest = Transition(label='Crop Harvest')
waste_sorting = Transition(label='Waste Sorting')
biomass_process = Transition(label='Biomass Process')
energy_recycling = Transition(label='Energy Recycling')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        seed_selection,
        germination_start,
        seedling_transplant,
        nutrient_mix,
        water_delivery,
        light_adjustment,
        climate_control,
        sensor_monitoring,
        health_check,
        pest_control,
        harvest_planning,
        crop_harvest,
        waste_sorting,
        biomass_process,
        energy_recycling,
        data_analysis,
        yield_forecast
    ],
    order=[
        (seed_selection, germination_start),
        (germination_start, seedling_transplant),
        (seedling_transplant, nutrient_mix),
        (nutrient_mix, water_delivery),
        (water_delivery, light_adjustment),
        (light_adjustment, climate_control),
        (climate_control, sensor_monitoring),
        (sensor_monitoring, health_check),
        (health_check, pest_control),
        (pest_control, harvest_planning),
        (harvest_planning, crop_harvest),
        (crop_harvest, waste_sorting),
        (waste_sorting, biomass_process),
        (biomass_process, energy_recycling),
        (energy_recycling, data_analysis),
        (data_analysis, yield_forecast)
    ]
)