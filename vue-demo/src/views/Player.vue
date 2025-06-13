<template>
  <div class="player-wrapper">
    <div class="main-content">
      <div class="video-section">
        <h1 class="page-title">手势识别智能播放器</h1>
        <VideoPlayer class="video-area" v-model:showHelp="showHelp" />
      </div>

      <!-- 手势帮助面板 -->
      <div class="gesture-help-panel" v-if="showHelp">
        <GestureHelp />
      </div>
    </div>
  </div>
</template>

<script setup>
import VideoPlayer from '@/components/VideoPlayer.vue'
import GestureHelp from '@/components/GestureHelp.vue'
import { ref } from 'vue'

const showHelp = ref(false) // 交由子组件控制
</script>

<style scoped>
.player-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #e6f7ff;
  min-height: 100vh;
}

/* 页面主区域布局 */
.main-content {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  max-width: 1200px;
  position: relative;
}

.video-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  max-width: 800px;
  background-color: white;
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.page-title {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

.video-area {
  width: 100%;
}

/* 手势帮助面板 */
.gesture-help-panel {
  width: 400px;
  margin-top: 60px;
  margin-left: 20px;
  max-height: 80vh;
  overflow-y: auto;
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
}
</style>