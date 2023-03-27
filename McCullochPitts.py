import random

# McCulloch-Pitts neuron


class McCullochPitts:
    def __init__(self, n_bits, gate, epoch):
        self.n_bits = n_bits
        self.gate = gate
        self.epoch = epoch
        self.threshold = random.randint(-1, 1)
        self.weights = [random.randint(1, 10) for _ in range(n_bits)]

# Activation function - returns 1 if the sum of the inputs is greater than or equal to the threshold
    def activation(self, inputs):
        suma = sum([weight * input for weight,
                   input in zip(self.weights, inputs)])
        return suma >= self.threshold if self.threshold <= 0 else suma == self.threshold

# Training function - trains the neuron to perform the desired logic gate
# The training is done by adjusting the threshold and weights,
# and it is done until the neuron is able to perform the desired logic gate
    def train(self):
        if self.gate == "NOT" and self.n_bits != 1:
            print("NOT gate only works with 1 bit.")
            return SystemExit
        
        for ep in range(self.epoch):
            for input, expected_output in self.truth_table():
                obtained_output = self.activation(input)
                if expected_output != obtained_output:
                    sign = 1 if expected_output > obtained_output else -1
                    self.threshold += sign
                    self.weights = [weight + sign * input[i]
                                    for i, weight in enumerate(self.weights)]
        
        print(f"Training successful in {self.epoch} epochs.")
        print("------------------------------------")
        print(f"Threshold value: {self.threshold}")
        print(f"Weight values: {self.weights}")



# Evaluate function - evaluates the neuron with the given input
# Returns True if the output is the same as the expected output
    def evaluate(self, input):
        if len(input) != self.n_bits:
            print("The given bit string is not of the same length as the number of bits trained.")
            return SystemExit
        output = self.activation(input)
        expected_output = bool(self.truth_table()[int("".join(str(i) for i in input), 2)][1])
        print(f'Expected output: {expected_output}')
        print(f'Obtained output: {output}')
        print("------------------------------------")
    
        return output == expected_output

# Truth table function - returns the truth table of the desired logic gate
# The truth table is a list of tuples, where the first element is the input and the second element is the expected output
# The truth table is used to train the neuron
    def truth_table(self):
        n = self.n_bits
        if self.gate == "AND":
            return [([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)], int(all([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)]))) for i in range(2**n)]
        elif self.gate == "OR":
            return [([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)], int(any([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)]))) for i in range(2**n)]
        elif self.gate == "NOT":
            return [([0], 1), ([1], 0)]
        else:
            print("Unknown gate or in lowercase")
            raise SystemExit

# Truth table check function - checks if the neuron is able to perform the desired logic gate
# Returns True if the output is the same as the expected output
    def truth_table_check(self):
        for input, expected_output in self.truth_table():
            obtained_output = self.activation(input)
            expected_output = bool(expected_output)
            print(f"{input}:{obtained_output == expected_output}")
        print("------------------------------------")
            
