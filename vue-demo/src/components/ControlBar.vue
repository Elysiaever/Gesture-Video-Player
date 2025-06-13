<template>
  <div class="control-bar-wrapper">
    <el-button class="gesture-help-btn" @click="$emit('update:showGestureHelp', !showGestureHelp)">
      {{ showGestureHelp ? '隐藏手势说明' : '显示手势说明' }}
    </el-button>

    <div class="control-bar">
      <div class="button-row">
        <el-button :disabled="disablePrev" @click="$emit('prev')">上一个</el-button>
        <el-button @click="$emit('seekBackward', 5)">快退5秒</el-button>
        <el-button @click="$emit('togglePlay')">{{ isPlaying ? '暂停' : '播放' }}</el-button>
        <el-button @click="$emit('seekForward', 5)">快进5秒</el-button>
        <el-button :disabled="disableNext" @click="$emit('next')">下一个</el-button>
      </div>

      <div class="button-row">
        <el-button
          :style="{
            backgroundColor: isMuted ? '#409EFF' : '#ffffff',
            color: isMuted ? '#ffffff' : '#000000'
          }"
          @click="$emit('mute')"
        >
          <i :class="isMuted ? 'el-icon-volume-off' : 'el-icon-volume-up'" style="margin-right: 5px"></i>
          {{ isMuted ? '解除静音' : '静音' }}
        </el-button>

        <div class="volume-control">
          <div class="volume-label">音量</div>
          <el-slider
            :min="0"
            :max="100"
            :model-value="volume"
            @update:modelValue="$emit('volumeChange', $event)"
            style="width: 120px"
          />
        </div>

        <div class="volume-control">
          <div class="volume-label">亮度</div>
          <el-slider
            :min="50"
            :max="200"
            :model-value="brightness"
            @update:modelValue="$emit('brightnessChange', $event)"
            style="width: 120px"
          />
        </div>

        <div class="volume-control">
          <div class="volume-label">倍速</div>
          <el-select
            :model-value="playbackRate"
            @update:modelValue="$emit('rateChange', $event)"
            style="width: 80px"
          >
            <el-option label="0.5x" :value="0.5" />
            <el-option label="1x" :value="1" />
            <el-option label="1.5x" :value="1.5" />
            <el-option label="2x" :value="2" />
          </el-select>
        </div>

        <!-- 播放模式切换按钮 -->
        <el-button @click="$emit('modeToggle')">
          <template v-if="playMode === 'single'">🔂 循环 </template>
          <template v-else-if="playMode === 'loop'">🔁 列表 </template>
          <template v-else>🔀 随机 </template>
        </el-button>

        <el-button @click="$emit('fullscreen')">全屏</el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  isPlaying: Boolean,
  isMuted: Boolean,
  volume: Number,
  brightness: Number,
  playbackRate: Number,
  playMode: String,
  disablePrev: Boolean,
  disableNext: Boolean,
  showGestureHelp: Boolean,
})
</script>

<style scoped>
.control-bar-wrapper {
  position: relative;
  width: 100%;
}

.control-bar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.button-row {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.gesture-help-btn {
  position: fixed;
  top: 50px;
  right: 200px;
  z-index: 999;
}

.volume-control {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}

.volume-label {
  font-size: 12px;
  color: #666;
  white-space: nowrap;
}
</style>