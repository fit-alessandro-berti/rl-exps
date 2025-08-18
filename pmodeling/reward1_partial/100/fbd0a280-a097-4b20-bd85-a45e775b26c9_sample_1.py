from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
seed_selection = Transition(label='Seed Selection')
germination_setup = Transition(label='Germination Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_control = Transition(label='Water Control')
climate_adjust = Transition(label='Climate Adjust')
sensor_monitor = Transition(label='Sensor Monitor')
lighting_tune = Transition(label='Lighting Tune')
airflow_manage = Transition(label='Airflow Manage')
health_scan = Transition(label='Health Scan')
pest_control = Transition(label='Pest Control')
harvest_timing = Transition(label='Harvest Timing')
cold_storage = Transition(label='Cold Storage')
package_prep = Transition(label='Package Prep')
delivery_plan = Transition(label='Delivery Plan')
feedback_loop = Transition(label='Feedback Loop')

# Define the loop for the operational cycle
operational_cycle = OperatorPOWL(operator=Operator.LOOP, children=[
    seed_selection,
    germination_setup,
    nutrient_mix,
    water_control,
    climate_adjust,
    sensor_monitor,
    lighting_tune,
    airflow_manage,
    health_scan,
    pest_control,
    harvest_timing,
    cold_storage,
    package_prep,
    delivery_plan,
    feedback_loop
])

# Define the partial order for the overall process
root = StrictPartialOrder(nodes=[operational_cycle])
root.order.add_edge(operational_cycle, operational_cycle)