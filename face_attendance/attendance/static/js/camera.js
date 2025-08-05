const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('captureBtn');
const statusText = document.getElementById('status');

// Start camera
navigator.mediaDevices.getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
  });

// On click capture
captureBtn.addEventListener('click', () => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  const dataURL = canvas.toDataURL('image/png');

  fetch('/mark/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCSRFToken(),
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `image=${encodeURIComponent(dataURL)}`
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'success') {
      statusText.innerText = 'Attendance marked!';
    } else {
      statusText.innerText = 'Failed to mark attendance.';
    }
  });
});

function getCSRFToken() {
  const name = 'csrftoken=';
  const decoded = decodeURIComponent(document.cookie);
  const cookies = decoded.split(';');
  for (let cookie of cookies) {
    while (cookie.charAt(0) === ' ') cookie = cookie.substring(1);
    if (cookie.indexOf(name) === 0) return cookie.substring(name.length, cookie.length);
  }
  return '';
}
