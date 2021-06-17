# VLC media player
vlc_main_window = {'title_re': '.*VLC media player'}
vlc_pause_button = {'best_match': 'Button0'}
vlc_fullscreen_button = {'best_match': 'Button5'}

# Time dialog
vlc_time_dialog = {'best_match': 'TimeDialog'}
vlc_time_dialog_reset_time_button = {'best_match': 'Button2', 'top_level_only': False}
vlc_time_dialog_go_button = {'best_match': 'Button3', 'top_level_only': False}

# Settings dialog
vlc_settings_dialog = {'best_match': 'Simple Preferences'}
vlc_setting_show_controllers_in_full_screen = {'title': "Show controls in full screen mode", 'control_type': "CheckBox"}
vlc_setting_update_notifier_checkbox = {'title': "Activate updates notifier", 'control_type': "CheckBox"}
vlc_settings_show_title_check_box = {'title': "Show media title on video start", 'control_type': "CheckBox"}
vlc_settings_subtitles_tab_button = {'best_match': 'Subtitles / OSD'}
vlx_settings_save_button = {'title': "Save Enter", 'control_type': "Button"}

# Open Files dialog
open_file_dialog = {'title': 'Open File'}
open_file_file_name_edit = {'class_name': 'Edit', 'title': 'File name:'}
open_file_open_button = {'class_name': 'Button', 'title': 'Open'}
