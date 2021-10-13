import pandas as pd
from os import listdir
from os.path import isfile, join
import os
from utils import *
import glob
class preProcessing:

    def __init__(self, dir, dirAudio, dirText) -> None:
        self.dir = dir
        self.dirAudio = dirAudio
        self.dirText = dirText

    #   EMOTION PART 
    #   RETURN Dataframe file name of audio and target emotion
    def emotionDF(self):
        #Read folder of text files about emotion information(file name, target, election)
        allPathText = [self.dir + self.dirText + "/" + f for f in listdir(self.dir + self.dirText) if isfile(join(self.dir + self.dirText, f))]
        allFilesText = [f for f in listdir(self.dir + self.dirText) if isfile(join(self.dir + self.dirText, f))]

        l = list()
        for filepath in allPathText:
            with open(filepath) as fp:
                line = fp.readline()
                lines = [(line.split()[3],line.split()[4])  for line in fp if line[0] == "["]
                l.append(lines)

        emoAndText = [j for sub in l for j in sub]
        self.emoDF = pd.DataFrame(emoAndText, columns =['FileName', 'Emotion'])
        return self.emoDF


    def wavFilePath(self):
        # print(self.dir)
        # print(self.dirAudio)
        dirlist = [self.dir + self.dirAudio + item for item in os.listdir(self.dir + self.dirAudio) 
                                                if os.path.isdir(os.path.join(dir + self.dirAudio, item)) ]
        wavFile = []
        for folders in dirlist:
            folders = [ folders+'/'+f for f in listdir(folders) if isfile(join(folders, f ))]

            wavFile.append(folders)
        # wavFile[0] is the audio list of the first folder in Session1 
        # wavFile[1] is the audio list of the second folder in Session1 

        # all pahts of audio in Session1
        # emoAndText = [j for sub in wavFile for j in sub]
        # print("emoAndText", emoAndText[0])
        # self.audioPathDF = pd.DataFrame(emoAndText, columns =['FileName', 'FilePath', 'AllPathofFile' ])
        return wavFile


    #   WAVE PART
    #   RETURN DataFrame Path and name of Audio

    # def audioDF(self):

    #     #List of all audio folders
    #     dirlist = [ item for item in os.listdir(dir + self.dirAudio) if os.path.isdir(os.path.join(dir + self.dirAudio, item)) ]
        
    #     print("AudioPathList---------------------->>>>", AudioPathList[:2])

    #     allPathAudio = list()
    #     audioFiles = list()
    #     for eachSession0iFileAudio in dirlist:
    #         # Open each Audio file and append all audio path
    #         # self.dir + self.dirAudio + eachSession0iFileAudio, 
    #         audioFiles.append(dir + self.dirAudio + eachSession0iFileAudio for f in listdir(dir + self.dirAudio + eachSession0iFileAudio) 
    #                                                                                 if isfile(join(self.dir + self.dirAudio + eachSession0iFileAudio, f)))
    #         allPathAudio.append([(f.split(".wav")[0], self.dir + dirAudio + eachSession0iFileAudio, dir + dirAudio + eachSession0iFileAudio +'/' + f) 
    #                             for f in listdir(dir + dirAudio + eachSession0iFileAudio) if isfile(join(dir + dirAudio + eachSession0iFileAudio, f))])
        
    #     #2D list to 1D
    #     emoAndText = [j for sub in allPathAudio for j in sub]
        
    #     self.audioPathDF = pd.DataFrame(emoAndText, columns =['FileName', 'FilePath', 'AllPathofFile' ])
    #     return self.audioPathDF, audioFiles


    # # Join 2 DataFrame
    # def JoinAudioAndEmotionTarget(self):

    #     dfEmo = self.emotionDF()
    #     dfAudioPath, _ = self.audioDF()

    #     df = pd.concat([dfEmo, dfAudioPath[dfAudioPath.columns.difference(dfEmo.columns)]], axis=1).reindex(dfEmo.index)
        
    #     return df
        

# C:\Users\Gayane\Desktop\EmotionTask\Data\IEMOCAP_full_release\Session1\sentences\wav\Ses01F_impro01
dir = "C:/Users/Gayane/Desktop/EmotionTask/Data/IEMOCAP_full_release/"
dirAudio = "Session1/sentences/wav/"
dirText = "Session1/dialog/EmoEvaluation/"


obj = preProcessing(dir, dirAudio, dirText)
wavFoldersPaths =  obj.wavFilePath()
# print(obj.wavFilePath()[0])
sampling_rate = 16000
emoAndText = [j for sub in wavFoldersPaths for j in sub]
# print(len(emoAndText), len(emoAndText[0]), emoAndText[0])
wavs_A = load_wavs(wav_dir = emoAndText[43:46], sr = sampling_rate)

# f0s, coded_sps_norm, log_f0s_mean, log_f0s_std, coded_sps_mean, coded_sps_std = vocoder_extract(train_dir=wavFoldersPaths[0])















# # _, AudioPathList = obj.audioDF()
# # df = obj.JoinAudioAndEmotionTarget()


# # print("df---------------------->>>>", type(df['FilePath'].tolist()), type(df['FilePath'].tolist()[0]))
# # cwd = os.getcwd()

# # print("AllPathofFile---------------------->>>>", df['AllPathofFile'][0])
# # print("FilePath---------------------->>>>", df['FilePath'][0])
# print("AudioPathList---------------------->>>>", AudioPathList[:2])


# sampling_rate = 16000
# wavs_A = load_wavs(wav_dir = AudioPathList[:2], sr = sampling_rate)
# f1 = "C:/Users/Gayane/Desktop/EmotionTask/Data/IEMOCAP_full_release/Session1/sentences/wav/Ses01F_impro01/Ses01F_impro01_F000.wav"

# # wavs_A = load_wavs(wav_dir = df['FilePath'], sr = sampling_rate)
