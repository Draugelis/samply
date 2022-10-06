document.getElementById("trackInputButton").addEventListener("click", addTrack);
document.getElementById("proceedButton").addEventListener("click", stepForward);
document
  .getElementById("playlistCreateButton")
  .addEventListener("click", createPlaylist);
document.getElementById("backButton").addEventListener("click", stepBack);
document.getElementById("restartButton").addEventListener("click", stepRestart);
document
  .getElementById("spotifyButton")
  .addEventListener("click", spotify_login);

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

function spotify_login() {
  let client_id = "461f9d29c55744a28f55ef0d762295c6";
  let redirect_uri = "http://127.0.0.1:5000/spotify";
  let scope = "playlist-modify-public";

  let url = "https://accounts.spotify.com/authorize";
  url += "?response_type=token";
  url += "&client_id=" + encodeURIComponent(client_id);
  url += "&scope=" + encodeURIComponent(scope);
  url += "&redirect_uri=" + encodeURIComponent(redirect_uri);

  window.location.replace(url);
}

async function addTrack() {
  document.getElementById("trackInputButton").classList.add("is-loading");
  const track = document.getElementById("trackInputText").value;

  const url = "/samples/";
  const data = {
    tracks: track,
  };

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Spotify": getCookie("spotify_token"),
    },
    body: JSON.stringify(data),
    redirect: "follow",
  };

  await fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed fetching track data");
      }
      return response.json();
    })
    .then(([json]) => {
      addTrackEntry(json.track);
      for (sample of json.samples) {
        addSampleEntry(sample);
      }
    })
    .catch((err) => console.error(err.message));
  
  document.getElementById("trackInputButton").classList.remove("is-loading");
}

function generateTrackEntry(track_id) {
  const embed_url = `https://open.spotify.com/embed/track/${track_id}?theme=0`;

  const track_entry_checkbox = document.createElement("input");
  track_entry_checkbox.setAttribute("id", track_id);
  track_entry_checkbox.setAttribute("name", "trackEntryCheckbox");
  track_entry_checkbox.setAttribute("type", "checkbox");
  track_entry_checkbox.setAttribute("checked", "");

  const track_entry_frame = document.createElement("iframe");
  track_entry_frame.setAttribute("src", embed_url);
  track_entry_frame.setAttribute("width", "100%");
  track_entry_frame.setAttribute("height", "80");
  track_entry_frame.setAttribute("frameBorder", "0");
  track_entry_frame.setAttribute("allow", "encrypted-media");

  const track_entry_div = document.createElement("div");
  track_entry_div.classList.add("track-entry");
  track_entry_div.appendChild(track_entry_checkbox);
  track_entry_div.appendChild(track_entry_frame);

  return track_entry_div;
}

function addTrackEntry(track_data) {
  const track_id = track_data.id;
  const track_entry = document.createElement("dt");
  const sample_list = document.getElementById("sample-list");

  track_entry.appendChild(generateTrackEntry(track_id));
  sample_list.appendChild(track_entry);
}

function addSampleEntry(sample_data) {
  const track_id = sample_data.id;
  const track_entry = document.createElement("dd");
  const sample_list = document.getElementById("sample-list");

  track_entry.appendChild(generateTrackEntry(track_id));
  sample_list.appendChild(track_entry);
}

async function createPlaylist() {
  document.getElementById("playlistCreateButton").classList.add("is-loading");
  const tracks = getTrackUris();
  const playlist_name = document.getElementById("playlistInputText").value;

  const url = "/playlist/";

  const data = {
    name: playlist_name,
    tracks: tracks,
  };

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Spotify": getCookie("spotify_token"),
    },
    body: JSON.stringify(data),
    redirect: "follow",
  };

  await fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed fetching track data");
      }
      console.log(response);
      return response.json();
    })
    .then((json) => {
      addPlaylistContainer(json.id);
    })
    .catch((err) => console.error(err.message));

  document.getElementById("playlistCreateButton").classList.remove("is-loading");
}

function getTrackUris() {
  const selected_tracks = Array.from(document.querySelectorAll(
    "input[name=trackEntryCheckbox]:checked"
  ));
  let track_uris = selected_tracks.map(({id}) => `spotify:track:${id}`)
  track_uris = [...new Set(track_uris)]; // Removing duplicates
  return track_uris;
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

  document.getElementById("sample-list").innerText = "";
  document.getElementById("output-container").appendChild(playlist_frame);

  document.getElementById("playlistInput").style.display = "none";
  document.getElementById("restartInput").style.display = "inherit";
}

function stepForward() {
  document.getElementById("trackInput").style.display = "none";
  document.getElementById("playlistInput").style.display = "inherit";
}

function stepBack() {
  document.getElementById("playlistInput").style.display = "none";
  document.getElementById("trackInput").style.display = "inherit";
}

function stepRestart() {
  document.getElementById("restartInput").style.display = "none";
  document.getElementById("trackInput").style.display = "inherit";
  document.getElementsByClassName("playlist")[0].remove();
}
