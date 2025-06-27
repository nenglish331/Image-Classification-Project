import os
import cv2
from pytube import YouTube

def get_screenshots(video_id, game_name, screeenshots, start_time, end_time=None):
    # Check if the video has already been downloaded
    # game_folder_path = f'videos/{game_name}'
    # video_path = f'videos/{game_name}/{game_name}_{video_id}.mp4'
    game_folder_path = f'C:/Users/nengl/Videos/Machine Learning Project/{game_name}' # laptop
    video_path = f'{game_folder_path}/{game_name}_{video_id}.mp4'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(game_folder_path):
        os.makedirs(game_folder_path)

    if not os.path.exists(video_path):
        # Download the YouTube video
        print(f"Downloading video {game_name}_{video_id}.mp4")
        yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        video = yt.streams.filter(res="360p", only_video=True).first()
        video.download(output_path=game_folder_path, filename_prefix=f'{game_name}_', filename=f'{video_id}.mp4')
    else:
        print(f"Video {game_name}_{video_id}.mp4 already exists")


    # Extract screenshots from the video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time * fps)
    
    if end_time is None:
        # Set end_time to the length of the video
        end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        end_time = end_frame / fps
    else:
        end_frame = int(end_time * fps)
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    frame_interval = (end_frame - start_frame) // screeenshots 
    current_frame = start_frame
    print(f"Extracting screenshots from {game_name}_{video_id}.mp4")
    print(f"Start frame: {start_frame}, End frame: {end_frame}, Frame interval: {frame_interval}")

    screenshot_count = screeenshots

    while current_frame <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        # Save the screenshot
        if (current_frame - start_frame) % frame_interval == 0 and screenshot_count > 0:
            screenshot_count -= 1
            screenshot_path = f"images/{game_name}/{game_name}_{video_id}_{current_frame}.jpg"
            directory = os.path.dirname(screenshot_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            cv2.imwrite(screenshot_path, frame)

        current_frame += 1

    # Clean up
    cap.release()
    # os.remove(video_path)

game_name = 'VAL'

video_ids = [
    'ZaGG96oBF6M',
    'fnwS9wqsbug',
    'pouJe_Z_IVg',
    '6oRp1r6-IZM',
    'Vx6jL94IhQk',
    'xJRm0bV-MDI',
    'xvd7-3aXjWo',
    'bKt8Kicl2NE',
    'rWEVyAp-0JA',
    'Zg41enauytg',
    'w49hYGXH-MM',
    'Us88k0oo8mg',
    'pouJe_Z_IVg',
    '1s3BXpbq-0w',
    'IO7SMYSqNZY',
]
start_times = [
    '0:1',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
]
end_times = [
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
    '0:0',
]
screeenshots = [
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    15,
]

for i in range(len(video_ids)):
    startTimeMinutes, startTimeSeconds = map(int, start_times[i].split(':'))
    startTime = startTimeMinutes * 60 + startTimeSeconds
    
    endTimeMinutes, endTimeSeconds = map(int, end_times[i].split(':'))
    endTime = endTimeMinutes * 60 + endTimeSeconds

    # get_screenshots(video_ids[i], game_name, screeenshots[i], startTime, endTime)
    get_screenshots(video_ids[i], game_name, screeenshots[i], startTime, None)
