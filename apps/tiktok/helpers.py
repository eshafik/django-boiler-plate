import copy


def flatten_videos(data):
    # Output list for flattened videos
    flattened_videos = []

    # Convert videos into the required format
    for video in data.get('videos', []):
        flattened_video = copy.deepcopy(video)

        # Match author_id with users.id
        # author = next((user for user in data['users'] if user['id'] == video['author_id']), None)
        # if author:
        #     flattened_video['author'] = {
        #         'tiktok_unique_id': author['tiktok_unique_id'],
        #         'sec_uid': author['sec_uid'],
        #         'follower_count': author['follower_count'],
        #         'following_count': author['following_count'],
        #         'video_count': author['video_count'],
        #         'like_count': author['like_count'],
        #         'has_sent': author['has_sent']
        #     }
        #
        # # Match hashtag_id with hashtags.id
        # hashtag = next((hashtag for hashtag in data['hashtags'] if hashtag['id'] == video['hashtag_id']), None)
        # if hashtag:
        #     flattened_video['hashtag'] = {
        #         'text': hashtag['text'],
        #         'challenge_id': hashtag['challenge_id'],
        #         'last_fetched_cursor': hashtag['last_fetched_cursor'],
        #         'has_more': hashtag['has_more'],
        #         'view_count': hashtag['view_count'],
        #         'video_count': hashtag['video_count'],
        #         'has_sent': hashtag['has_sent']
        #     }
        #
        # # Add flattened video to the list
        # flattened_videos.append(flattened_video)

    return {'videos': data}