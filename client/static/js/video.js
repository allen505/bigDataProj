var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var video=document.getElementsByTagName('h1')[0];
id=video.id
var lastSentTime = 0;
function onYouTubePlayerAPIReady() {
    player = new YT.Player('video-frame', {
    width: '1239px',
    height:'695px',
    videoId: id,
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
    if (events.data == YT.PlayerState.PLAYING) {
        var currentTime = Math.round(player.playerInfo.currentTime);
        var total_time = Math.round(player.getDuration());
        console.log("Total time = ", total_time)
        console.log(currentTime)
        fetch('/update_time', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'video_id': id, 'current_time': currentTime, 'total_time': total_time })
        }).then(response => {
            console.log('Current time sent successfully:', currentTime);
        }).catch(error => {
            console.error('Error sending current time:', error);
        });

    }
}

function sendCurrentTime() {

}