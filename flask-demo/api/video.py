# ========== api/video.py ==========
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from service.player_state import player_state

video_bp = Blueprint('video', __name__)


@video_bp.route('/toggle_play', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '播放/暂停切换',
    'responses': {200: {'description': '播放状态已切换'}}
})
def toggle_play():
    player_state['is_playing'] = not player_state['is_playing']
    return jsonify(player_state)

@video_bp.route('/speed', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '调节播放速度',
    'parameters': [{
        'name': 'speed', 'in': 'json', 'type': 'number', 'required': True
    }],
    'responses': {200: {'description': '速度设置成功'}}
})
def set_speed():
    data = request.get_json()
    player_state['playback_speed'] = data.get('speed', 1.0)
    return jsonify(player_state)

@video_bp.route('/volume', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '调节音量',
    'parameters': [{
        'name': 'volume', 'in': 'json', 'type': 'integer', 'required': True
    }],
    'responses': {200: {'description': '音量设置成功'}}
})
def set_volume():
    data = request.get_json()
    player_state['volume'] = data.get('volume', 50)
    return jsonify(player_state)

@video_bp.route('/toggle_mute', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '切换静音状态',
    'responses': {200: {'description': '静音状态切换'}}
})
def toggle_mute():
    player_state['is_muted'] = not player_state['is_muted']
    return jsonify(player_state)

@video_bp.route('/fullscreen', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '切换全屏状态',
    'responses': {200: {'description': '全屏状态切换'}}
})
def toggle_fullscreen():
    player_state['is_fullscreen'] = not player_state['is_fullscreen']
    return jsonify(player_state)

@video_bp.route('/brightness', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '调节亮度',
    'parameters': [{
        'name': 'brightness', 'in': 'json', 'type': 'integer', 'required': True
    }],
    'responses': {200: {'description': '亮度设置成功'}}
})
def set_brightness():
    data = request.get_json()
    player_state['brightness'] = data.get('brightness', 50)
    return jsonify(player_state)

@video_bp.route('/switch_video', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '切换视频',
    'parameters': [{
        'name': 'direction', 'in': 'json', 'type': 'string', 'enum': ['next', 'previous'], 'required': True
    }],
    'responses': {200: {'description': '视频已切换'}}
})
def switch_video():
    # 前端根据方向实现切换播放源，后端仅记录状态
    data = request.get_json()
    player_state['current_time'] = 0
    return jsonify(player_state)

@video_bp.route('/exit', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '退出播放器',
    'responses': {200: {'description': '播放器退出'}}
})
def exit_player():
    player_state['is_playing'] = False
    return jsonify({'message': 'Player exited'})

# @video_bp.route('/collect', methods=['POST'])
# @swag_from({
#     'tags': ['Video Control'],
#     'summary': '收藏当前视频',
#     'responses': {200: {'description': '已收藏'}}
# })
# def toggle_collect():
#     player_state['collected'] = not player_state['collected']
#     return jsonify(player_state)

# @video_bp.route('/rotate', methods=['POST'])
# @swag_from({
#     'tags': ['Video Control'],
#     'summary': '旋转画面方向',
#     'parameters': [{
#         'name': 'angle', 'in': 'json', 'type': 'integer', 'required': True
#     }],
#     'responses': {200: {'description': '方向已旋转'}}
# })
# def rotate():
#     data = request.get_json()
#     player_state['rotation'] = data.get('angle', 0)
#     return jsonify(player_state)

@video_bp.route('/seek', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '快进/快退',
    'parameters': [{
        'name': 'offset', 'in': 'json', 'type': 'integer', 'required': True
    }],
    'responses': {200: {'description': '时间轴偏移成功'}}
})
def seek():
    data = request.get_json()
    player_state['current_time'] += data.get('offset', 0)
    return jsonify(player_state)

@video_bp.route('/mode', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '切换播放模式',
    'parameters': [{
        'name': 'mode', 'in': 'json', 'type': 'string', 'required': True
    }],
    'responses': {200: {'description': '播放模式切换成功'}}
})
def change_mode():
    data = request.get_json()
    player_state['mode'] = data.get('mode', 'normal')
    return jsonify(player_state)

@video_bp.route('/progress', methods=['POST'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '呼出/隐藏进度条',
    'responses': {200: {'description': '进度条显示状态切换'}}
})
def toggle_progress():
    player_state['progress_visible'] = not player_state['progress_visible']
    return jsonify(player_state)

@video_bp.route('/state', methods=['GET'])
@swag_from({
    'tags': ['Video Control'],
    'summary': '获取当前播放器状态',
    'responses': {200: {'description': '返回所有播放器状态'}}
})
def get_state():
    return jsonify(player_state)