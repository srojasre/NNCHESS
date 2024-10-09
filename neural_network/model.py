import torch
import torch.nn as nn
import torch.nn.functional as F

class ChessNet(nn.Module):
    def __init__(self, input_channels=12, num_outputs=64 * 64):
        """
        Convolutional Neural Network for Chess move prediction.
        * Input channels: 12 (6 planes for white pieces + 6 planes for black pieces).
        * Output size: 4096 (64x64), representing the possible squares for legal moves (from -> to).
        """
        super(ChessNet, self).__init__()
        
        # Convolutional layers
        self.conv1 = nn.Conv2d(input_channels, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        
        # Fully connected layers for move prediction
        self.fc1 = nn.Linear(8 * 8 * 128, 1024)
        self.fc2 = nn.Linear(1024, num_outputs)  # Output is flattened move-space (64 'from' * 64 'to')
        
    def forward(self, x):
        # Pass through convolutional layers
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        
        # Flatten the output for fully connected layers
        x = x.view(x.size(0), -1)
        
        # Pass through fully connected layers
        x = F.relu(self.fc1(x))
        x = self.fc2(x)  # No activation for the final layer (we'll apply softmax or log_softmax later)
        
        return x