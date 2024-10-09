"""Training script for the neural network."""

import torch
import torch.optim as optim
import torch.nn.functional as F
from model import ChessNet
from neural_network.data_recollection import process_pgn  


# PARAMETERS

learning_rate = 0.001
batch_size = 64
epochs = 20

net = ChessNet()
optimizer = optim.Adam(net.parameters(), lr=learning_rate)
# DATA LOAD
training_data = process_pgn('data/Modern.pgn')  
#TORCH TENSORS CONFIG
inputs = torch.stack([x[0] for x in training_data])  
targets = torch.tensor([x[1] for x in training_data])  

for epoch in range(epochs): #NVIDIA DEEP LEARNING IMPLEMENTATION
    running_loss = 0.0
    for i in range(0, len(inputs), batch_size):
        input_batch = inputs[i:i+batch_size]
        target_batch = targets[i:i+batch_size]
        
        optimizer.zero_grad()
        outputs = net(input_batch)
        loss = F.cross_entropy(outputs, target_batch)
        
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f'Epoch {epoch+1}, Loss: {running_loss}')
print("End training.")