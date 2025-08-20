import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
A = Transition(label='Boil salted water')
B = Transition(label='Boil spaghetti')
C = Transition(label='Enjoy Spaghetti Carbonara')
D = Transition(label='Gather ingredients')
E = Transition(label='Mix with egg mixture and pancetta')
F = Transition(label='Plan how to cook')
G = Transition(label='Plate and garnish dish')
H = Transition(label='Pour egg yolk and cheese mixture')
I = Transition(label='Saute pancetta until crispy')
J = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Define the partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J])

# Add dependencies to the partial order
root.order.add_edge(F, D)  # Plan how to cook -> Gather ingredients
root.order.add_edge(D, A)  # Gather ingredients -> Boil salted water
root.order.add_edge(A, B)  # Boil salted water -> Boil spaghetti
root.order.add_edge(B, E)  # Boil spaghetti -> Mix with egg mixture and pancetta
root.order.add_edge(E, H)  # Mix with egg mixture and pancetta -> Pour egg yolk and cheese mixture
root.order.add_edge(H, G)  # Pour egg yolk and cheese mixture -> Plate and garnish dish
root.order.add_edge(G, C)  # Plate and garnish dish -> Enjoy Spaghetti Carbonara
root.order.add_edge(D, I)  # Gather ingredients -> Saute pancetta until crispy
root.order.add_edge(I, J)  # Saute pancetta until crispy -> Whisk egg yolks, Parmesan, and black pepper
root.order.add_edge(J, E)  # Whisk egg yolks, Parmesan, and black pepper -> Mix with egg mixture and pancetta

root