document.getElementById("proceedButton").addEventListener("click", replaceInput);


async function replaceInput() {
    document.getElementById("trackInputText").remove();
    document.getElementById("trackInputButton").remove();
    document.getElementById("proceedButton").remove();

    const playlist_name_input = document.createElement("input");
    playlist_name_input.setAttribute("id", "playlistNameText");
    playlist_name_input.setAttribute("type", "text");
    document.getElementById("input-container").appendChild(playlist_name_input);

    const playlist_create_button = document.createElement("button");
    playlist_create_button.setAttribute("id", "playlistCreateButton");
    playlist_create_button.textContent =  "Create playlist";
    playlist_create_button.addEventListener("click", createPlaylist);
    document.getElementById("input-container").appendChild(playlist_create_button);
}

async function createPlaylist() {
    const tracks = getTrackUris();
    const playlist_name = document.getElementById("playlistNameText").value;

    const url = "http://127.0.0.1:5000/playlist/";
 
    const data = {
        "name": playlist_name,
        "tracks": tracks
    };
    
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-Spotify": ""
        },
        body: JSON.stringify(data),
        redirect: "follow"
    };

    await fetch(url, requestOptions)
        .then((response) => {
            if(!response.ok) {
                throw new Error("Failed fetching track data");
            }
            console.log(response);
            return response.json();
        })
        .then((json) => {
            addPlaylistContainer(json.id);
        })
        .catch((err) => console.error(err.message));
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

function addPlaylistContainer(playlist_id) {
    const embed_url = `https://open.spotify.com/embed/playlist/${playlist_id}?theme=0`;
    const playlist_frame = document.createElement("iframe");
    playlist_frame.setAttribute("src", embed_url);
    playlist_frame.setAttribute("width", "100%");
    playlist_frame.setAttribute("height", "380");
    playlist_frame.setAttribute("frameBorder", "0");
    playlist_frame.setAttribute("allow", "encrypted-media");
    playlist_frame.classList.add("playlist");

    document.getElementById("sample-list").remove();
    document.getElementById("output-container").appendChild(playlist_frame);
    document.getElementById("input-container").remove();
}

