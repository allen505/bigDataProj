fetch('/')

function onYouTubePlayerAPIReady() {
    player = new YT.Player('ytplayer', {
    height: '200',
    width: '400',
    videoId: '3C66w5Z0ixs',
    events: {
        'onStateChange': onPlayerStateChange
    }
});
}

function loadScript()
{
    if (typeof(YT) == 'undefined' || typeof(YT.Player) == 'undefined') {
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    }
}

function loadPlayer() {
        window.onYouTubePlayerAPIReady = function() {
            onYouTubePlayer();
        };
}


for(let i=0;i<videoId.length;i++){
    console.log("Running in the ", i, "th loop")
    var temp=document.createElement("div")
    temp.id=`player${i}`;
    get_recommendation.insertAdjacentElement('beforeend',temp);
    temp.innerText="Hello How are you"+i;
    onYouTubePlayerAPIReady();
}



// function createYouTubePlayer(playerId, videoId, width, height) {
//     new YT.Player(playerId, {
//         height: height,
//         width: width,
//         videoId: videoId,
//         events: {
//             'onStateChange': onPlayerStateChange
//         }
//     });
// }


function onPlayerStateChange(events){
    if (events.data==YT.PlayerState.PLAYING)
        {
            console.log(Math.round(player.playerInfo.currentTime))
        }
    }