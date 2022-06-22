const visualizerContainer = document.querySelector(".visualizer-container");
const albumControlBtn = document.querySelectorAll(".album-control-btn")
const audioWrapper = document.querySelector("#audio-wrapper");
const audioWrapperChildren = audioWrapper.children;
const audioMedia= [...audioWrapperChildren]


    let numberOfBars = 130;

    for(let i = 0; i < numberOfBars; i++) {
        const bar = document.createElement("div");
        bar.setAttribute("id", "bar" + i);
        bar.setAttribute("class", "visualizer-bar")
        visualizerContainer.appendChild(bar)
    }

    audioMedia.forEach(function(audio){

        audio.addEventListener("playing", function(event){
            
            const index = audioMedia.indexOf(event.currentTarget);
            
            // 1. Get auto element 
            const audioElement = document.querySelector(`#audio${index + 1}`);
        
            // 2. Create audio context
            const audioCtx = new AudioContext();

            // 3. Create audio source 
            const audioSource = audioCtx.createMediaElementSource(audioElement);

            // 4. create analyser
            const analyser = audioCtx.createAnalyser();
            
            // 5. connect the audioSource to the analyser, and then back to the audioCtx's destination
            audioSource.connect(analyser);
            audioSource.connect(audioCtx.destination);

            // 6. print and analyze frequencies
            let frequencyData = new Uint8Array(analyser.frequencyBinCount);
            analyser.getByteFrequencyData(frequencyData);

            // this function has the task of adjusting the bar height according to the frequency data
            function renderFrame(){

                // update frequencyData array with latest frequency data
                analyser.getByteFrequencyData(frequencyData);

                for(let i = 0; i < numberOfBars; i++) {

                    // fd is the frequency data(a value between 0 and 256)
                    const fd = frequencyData[i];

                    const bar = document.querySelector(`#bar${i}`)
                    
                    if(!bar) {
                        continue;
                    }

                    const barHeight = fd || 0
                    // const barHeight = Math.max(10, fd || 0)
                    bar.style.height = `${barHeight}px`
                };
                window.requestAnimationFrame(renderFrame);
            };
            renderFrame();

        });

    });


