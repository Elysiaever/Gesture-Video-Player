<template>
  <el-card class="gesture-help">
    <h3>手势功能说明</h3>
    <el-table :data="gestureList" style="width: 100%">
      <el-table-column prop="id" label="ID" width="50" />
      <el-table-column prop="desc" label="功能" />
      <el-table-column prop="gesture" label="手势描述" />
    </el-table>
  </el-card>
</template>

<script setup>
const gestureList = [
  { id: 1, desc: '播放/暂停', gesture: '张手/收手' },
  { id: 2, desc: '加速播放', gesture: '剪刀手' },
  { id: 3, desc: '音量加/减/静音', gesture: '加、减、拳头' },
  { id: 4, desc: '全屏切换', gesture: '双手展开/并拢' },
  { id: 5, desc: '切换视频', gesture: '指左/指右' },
  { id: 6, desc: '退出播放器', gesture: '长停+确认' },
  { id: 7, desc: '收藏', gesture: '交叉手指' },
  { id: 8, desc: '亮度调节', gesture: '上滑/下滑' },
  { id: 9, desc: '方向旋转', gesture: '圈手' },
  { id: 10, desc: '快进/快退', gesture: '合指滑动' },
  { id: 11, desc: '播放模式切换', gesture: '四指张开' },
  { id: 12, desc: '手势说明栏', gesture: '三指张开/并拢' },
  { id: 13, desc: '呼出进度条', gesture: '握拳再打开' }
]
</script>

<style>
.gesture-help {
  margin: 20px;
}
</style>
