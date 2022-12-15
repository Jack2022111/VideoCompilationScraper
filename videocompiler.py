def videocompiler():
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    import moviepy.editor as mp
    import glob
    import os.path
    import os

    dir = r'C:\Users\JZipp\PycharmProjects\3dphotoeffects'
    # sets directory
    files = []
    processing = []
    files = (glob.glob(os.path.join(dir, '*.mp4')))
    # reads files with .mp4
    for z in files:
        V = mp.VideoFileClip(z)
        V2 = V.subclip(1, 5)
        # creates subclip and appends info to list
        processing.append(V2)

    final_clip = mp.concatenate_videoclips(processing)
    # compils list
    final_clip.write_videofile("output.mp4")
    # writes video file
    final_clip.close()
