# Chess Neural Network

Welcome to the Chess Neural Network project! This project utilizes a neural network model to play the game of chess. The aim is to develop a model that can compete at various levels, improving its gameplay through machine learning techniques.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)


## Introduction

This project involves the creation and training of a neural network capable of playing chess. Leveraging the power of machine learning, the model is trained on various chess positions and games to understand strategic and tactical elements of gameplay, is currently not finish so don't expect to fully work. The only 100% part that is finish is de pygame render of the game, legal moves and moves story.

## Installation

Before running the project, make sure you have Python [At least >=3.11 ] installed on your system. You can then install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To start using the chess neural network, follow these steps:

1. Clone the repository in your desire workspace:
   ```bash
   git clone https://github.com/srojasre/NNCHESS.git
   cd NNCHESS
   ```

2. For just starting a normal chess game just run
   ```bash
   python run_game.py
   ```

3. For training the model modify the training data path with the wished pgn and run
```bash
   python train.py
   ```


## Model Architecture

For the model we are using Convolutional Neural Network for Chess move prediction.
        * Input channels: 12 (6 planes for white pieces + 6 planes for black pieces).
        * Output size: 4096 (64x64), representing the possible squares for legal moves (from -> to).

## Training

WIP

## Evaluation

WIP

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Open a Pull Request.
