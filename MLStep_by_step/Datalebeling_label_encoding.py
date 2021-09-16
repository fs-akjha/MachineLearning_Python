import numpy as np
from sklearn import preprocessing

input_labels=['red','black','red','green','black','yellow','white']
encoder=preprocessing.LabelEncoder()
encoder.fit(input_labels)
test_labels=['green','red','black']
encoded_values=encoder.transform(test_labels)
print("\n Labels=",test_labels)
print("\n Encoded values=",list(encoded_values))
encoded_values=[3,0,4,1]
decoded_list=encoder.inverse_transform(encoded_values)
print("\n Encoded Values=",encoded_values)
print("\n Decoded Labels=",list(decoded_list))