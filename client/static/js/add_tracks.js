document.getElementById("trackInputButton").addEventListener("click", addTrack);

async function addTrack() {
    const track = document.getElementById("trackInputText").value;

    const url = "http://127.0.0.1:5000/samples/";
    const data = {
        "tracks": track
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
            addTrackEntry(json[0].track);
            let sampleCount = json[0].samples.length;
            for(let i = 0; i < sampleCount; i++) {
                addSampleEntry(json[0].samples[i]);
            }
        })
        .catch((err) => console.error(err.message));
    
    return trackData
};

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

    return track_entry_div
}

function addTrackEntry(track_data) {
    const track_id = track_data.uri.replace("spotify:track:", "");
    const track_entry = document.createElement("dt");
    const sample_list = document.getElementById("sample-list");

    track_entry.appendChild(generateTrackEntry(track_id));
    sample_list.appendChild(track_entry);
}

function addSampleEntry(sample_data) {
    const track_id = sample_data.uri.replace("spotify:track:", "");
    const track_entry = document.createElement("dd");
    const sample_list = document.getElementById("sample-list");

    track_entry.appendChild(generateTrackEntry(track_id));
    sample_list.appendChild(track_entry);
}