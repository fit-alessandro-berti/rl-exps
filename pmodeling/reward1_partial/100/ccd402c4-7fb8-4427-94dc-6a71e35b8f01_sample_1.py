from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
stakeholder_meet = Transition(label='Stakeholder Meet')
design_layout = Transition(label='Design Layout')
iot_install = Transition(label='IoT Install')
sensor_calibrate = Transition(label='Sensor Calibrate')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_sowing = Transition(label='Seed Sowing')
climate_control = Transition(label='Climate Control')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_plan = Transition(label='Energy Plan')
maintenance_plan = Transition(label='Maintenance Plan')
harvest_prep = Transition(label='Harvest Prep')
supply_dispatch = Transition(label='Supply Dispatch')
market_launch = Transition(label='Market Launch')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_filing,
        stakeholder_meet,
        design_layout,
        iot_install,
        sensor_calibrate,
        hydroponic_setup,
        nutrient_mix,
        seed_sowing,
        climate_control,
        data_monitor,
        yield_forecast,
        energy_plan,
        maintenance_plan,
        harvest_prep,
        supply_dispatch,
        market_launch
    ],
    order={
        (site_survey, permit_filing): 1,
        (site_survey, stakeholder_meet): 1,
        (permit_filing, design_layout): 1,
        (stakeholder_meet, design_layout): 1,
        (design_layout, iot_install): 1,
        (iot_install, sensor_calibrate): 1,
        (sensor_calibrate, hydroponic_setup): 1,
        (hydroponic_setup, nutrient_mix): 1,
        (nutrient_mix, seed_sowing): 1,
        (seed_sowing, climate_control): 1,
        (climate_control, data_monitor): 1,
        (data_monitor, yield_forecast): 1,
        (yield_forecast, energy_plan): 1,
        (energy_plan, maintenance_plan): 1,
        (maintenance_plan, harvest_prep): 1,
        (harvest_prep, supply_dispatch): 1,
        (supply_dispatch, market_launch): 1
    }
)

# Add the dependencies between activities
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(permit_filing, design_layout)
root.order.add_edge(stakeholder_meet, design_layout)
root.order.add_edge(design_layout, iot_install)
root.order.add_edge(iot_install, sensor_calibrate)
root.order.add_edge(sensor_calibrate, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_sowing)
root.order.add_edge(seed_sowing, climate_control)
root.order.add_edge(climate_control, data_monitor)
root.order.add_edge(data_monitor, yield_forecast)
root.order.add_edge(yield_forecast, energy_plan)
root.order.add_edge(energy_plan, maintenance_plan)
root.order.add_edge(maintenance_plan, harvest_prep)
root.order.add_edge(harvest_prep, supply_dispatch)
root.order.add_edge(supply_dispatch, market_launch)

print(root)