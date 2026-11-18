# Basic Bayesian Network

# Variables:
# Rain -> Wet Grass
# Sprinkler -> Wet Grass

# Prior probabilities
P_Rain = 0.2
P_Sprinkler = 0.3

# Conditional probability table
P_Wet_Grass = {
    (1, 1): 0.99,
    (1, 0): 0.90,
    (0, 1): 0.80,
    (0, 0): 0.01
}

# Calculate probability of wet grass
P_Wet = 0

for rain in [0, 1]:
    for sprinkler in [0, 1]:

        p_rain = P_Rain if rain else 1 - P_Rain
        p_sprinkler = (
            P_Sprinkler if sprinkler else 1 - P_Sprinkler
        )

        p_wet = P_Wet_Grass[(rain, sprinkler)]

        P_Wet += p_rain * p_sprinkler * p_wet

print("Bayesian Network Results")

print("Probability of Rain:", P_Rain)

print("Probability of Sprinkler:", P_Sprinkler)

print("Probability of Wet Grass:", round(P_Wet, 4))
