# -*- coding: utf-8 -*-
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa, librosa.display 
import cv2

n_data = np.load('N_samples.npy') 
s_data = np.load('S_samples.npy') 
v_data = np.load('V_samples.npy') 
f_data = np.load('F_samples.npy') 
q_data = np.load('Q_samples.npy')



n_fft_n= 256
win_length_n=64
hp_length_n=2
sr = 360 

data =n_data #?°ì´??ì¢…ë¥˜

lst = [] #npyë¡??€?¥í•  ?°ì´?°ë“¤
length = len(data) #ì¶œë ¥???°ì´??ê°œìˆ˜


for i in range(length):
    #?ë˜ ECG ê·¸ë˜??ê·¸ë¦¬ê¸?    #ax1 = fig1.add_subplot(length,2,2*(i+1)-1)
    #ax1.plot(data[i,0,:])
   
    # STFT ?´ë?ì§€ ê·¸ë¦¬ê¸?    #ax2 = fig1.add_subplot(length,2,2*(i+1))
             
    #STFT
    D_highres = librosa.stft(data[i,0,:].flatten(), n_fft=n_fft_n, hop_length=hp_length_n, win_length=win_length_n)
    
    #ampiltudeë¡?ë³€??    
    magnitude = np.abs(D_highres)
             
    #amplitudeë¥?db ?¤ì??¼ë¡œ ë³€??    
    
    log_spectrogram = librosa.amplitude_to_db(magnitude)
             
    #?”ì´???¸ì´ì¦??œê±°
    log_spectrogram = log_spectrogram[:,10:150]
             
    #128,128ë¡?resize
    log_spectrogram = cv2.resize(log_spectrogram, (64,64), interpolation = cv2.INTER_AREA)
    
    #?¤í™?¸ë¡œê·¸ë¨ ì¶œë ¥
    #img = librosa.display.specshow(log_spectrogram, sr=sr, hop_length = hp_length_n, ax=ax2, y_axis="linear", x_axis="time")
             
    #ì»¬ëŸ¬ë°?    #fig.colorbar(img, ax=ax2)# format="%+2.f dB")
    
    #print(log_spectrogram.shape)
    
    lst.append(log_spectrogram)
    if i%30==0:
        print(i,'/',length)

#npyë¡??€??
lst = np.array(lst)
output_filename = 'n_spectrogram'
print(lst.shape)
np.save(output_filename, lst)


##########

data =s_data #?°ì´??ì¢…ë¥˜

lst = [] #npyë¡??€?¥í•  ?°ì´?°ë“¤
length = len(data) #ì¶œë ¥???°ì´??ê°œìˆ˜


for i in range(length):
    #?ë˜ ECG ê·¸ë˜??ê·¸ë¦¬ê¸?    #ax1 = fig1.add_subplot(length,2,2*(i+1)-1)
    #ax1.plot(data[i,0,:])
   
    # STFT ?´ë?ì§€ ê·¸ë¦¬ê¸?    #ax2 = fig1.add_subplot(length,2,2*(i+1))
             
    #STFT
    D_highres = librosa.stft(data[i,0,:].flatten(), n_fft=n_fft_n, hop_length=hp_length_n, win_length=win_length_n)
    
    #ampiltudeë¡?ë³€??    
    magnitude = np.abs(D_highres)
             
    #amplitudeë¥?db ?¤ì??¼ë¡œ ë³€??    
    log_spectrogram = librosa.amplitude_to_db(magnitude)
             
    #?”ì´???¸ì´ì¦??œê±°
    log_spectrogram = log_spectrogram[:,10:150]
             
    #128,128ë¡?resize
    log_spectrogram = cv2.resize(log_spectrogram, (64,64), interpolation = cv2.INTER_AREA)
    
    #?¤í™?¸ë¡œê·¸ë¨ ì¶œë ¥
    #img = librosa.display.specshow(log_spectrogram, sr=sr, hop_length = hp_length_n, ax=ax2, y_axis="linear", x_axis="time")
             
    #ì»¬ëŸ¬ë°?    #fig.colorbar(img, ax=ax2)# format="%+2.f dB")
    
    #print(log_spectrogram.shape)
    
    lst.append(log_spectrogram)
    if i%30==0:
        print(i,'/',length)

#npyë¡??€??
lst = np.array(lst)
output_filename = 's_spectrogram'
print(lst.shape)
np.save(output_filename, lst)

##########

data =v_data #?°ì´??ì¢…ë¥˜

lst = [] #npyë¡??€?¥í•  ?°ì´?°ë“¤
length = len(data) #ì¶œë ¥???°ì´??ê°œìˆ˜


