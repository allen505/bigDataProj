var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
function onYouTubePlayerAPIReady() {
    player = new YT.Player('video-frame', {
    height: '200',
    width: '400',
    videoId: '0a5YhsnITFE',
    playerVars: {
        'autoplay': 0, // This is optional, 1 for autoplay when the video loads
        'controls': 1, // This is optional, 0 to hide player controls
        'fs': 1 // Allows the fullscreen button
    },
    events: {
        'onStateChange': onPlayerStateChange
    }
});
}

function onPlayerStateChange(events){
    if (events.data==YT.PlayerState.PLAYING)
        {
            console.log(Math.round(player.playerInfo.currentTime))
        }
    }