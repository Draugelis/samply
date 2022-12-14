document.getElementById('trackInputButton').addEventListener('click', addTrack);
document.getElementById('proceedButton').addEventListener('click', stepForward);
document
  .getElementById('playlistCreateButton')
  .addEventListener('click', createPlaylist);
document.getElementById('backButton').addEventListener('click', stepBack);
document.getElementById('restartButton').addEventListener('click', stepRestart);
document
  .getElementById('spotifyButton')
  .addEventListener('click', spotify_login);

showInput();

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

async function spotify_login() {
  const url = '/spotify_client/';
  const requestOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  };

  await fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed fetching Spotify client id');
      }
      return response.json();
    })
    .then((json) => {
      const client_id = json.spotify_client_id;
      const redirect_uri = window.location.href + 'spotify';
      const scope = 'playlist-modify-public';

      let url = 'https://accounts.spotify.com/authorize';
      url += '?response_type=token';
      url += '&client_id=' + encodeURIComponent(client_id);
      url += '&scope=' + encodeURIComponent(scope);
      url += '&redirect_uri=' + encodeURIComponent(redirect_uri);

      window.location.href = url;
    });
}

async function addTrack() {
  const track = document.getElementById('trackInputText').value;
  document.getElementById('trackInputText').value = '';
  if(track.length == 0) {
    hightlightFieldError('trackInputText');
    return;
  }

  document.getElementById('trackInputButton').classList.add('is-loading');

  const url = '/samples/';
  const data = {
    tracks: track,
  };

  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    redirect: 'follow',
  };

  await fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed fetching track data');
      }
      return response.json();
    })
    .then(([json]) => {
      if (json.status == 'OK') {
        addTrackPanel(json);
      } else {
        hightlightFieldError('trackInputText');
        addError(track, json.error);
      }
    })
    .catch((err) => console.error(err.message));

  document.getElementById('trackInputButton').classList.remove('is-loading');
}

async function createPlaylist() {
  const tracks = getTrackUris();
  const playlist_name = document.getElementById('playlistInputText').value;
  if(playlist_name.length == 0) {
    hightlightFieldError('playlistInputText');
    return;
  }

  document.getElementById('playlistCreateButton').classList.add('is-loading');

  const url = '/playlist/';

  const data = {
    name: playlist_name,
    tracks: tracks,
  };

  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    redirect: 'follow',
  };

  await fetch(url, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed fetching track data');
      }
      return response.json();
    })
    .then((json) => {
      if (json.status == 'OK') {
        addPlaylistPanel(json);
      } else {
        hightlightFieldError('playlistInputText');
        addError(playlist_name, json.error);
      }
    })
    .catch((err) => console.error(err.message));

  document
    .getElementById('playlistCreateButton')
    .classList.remove('is-loading');
}

function showInput() {
  if (getCookie('spotify_token')) {
    document.getElementById('trackInput').classList.remove('hide');
  } else {
    document.getElementById('spotifyLogin').classList.remove('hide');
  }
}

function stepForward() {
  document.getElementById('trackInput').classList.add('hide');
  document.getElementById('playlistInput').classList.remove('hide');
}

function stepBack() {
  document.getElementById('playlistInput').classList.add('hide');
  document.getElementById('trackInput').classList.remove('hide');
}

function stepRestart() {
  document.getElementById('restartInput').classList.add('hide');
  document.getElementById('trackInput').classList.remove('hide');
  document.getElementById('playlistPanel').remove();
}

function addTrackPanel(track_data) {
  const track_panel = document.createElement('div');
  track_panel.classList.add('panel');
  track_panel.classList.add('fadein');

  const track_panel_head = document.createElement('p');
  track_panel_head.classList.add('panel-heading');
  track_panel_head.innerText = `${track_data.track.artist} - ${track_data.track.track}`;

  track_panel.appendChild(track_panel_head);
  track_panel.appendChild(getTrackBlock(track_data.track.id));
  for (sample of track_data.samples) {
    track_panel.appendChild(getTrackBlock(sample.id));
  }

  document.getElementById('output-container').prepend(track_panel);
}

function getTrackBlock(track_id) {
  const embed_url = `https://open.spotify.com/embed/track/${track_id}?theme=0`;
  const track_entry_frame = document.createElement('iframe');
  track_entry_frame.setAttribute('src', embed_url);
  track_entry_frame.setAttribute('width', '100%');
  track_entry_frame.setAttribute('height', '80');
  track_entry_frame.setAttribute('frameBorder', '0');
  track_entry_frame.setAttribute('allow', 'encrypted-media');

  const track_entry_checkbox = document.createElement('input');
  track_entry_checkbox.setAttribute('id', track_id);
  track_entry_checkbox.setAttribute('name', 'trackEntryCheckbox');
  track_entry_checkbox.setAttribute('type', 'checkbox');
  track_entry_checkbox.setAttribute('checked', '');

  const track_entry_checkbox_span = document.createElement('span');
  track_entry_checkbox_span.classList.add('panel-icon');
  track_entry_checkbox_span.appendChild(track_entry_checkbox);

  const track_entry_block = document.createElement('div');
  track_entry_block.classList.add('panel-block');
  track_entry_block.appendChild(track_entry_checkbox_span);
  track_entry_block.appendChild(track_entry_frame);

  return track_entry_block;
}

function getTrackUris() {
  const selected_tracks = Array.from(
    document.querySelectorAll('input[name=trackEntryCheckbox]:checked')
  );
  let track_uris = selected_tracks.map(({ id }) => `spotify:track:${id}`);
  track_uris = [...new Set(track_uris)]; // Removing duplicates
  return track_uris;
}

function addPlaylistPanel(playlist_data) {
  const playlist_panel = document.createElement('div');
  playlist_panel.classList.add('box');
  playlist_panel.classList.add('fadein');
  playlist_panel.setAttribute('id', 'playlistPanel');

  const embed_url = `https://open.spotify.com/embed/playlist/${playlist_data.id}?theme=0`;
  const playlist_frame = document.createElement('iframe');
  playlist_frame.setAttribute('src', embed_url);
  playlist_frame.setAttribute('width', '100%');
  playlist_frame.setAttribute('height', '380');
  playlist_frame.setAttribute('frameBorder', '0');
  playlist_frame.setAttribute('allow', 'encrypted-media');

  playlist_panel.appendChild(playlist_frame);

  document.getElementById('output-container').innerText = '';
  document.getElementById('output-container').appendChild(playlist_panel);

  document.getElementById('playlistInput').classList.add('hide');
  document.getElementById('restartInput').classList.remove('hide');
}

function hightlightFieldError(field_id) {
  document.getElementById(field_id).classList.add('is-danger');
  setTimeout(() => {
    document.getElementById(field_id).classList.remove('is-danger');
  }, '5000');
}

function addError(query, error) {
  const message = `${error}: ${query}`;
  const notification = getNotification(message, 'is-primary');
  document.getElementById('notifications').prepend(notification);
}

function getNotification(message, type) {
  const delete_button = document.createElement('button');
  delete_button.classList.add('delete');
  delete_button.addEventListener('click', () =>
    delete_button.parentNode.remove()
  );
  const notification = document.createElement('div');
  notification.classList.add('notification');
  notification.classList.add(type);
  notification.classList.add('fadein');
  notification.innerText = message;
  notification.prepend(delete_button);

  return notification;
}