for i in range(length):
    #?ë˜ ECG ê·¸ë˜??ê·¸ë¦¬ê¸?    #ax1 = fig1.add_subplot(length,2,2*(i+1)-1)
    #ax1.plot(data[i,0,:])
   
    # STFT ?´ë?ì§€ ê·¸ë¦¬ê¸?    #ax2 = fig1.add_subplot(length,2,2*(i+1))
             
    #STFT
    D_highres = librosa.stft(data[i,0,:].flatten(), n_fft=n_fft_n, hop_length=hp_length_n, win_length=win_length_n)
    
    #ampiltudeë¡?ë³€??    
    magnitude = np.abs(D_highres)
             
    #amplitudeë¥?db ?¤ì??¼ë¡œ ë³€??    
    log_spectrogram = librosa.amplitude_to_db(magnitude)
             
    #?”ì´???¸ì´ì¦??œê±°
    log_spectrogram = log_spectrogram[:,10:150]
             
    #128,128ë¡?resize
    log_spectrogram = cv2.resize(log_spectrogram, (64,64), interpolation = cv2.INTER_AREA)
    
    #?¤í™?¸ë¡œê·¸ë¨ ì¶œë ¥
    #img = librosa.display.specshow(log_spectrogram, sr=sr, hop_length = hp_length_n, ax=ax2, y_axis="linear", x_axis="time")
             
    #ì»¬ëŸ¬ë°?    #fig.colorbar(img, ax=ax2)# format="%+2.f dB")
    
    #print(log_spectrogram.shape)
    
    lst.append(log_spectrogram)
    if i%30==0:
        print(i,'/',length)

#npyë¡??€??
lst = np.array(lst)
output_filename = 'v_spectrogram'
print(lst.shape)
np.save(output_filename, lst)

##########

data =f_data #?°ì´??ì¢…ë¥˜

lst = [] #npyë¡??€?¥í•  ?°ì´?°ë“¤
length = len(data) #ì¶œë ¥???°ì´??ê°œìˆ˜


for i in range(length):
    #?ë˜ ECG ê·¸ë˜??ê·¸ë¦¬ê¸?    #ax1 = fig1.add_subplot(length,2,2*(i+1)-1)
    #ax1.plot(data[i,0,:])
   
    # STFT ?´ë?ì§€ ê·¸ë¦¬ê¸?    #ax2 = fig1.add_subplot(length,2,2*(i+1))
             
    #STFT
    D_highres = librosa.stft(data[i,0,:].flatten(), n_fft=n_fft_n, hop_length=hp_length_n, win_length=win_length_n)
    
    #ampiltudeë¡?ë³€??    
    magnitude = np.abs(D_highres)
             
    #amplitudeë¥?db ?¤ì??¼ë¡œ ë³€??    
    log_spectrogram = librosa.amplitude_to_db(magnitude)
             
    #?”ì´???¸ì´ì¦??œê±°
    log_spectrogram = log_spectrogram[:,10:150]
             
    #128,128ë¡?resize
    log_spectrogram = cv2.resize(log_spectrogram, (64,64), interpolation = cv2.INTER_AREA)
    
    #?¤í™?¸ë¡œê·¸ë¨ ì¶œë ¥
    #img = librosa.display.specshow(log_spectrogram, sr=sr, hop_length = hp_length_n, ax=ax2, y_axis="linear", x_axis="time")
             
    #ì»¬ëŸ¬ë°?    #fig.colorbar(img, ax=ax2)# format="%+2.f dB")
    
    #print(log_spectrogram.shape)
    
    lst.append(log_spectrogram)
    if i%30==0:
        print(i,'/',length)

#npyë¡??€??
lst = np.array(lst)
output_filename = 'f_spectrogram'
print(lst.shape)
np.save(output_filename, lst)

##########

data =q_data #?°ì´??ì¢…ë¥˜

lst = [] #npyë¡??€?¥í•  ?°ì´?°ë“¤
length = len(data) #ì¶œë ¥???°ì´??ê°œìˆ˜


for i in range(length):
    #?ë˜ ECG ê·¸ë˜??ê·¸ë¦¬ê¸?    #ax1 = fig1.add_subplot(length,2,2*(i+1)-1)
    #ax1.plot(data[i,0,:])
   
    # STFT ?´ë?ì§€ ê·¸ë¦¬ê¸?    #ax2 = fig1.add_subplot(length,2,2*(i+1))
             
    #STFT
    D_highres = librosa.stft(data[i,0,:].flatten(), n_fft=n_fft_n, hop_length=hp_length_n, win_length=win_length_n)
    
    #ampiltudeë¡?ë³€??    
    magnitude = np.abs(D_highres)
             
    #amplitudeë¥?db ?¤ì??¼ë¡œ ë³€??    
    log_spectrogram = librosa.amplitude_to_db(magnitude)
             
    #?”ì´???¸ì´ì¦??œê±°
    log_spectrogram = log_spectrogram[:,10:150]
             
    #128,128ë¡?resize
    log_spectrogram = cv2.resize(log_spectrogram, (64,64), interpolation = cv2.INTER_AREA)
    
    #?¤í™?¸ë¡œê·¸ë¨ ì¶œë ¥
    #img = librosa.display.specshow(log_spectrogram, sr=sr, hop_length = hp_length_n, ax=ax2, y_axis="linear", x_axis="time")
             
    #ì»¬ëŸ¬ë°?    #fig.colorbar(img, ax=ax2)# format="%+2.f dB")
    
    #print(log_spectrogram.shape)
    
    lst.append(log_spectrogram)
    if i%30==0:
        print(i,'/',length)

#npyë¡??€??
lst = np.array(lst)
output_filename = 'q_spectrogram'
print(lst.shape)
np.save(output_filename, lst)
