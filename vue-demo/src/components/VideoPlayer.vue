<script setup>
import { ref, onMounted, nextTick } from 'vue'
import ControlBar from './ControlBar.vue'

const props = defineProps({
  showHelp: Boolean
})
const emit = defineEmits(['update:showHelp'])

const videoList = ref([])
const currentIndex = ref(0)
const currentVideoSrc = ref('')
const videoElement = ref(null)

const isPlaying = ref(false)
const isMuted = ref(false)
const volume = ref(50)
const brightness = ref(100)
const playbackRate = ref(1.0)
const playMode = ref('loop') // 'single', 'loop', 'shuffle'
let previousVolume = 50

onMounted(() => {
  videoList.value = ['sample1.mp4', 'sample2.mp4']
  if (videoList.value.length) selectVideo(0)

  nextTick(() => {
    if (videoElement.value) {
      videoElement.value.addEventListener('ended', handleEnded)
    }
  })
})

function selectVideo(index) {
  currentIndex.value = index
  currentVideoSrc.value = `/videos/${videoList.value[index]}`

  nextTick(() => {
    if (videoElement.value) {
      videoElement.value.volume = volume.value / 100
      videoElement.value.muted = isMuted.value
      videoElement.value.playbackRate = playbackRate.value
      videoElement.value.play()
      isPlaying.value = true
    }
  })
}

function prevVideo() {
  if (currentIndex.value > 0) selectVideo(currentIndex.value - 1)
}

function nextVideo() {
  if (currentIndex.value < videoList.value.length - 1) selectVideo(currentIndex.value + 1)
}

function seekBackward(seconds) {
  if (videoElement.value) {
    videoElement.value.currentTime = Math.max(0, videoElement.value.currentTime - seconds)
  }
}

function seekForward(seconds) {
  if (videoElement.value) {
    videoElement.value.currentTime = Math.min(videoElement.value.duration, videoElement.value.currentTime + seconds)
  }
}

function togglePlay() {
  if (!videoElement.value) return
  if (videoElement.value.paused) {
    videoElement.value.play()
    isPlaying.value = true
  } else {
    videoElement.value.pause()
    isPlaying.value = false
  }
}

function toggleMute() {
  if (!isMuted.value) {
    previousVolume = volume.value
    volume.value = 0
  } else {
    volume.value = previousVolume
  }

  isMuted.value = !isMuted.value

  if (videoElement.value) {
    videoElement.value.muted = isMuted.value
    videoElement.value.volume = volume.value / 100
  }
}

function changeVolume(val) {
  volume.value = val
  isMuted.value = val === 0

  if (videoElement.value) {
    videoElement.value.volume = val / 100
    videoElement.value.muted = isMuted.value
  }
}

function changeBrightness(val) {
  brightness.value = val
}

function changeRate(val) {
  playbackRate.value = val
  if (videoElement.value) {
    videoElement.value.playbackRate = val
  }
}

function enterFullscreen() {
  videoElement.value?.requestFullscreen?.()
}

function togglePlayMode() {
  const modes = ['loop', 'single', 'shuffle']
  const current = modes.indexOf(playMode.value)
  playMode.value = modes[(current + 1) % modes.length]
}

function handleEnded() {
  if (!videoElement.value) return

  if (playMode.value === 'single') {
    videoElement.value.currentTime = 0
    videoElement.value.play()
  } else if (playMode.value === 'loop') {
    if (currentIndex.value < videoList.value.length - 1) {
      selectVideo(currentIndex.value + 1)
    } else {
      selectVideo(0)
    }
  } else if (playMode.value === 'shuffle') {
    let next
    do {
      next = Math.floor(Math.random() * videoList.value.length)
    } while (next === currentIndex.value && videoList.value.length > 1)
    selectVideo(next)
  }
}
</script>

<template>
  <div class="video-player">
    <div class="video-list" :class="{ shifted: showHelp }">
      <h3>视频目录</h3>
      <ul>
        <li
          v-for="(video, idx) in videoList"
          :key="idx"
          :class="{ active: idx === currentIndex }"
          @click="selectVideo(idx)"
        >
          {{ video }}
        </li>
      </ul>
    </div>

    <div class="video-area">
      <video
        ref="videoElement"
        :src="currentVideoSrc"
        controls
        :style="{ width: '100%', maxHeight: '600px', filter: `brightness(${brightness}%)` }"
      ></video>

      <ControlBar
        :isPlaying="isPlaying"
        :isMuted="isMuted"
        :volume="volume"
        :brightness="brightness"
        :playbackRate="playbackRate"
        :disablePrev="currentIndex === 0"
        :disableNext="currentIndex === videoList.length - 1"
        :showGestureHelp="showHelp"
        :playMode="playMode"
        @update:showGestureHelp="emit('update:showHelp', $event)"
        @prev="prevVideo"
        @next="nextVideo"
        @togglePlay="togglePlay"
        @mute="toggleMute"
        @volumeChange="changeVolume"
        @brightnessChange="changeBrightness"
        @rateChange="changeRate"
        @fullscreen="enterFullscreen"
        @seekForward="seekForward"
        @seekBackward="seekBackward"
        @modeToggle="togglePlayMode"
      />
    </div>
  </div>
</template>

<style scoped>
.video-player {
  display: flex;
  flex-direction: row;
}

.video-list {
  position: absolute;
  top: 50px;
  left: -50px;
  width: 180px;
  height: 700px;
  background-color: #eaf4fc;
  padding: 20px 15px;
  border-right: 1px solid #d0e3f1;
  border-radius: 10px 0 0 10px;
  box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  transition: transform 0.3s ease;
  z-index: 10;
}

.video-list.shifted {
  transform: translateX(-200px);
}

.video-list h3 {
  font-size: 16px;
  margin-bottom: 12px;
  color: #409eff;
  border-bottom: 1px solid #d0e3f1;
  padding-bottom: 6px;
}

.video-list ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.video-list li {
  padding: 8px 10px;
  margin-bottom: 6px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s, color 0.2s;
  color: #333;
}

.video-list li:hover {
  background-color: #d0eaff;
  color: #000;
}

.video-list li.active {
  background-color: #409eff;
  color: #fff;
  font-weight: bold;
}

.video-area {
  flex: 1;
  padding: 20px;
}
</style>