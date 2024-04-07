// Your JavaScript code

let chunks = [];
let mediaRecorder;

// Function to start recording
function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(function(stream) {
      mediaRecorder = new MediaRecorder(stream);
      
      mediaRecorder.ondataavailable = function(event) {
        chunks.push(event.data);
      };
      
      mediaRecorder.start();
    })
    .catch(function(err) {
      console.log('The following getUserMedia error occurred: ' + err);
    });
}

// Function to stop recording and submit the form
function stopRecording() {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    mediaRecorder.stop();
    mediaRecorder.onstop = function() {
      let blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
      let formData = new FormData(document.getElementById('myForm'));
      formData.append('voice_file', blob, 'recorded_voice.ogg');
      
      fetch('/upload_voice/', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        // Handle response from the server
      })
      .catch(error => {
        console.error('Error:', error);
      });
    };
  }
}

// Optional: You can also submit the form when the user clicks the submit button
document.getElementById('voiceForm').addEventListener('submit', function(event) {
  event.preventDefault();
  stopRecording();
  // Optionally, you can also submit the form data here
  // this.submit();
});
