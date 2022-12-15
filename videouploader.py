def videouploader():
    from simple_youtube_api.Channel import Channel
    from simple_youtube_api.LocalVideo import LocalVideo

    # loggin into the channel
    channel = Channel()
    channel.login("cls.json", "credentials.storage")
    # sets up local video
    video = LocalVideo(file_path="output.mp4")
    # setting up specifics
    video.set_title("Test title")
    video.set_description("This is a description")
    video.set_tags(["this", "tag"])
    video.set_category("gaming")
    video.set_default_language("en-US")
    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("private")
    video.set_public_stats_viewable(True)
    # uploading video and printing the results 'video id'
    video = channel.upload_video(video)
    # print(video.id)
    # print(video)
    # videro = "https://www.youtube.com/watch?v=" + video.id
    return "HERE IS YOUR LINK:" + "https://www.youtube.com/watch?v=" + video.id
    # return "https://www.youtube.com/watch?v="
