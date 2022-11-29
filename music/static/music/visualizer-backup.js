
const canvas = document.querySelector('#canvas1');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const canvasCtx = canvas.getContext('2d');


// get all audio media
const audioWrapper = document.querySelector("#audio-wrapper");
const audioWrapperChildren = audioWrapper.children;
const audioMedia= [...audioWrapperChildren]

// create audioSource and analyser variables
let audioSource;
let analyser;


audioMedia.forEach(function(audio){

    audio.addEventListener("playing", function(event){

        const index = audioMedia.indexOf(event.currentTarget);

        // 1. get currently playing audio
        const audioElement = document.querySelector(`#audio${index + 1}`);

        // 2. Create audio context
        const audioCtx = new AudioContext();

        // 3. Create audio source and analyser
        audioSource = audioCtx.createMediaElementSource(audioElement);
        analyser = audioCtx.createAnalyser();
        audioSource.connect(analyser);
        analyser.connect(audioCtx.destination);

        // analyser fftSize: 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, default-2048
        analyser.fftSize = 128;

        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        const barWidth = canvas.width/bufferLength;
        let barHeight;
        let x;


        function animate() {
            x = 0;
            canvasCtx.clearRect(0, 0, canvas.width, canvas.height);
            analyser.getByteFrequencyData(dataArray);


            for(let i = 0; i < bufferLength; i++) {
                barHeight = dataArray[i];
                canvasCtx.fillStyle = "orange"
                canvasCtx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
                x += barWidth
            }
            requestAnimationFrame(animate);
        };
        animate();
    });

});