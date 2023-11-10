import pyaudio

def record(self):
		pa = PyAudio()
		in_stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=BUFFER_SIZE)
		save_count = 0
		save_buffer = []

		save_count = SAVE_LENGTH
		
		print 'start recording'
		while save_count>0:
			string_audio_data = in_stream.read(BUFFER_SIZE)
			audio_data = np.fromstring(string_audio_data, dtype=np.short)
			save_buffer.append( string_audio_data )
			save_count = save_count - 1

		print 'save %s' % (self.fileName)
		pa.terminate()
		
		wf = wave.open(self.fileName, 'wb')
		wf.setnchannels(1)
		wf.setsampwidth(2)
		wf.setframerate(SAMPLING_RATE)
		wf.writeframes("".join(save_buffer))
		wf.close()
		
		self.stringAudioData = "".join(save_buffer)
		save_data = np.fromstring(self.stringAudioData, dtype=np.short)
		self.audioData = save_data[10000:10000+4608*4]
		self.stringAudioData = self.audioData.tostring()
		self.cutAudio = self.audioData
		# self.cut2()
		self.getFeature()
