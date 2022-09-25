document.getElementById("proceedButton").addEventListener("click", createPlaylist);

async function createPlaylist() {
    const tracks = getTrackUris();

    const url = "http://127.0.0.1:5000/playlist/";
 
}

function getTrackUris() {
    const selected_tracks = document.querySelectorAll("input[name=trackEntryCheckbox]:checked");
    let track_uris = [];
    let track_count = selected_tracks.length;
    for(let i = 0; i < track_count; i++) {
        let track_uri = `spotify:track:${selected_tracks[i].id}`;
        track_uris.push(track_uri);
    }
    track_uris = [...new Set(track_uris)]; // Removing duplicates
    return track_uris
}

function addPlaylistContainer() {

}