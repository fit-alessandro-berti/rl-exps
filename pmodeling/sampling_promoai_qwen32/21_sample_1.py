import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
BoilSaltedWater = Transition(label='Boil salted water')
BoilSpaghetti = Transition(label='Boil spaghetti')
EnjoySpaghettiCarbonara = Transition(label='Enjoy Spaghetti Carbonara')
GatherIngredients = Transition(label='Gather ingredients')
MixWithEggMixtureAndPancetta = Transition(label='Mix with egg mixture and pancetta')
PlanHowToCook = Transition(label='Plan how to cook')
PlateAndGarnishDish = Transition(label='Plate and garnish dish')
PourEggYolkAndCheeseMixture = Transition(label='Pour egg yolk and cheese mixture')
SautePancettaUntilCrispy = Transition(label='Saute pancetta until crispy')
WhiskEggYolksParmesanAndBlackPepper = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Define control flow structures
plan = OperatorPOWL(operator=Operator.LOOP, children=[PlanHowToCook])
gather = OperatorPOWL(operator=Operator.XOR, children=[GatherIngredients])
boilWater = OperatorPOWL(operator=Operator.XOR, children=[BoilSaltedWater])
boilSpaghetti = OperatorPOWL(operator=Operator.XOR, children=[BoilSpaghetti])
sautePancetta = OperatorPOWL(operator=Operator.XOR, children=[SautePancettaUntilCrispy])
whiskEggYolks = OperatorPOWL(operator=Operator.XOR, children=[WhiskEggYolksParmesanAndBlackPepper])
pourEggYolk = OperatorPOWL(operator=Operator.XOR, children=[PourEggYolkAndCheeseMixture])
mixEggMixture = OperatorPOWL(operator=Operator.XOR, children=[MixWithEggMixtureAndPancetta])
plateDish = OperatorPOWL(operator=Operator.XOR, children=[PlateAndGarnishDish])
enjoyDish = OperatorPOWL(operator=Operator.XOR, children=[EnjoySpaghettiCarbonara])

# Define the root node
root = StrictPartialOrder(nodes=[plan, gather, boilWater, boilSpaghetti, sautePancetta, whiskEggYolks, pourEggYolk, mixEggMixture, plateDish, enjoyDish])
root.order.add_edge(plan, gather)
root.order.add_edge(gather, boilWater)
root.order.add_edge(boilWater, boilSpaghetti)
root.order.add_edge(boilSpaghetti, sautePancetta)
root.order.add_edge(sautePancetta, whiskEggYolks)
root.order.add_edge(whiskEggYolks, pourEggYolk)
root.order.add_edge(pourEggYolk, mixEggMixture)
root.order.add_edge(mixEggMixture, plateDish)
root.order.add_edge(plateDish, enjoyDish)