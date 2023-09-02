# Notes

## One Hot Encoding
| Binary | Gray Code | One Hot Encoding |
|:------:|:---------:|:----------------:|
| 000    | 000       | 00000001         |
| 001    | 001       | 00000010         |
| 010    | 011       | 00000100         |
| 011    | 010       | 00001000         |
| 100    | 110       | 00010000         |

## np_utils
### Install
```
>> conda install np_utils
>> conda list | grep np_utils
```

### Use
```
>> from keras.utils import to_categorical
```