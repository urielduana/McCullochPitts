# McCulloch-Pitts Neuron

This is a Python implementation of the McCulloch-Pitts Neuron. 

## Description

The McCulloch-Pitts Neuron is a simple model of a biological neuron that was first introduced by Warren McCulloch and Walter Pitts in 1943. The model takes in several binary inputs and produces a binary output based on a threshold function. 

## Usage

To use this implementation, simply create an instance of the `McCullochPitts` class and call the `train()` method to train the neuron. Once trained, you can call the `evaluate()` method to test the neuron with a given input. 

## Example

```python
from mcculloch_pitts_neuron import McCullochPitts

# Create a neuron with 2 input bits, an AND gate, and train for 10 epochs
neuron = McCullochPitts(n_bits=2, gate="AND", epochs=10)

# Train the neuron
neuron.train()

# Evaluate the neuron with an input of [0, 1]
neuron.evaluate([0, 1])
