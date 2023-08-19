# Notes

## Training Concepts
one epoch = one forward pass and one backward pass of all the training examples

batch size = the number of training examples in one forward / backward pass. The higher the batch size, the more memory space you'll need.

number of iterations = number of passes, each pass using [batch size] number of examples. To be clear, one pass = one forward pass + one backward pass (we do not count the forward pass and backward pass as two different passes).

## TensorBoard
```
>> tensorboard --logdir ./ --host localhost 
```