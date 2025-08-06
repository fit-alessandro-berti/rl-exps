import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
seed_select = Transition(label='Seed Select')
trend_analyze = Transition(label='Trend Analyze')
nutrient_mix = Transition(label='Nutrient Mix')
auto_plant = Transition(label='Auto Plant')
sensor_check = Transition(label='Sensor Check')
data_analyze = Transition(label='Data Analyze')
water_adjust = Transition(label='Water Adjust')
light_control = Transition(label='Light Control')
humidity_monitor = Transition(label='Humidity Monitor')
pest_inspect = Transition(label='Pest Inspect')
growth_forecast = Transition(label='Growth Forecast')
harvest_plan = Transition(label='Harvest Plan')
rapid_cool = Transition(label='Rapid Cool')
quality_grade = Transition(label='Quality Grade')
eco_package = Transition(label='Eco Package')
logistics_prep = Transition(label='Logistics Prep')
feedback_collect = Transition(label='Feedback Collect')
system_maintain = Transition(label='System Maintain')

# Define the nodes
trend_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[trend_analyze])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
auto_plant_loop = OperatorPOWL(operator=Operator.LOOP, children=[auto_plant])
sensor_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_check])
data_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze])
water_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_adjust])
light_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_control])
humidity_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity_monitor])
pest_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspect])
growth_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_forecast])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan])
rapid_cool_loop = OperatorPOWL(operator=Operator.LOOP, children=[rapid_cool])
quality_grade_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_grade])
eco_package_loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_package])
logistics_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_prep])
feedback_collect_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect])
system_maintain_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_maintain])

# Define the transitions
seed_select_next = Transition(label='Next')
trend_analyze_next = Transition(label='Next')
nutrient_mix_next = Transition(label='Next')
auto_plant_next = Transition(label='Next')
sensor_check_next = Transition(label='Next')
data_analyze_next = Transition(label='Next')
water_adjust_next = Transition(label='Next')
light_control_next = Transition(label='Next')
humidity_monitor_next = Transition(label='Next')
pest_inspect_next = Transition(label='Next')
growth_forecast_next = Transition(label='Next')
harvest_plan_next = Transition(label='Next')
rapid_cool_next = Transition(label='Next')
quality_grade_next = Transition(label='Next')
eco_package_next = Transition(label='Next')
logistics_prep_next = Transition(label='Next')
feedback_collect_next = Transition(label='Next')
system_maintain_next = Transition(label='Next')

# Define the partial order
root = StrictPartialOrder(nodes=[
    trend_analyze_loop,
    nutrient_mix_loop,
    auto_plant_loop,
    sensor_check_loop,
    data_analyze_loop,
    water_adjust_loop,
    light_control_loop,
    humidity_monitor_loop,
    pest_inspect_loop,
    growth_forecast_loop,
    harvest_plan_loop,
    rapid_cool_loop,
    quality_grade_loop,
    eco_package_loop,
    logistics_prep_loop,
    feedback_collect_loop,
    system_maintain_loop
])
root.order.add_edge(trend_analyze_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, auto_plant_loop)
root.order.add_edge(auto_plant_loop, sensor_check_loop)
root.order.add_edge(sensor_check_loop, data_analyze_loop)
root.order.add_edge(data_analyze_loop, water_adjust_loop)
root.order.add_edge(water_adjust_loop, light_control_loop)
root.order.add_edge(light_control_loop, humidity_monitor_loop)
root.order.add_edge(humidity_monitor_loop, pest_inspect_loop)
root.order.add_edge(pest_inspect_loop, growth_forecast_loop)
root.order.add_edge(growth_forecast_loop, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, rapid_cool_loop)
root.order.add_edge(rapid_cool_loop, quality_grade_loop)
root.order.add_edge(quality_grade_loop, eco_package_loop)
root.order.add_edge(eco_package_loop, logistics_prep_loop)
root.order.add_edge(logistics_prep_loop, feedback_collect_loop)
root.order.add_edge(feedback_collect_loop, system_maintain_loop)