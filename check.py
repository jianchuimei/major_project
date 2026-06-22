from script.data_pipeline import load_data
import matplotlib.pyplot as plt
ds,vs,cn=load_data(r'dataset\data')
# print(dir(ds))
print("Printing...")
i=0
for bat, label in  ds:
    i+=1
    print(i)
    if i==2:
        print(i, (bat[0].shape))
        plt.imshow(bat[0])
        plt.title(cn[label[0]])
        plt.grid(False)
        plt.show()
    break