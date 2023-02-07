#tutorial: https://www.youtube.com/watch?v=mYUyaKmvu6Y&t=970s&ab_channel=freeCodeCamp.org


# Audio file formats
# mp3
# flac
# wav  audio quality is best, but file is largest

import wave

# audio signal parameters
# number of channels (one or two, one known as mono and two known as stereo)
# sample width(number of bytes for each sample)
# framrate/sample_rate (sample frequency, 44,100 hz means we get 44,100 samples each second)
# number of frames
# values of a frame (when loaded will be in binary, but can be converted to integer values latter)



#pip inistall pyaudio

obj = wave.open("/home/jesselunger/tmp/SchoolWork/Desktop/Cs472/project/Recording.wav", "rb")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()

print(t_audio)
frames = obj.readframes(-1) 
obj.close()

print(type(frames), type(frames[0]))
print(len(frames))

obj_new = wave.open("new_recording.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(48000.0)
obj_new.setnframes(144000)

obj_new.writeframes(frames)
obj_new.close()


#------------------------------chat gpt----------------------------

# import torch
# import torchvision
# import torchvision.transforms as transforms 


# transform = [transforms.ToTensor(),
#             transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))] 
            
# #method is used to stack multiple transforms into a single transform

# #load the trainset
# trainset = torchvision.datasets.CIFAR10(root= './data', train=True, download=True, transform=transform)

# #load the testset
# testset = torchvision.datasets.CIFAR10(root= './data', train=False, download=True, transform= transform)