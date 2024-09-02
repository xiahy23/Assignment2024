let startTime;
let elapsed = 0;
let timerId;
let running = false;

function setTimer() {
  const hours = document.getElementById('hours').value? parseInt(document.getElementById('hours').value, 10): 
    document.getElementById('DynamicButton') === 'Countdown'? 23: 0;
  const minutes = document.getElementById('minutes').value? parseInt(document.getElementById('minutes').value, 10):
    document.getElementById('DynamicButton') === 'Countdown'? 59: 0;
  const seconds = document.getElementById('seconds').value? parseInt(document.getElementById('seconds').value, 10):
    document.getElementById('DynamicButton') === 'Countdown'? 59: 0;
  if (document.getElementById('DynamicButton').textContent === 'Countdown' && hours === 0 && minutes === 0 && seconds === 0) {
    document.getElementById('errorDisplay').textContent = 'Please enter a valid time!';
  } else {
    document.getElementById('errorDisplay').textContent = '';
    elapsed = hours * 3600 + minutes * 60 + seconds;
    displayTime(elapsed);
    pauseTimer();
    document.getElementById('DynamicStart').textContent = 'Start';
  }
}

function StartAndPause() {
  if (document.getElementById('DynamicButton').textContent === 'Countdown' && hours === 0 && minutes === 0 && seconds === 0) {
    document.getElementById('errorDisplay').textContent = 'Please enter a valid time!';
  } else {
    const button = document.getElementById('DynamicStart');
    // Define an array of possible button texts
    const buttonTexts = ['Start', 'Pause'];
    // Get the current text of the button
    const currentText = button.textContent;
    // Find the index of the current text in the buttonTexts array
    const currentIndex = buttonTexts.indexOf(currentText);
    // Calculate the index of the next text
    const nextIndex = (currentIndex + 1) % buttonTexts.length;
    // Update the button text
    button.textContent = buttonTexts[nextIndex];
    if (nextIndex === 1) {
      startTimer();
    } else {
      pauseTimer();
    }
  }
}

function startTimer() {
  if (!running) {
    if (document.getElementById('DynamicButton').textContent === 'Countdown') {
      if (checkCountdown()) {
        if (timerId) {
        clearInterval(timerId);
        }
        startTime = Date.now() - elapsed * 1000;
        timerId = setInterval(() => {
          countDownTime = Math.floor((Date.now() - startTime) / 1000);
          displayTime(elapsed*2-countDownTime);
          if (elapsed*2 - countDownTime <= 0) {
            clearInterval(timerId);
            pauseTimer();
            document.getElementById('errorDisplay').textContent = 'Time is up!';
            document.getElementById('DynamicStart').textContent = 'Start';
          }
        }, 1000);
      }
    } else {
      if (timerId) {
        clearInterval(timerId);
      }
      startTime = Date.now() - elapsed * 1000;
      timerId = setInterval(() => {
        elapsed = Math.floor((Date.now() - startTime) / 1000);
        displayTime(elapsed);
      }, 1000);
    }
    running = true;
  }
}

function pauseTimer() {
  if (running) {
    clearInterval(timerId);
    running = false;
  }
}

function resetTimer() {
  clearInterval(timerId);
  elapsed = 0;
  displayTime(elapsed);
  pauseTimer();
  document.getElementById('DynamicStart').textContent = 'Start';
}

function displayTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const remainingSeconds = seconds % 60;
  document.getElementById('timer').textContent = 
    `${pad(hours)}:${pad(minutes)}:${pad(remainingSeconds)}`;
}

function pad(num) {
  return num.toString().padStart(2, '0');
}

function checkCountdown() {
  const Seconds = elapsed;
  const hours = Math.floor(Seconds / 3600);
  const minutes = Math.floor((Seconds % 3600) / 60);
  const seconds = Seconds % 60;
  if (document.getElementById('DynamicButton').textContent === 'Countdown' && hours === 0 && minutes === 0 && seconds === 0) {
    document.getElementById('errorDisplay').textContent = 'Please set a valid time!';
    return false;
  }
  return true;
}

function changeButtonText() {
  const button = document.getElementById('DynamicButton');
  // Define an array of possible button texts
  const buttonTexts = ['Countdown', 'Countup'];
  // Get the current text of the button
  const currentText = button.textContent;
  // Find the index of the current text in the buttonTexts array
  const currentIndex = buttonTexts.indexOf(currentText);
  // Calculate the index of the next text
  const nextIndex = (currentIndex + 1) % buttonTexts.length;
  // Update the button text
  button.textContent = buttonTexts[nextIndex];
  // Update the timer
  pauseTimer();
  document.getElementById('DynamicStart').textContent = 'Start';
}