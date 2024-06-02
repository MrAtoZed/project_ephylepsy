from glob import glob
import os
import mne
import numpy as np
import pandas
import matplotlib.pyplot as plt

all_file_path = glob('D:/project/Deteksi_Epilepsi/dataset/chb06/*.edf')#membaca semua file berformat .edf
#all_file_path[0]#mengambil data urutan pertama dari file tipe .edf

healthy_file_path = [i for i in all_file_path if 'h' in i.split('\\')[1]]#hanya menampilkan data yang terdapat karakter h
patient_file_path = [i for i in all_file_path if '01' in i.split('\\')[1]]#hanya menampilkan data yang terdapat karakter 01
print(len(healthy_file_path),len(patient_file_path))

def read_data(file_path):
    data=mne.io.read_raw_edf(file_path,preload=True)
    data.set_eeg_reference()
    data.filter(l_freq=0.5,h_freq=45)
    epochs=mne.make_fixed_length_epochs(data,duration=5,overlap=1)
    array=epochs.get_data()
    return array

sample_data=read_data(healthy_file_path[0])
print(sample_data.shape)

control_epochs_array=[read_data(i) for i in healthy_file_path]
patient_epochs_array=[read_data(i) for i in patient_file_path]

'''print(control_epochs_array[0].shape,control_epochs_array[1].shape)

control_epoch_labels=[len(i)*[0] for i in control_epochs_array]
patient_epoch_labels=[len(i)*[0] for i in patient_epochs_array]
print(len(control_epoch_labels),len(patient_epoch_labels))

data_list=control_epochs_array+patient_epochs_array
label_list=control_epoch_labels+patient_epoch_labels

group_list=[[i]*len(j) for i,j in enumerate(data_list)]
print(len(group_list))

data_array=np.vstack(data_list)
label_array=np.hstack(label_list)
group_array=np.hstack(group_list)
print(data_array.shape,label_array.shape,group_array.shape)'''