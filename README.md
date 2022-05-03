# Grasp-and-Lift-EEG-feature-extraction-using-CWT
A practical approach to classifying Grasp and Lift events of EEG signals using Continuous Wavelet Transform...


Talking about Wavelet Transform;
A wavelet is a wave-like oscillation that is localized in time, wavelets have two basic properties: scale and location. Scale defines how stretched or how compact the wavelet is. Location describes what position in time the wavelet is positioned. A typical example of a wavelet is the Morlet wavelet (morl).
In wavelet transform, the basic idea is to compute how much of a wavelet is in a signal for a particular scale and location. A wavelet with a particular scale is convolved across the entire signal in time. The result of this convolution or signal multiplication gives the coefficient for that wavelet scale at that time step, the process is then repeated with increase in the wavelet scale.
Continuous wavelet transform can be used to obtain a simultaneous time frequency analysis of a signal. The output of CWT are coefficients which are functions of scale or frequency and time. Each scaled wavelet is shifted in time along the entire length of the signal compared with the original signal. This process is repeated for all the scales, resulting in coefficients that are functions of the wavelet's scale and shift parameter. To put in perspective, a signal with 1500 samples analyzed with 20 scales results in 30,000 coefficients.

We want to extract features from EEG signals that would be useful in classifying events corresponding to waves extracted from the brain cells. This generally means that you convert the extracted brain waves into a kind of file that is readable or usable in some other software or program. 
In this project, we made use of the NeuroPype Pipeline designer application and the OpenBCI kit in the acquisition and recording of brain event, which is imported into a .xdf file.
The .xdf is therefore usable in our python program and can be converted into Amplitude vs Time format. Following this is the Wavelet Transform process used to extract features, and to convert the extracted features into a Scale vs Time representation which is called a Scalogram. Scalogram images of different images can be generated and used as classification dataset for multiple events. In this case, a grasp and lift events space. 
